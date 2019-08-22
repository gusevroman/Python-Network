# -*- coding: utf-8 -*-

'''
Задание 26.2

Добавить к классу CiscoTelnet из задания 25.2x поддержку работы в менеджере контекста.
При выходе из блока менеджера контекста должно закрываться соединение.
Все исключения, которые возникли в менеджере контекста, должны генерироваться после выхода из блока with.

Пример работы:

In [14]: r1_params = {
    ...:     'ip': '192.168.100.1',
    ...:     'username': 'cisco',
    ...:     'password': 'cisco',
    ...:     'secret': 'cisco'}

In [15]: from task_26_2 import CiscoTelnet

In [16]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:
sh clock
*19:17:20.244 UTC Sat Apr 6 2019
R1#

In [17]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:     raise ValueError('Возникла ошибка')
    ...:
sh clock
*19:17:38.828 UTC Sat Apr 6 2019
R1#
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-f3141be7c129> in <module>
      1 with CiscoTelnet(**r1_params) as r1:
      2     print(r1.send_show_command('sh clock'))
----> 3     raise ValueError('Возникла ошибка')
      4

ValueError: Возникла ошибка
'''
import telnetlib
import time
from textfsm import clitable
from pprint import pprint
from datetime import datetime
import logging


logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


r1_params = {'ip': '192.168.100.1',
             'username': 'cisco',
             'password': 'cisco',
             'secret': 'cisco'}


class CiscoTelnet:
    def __init__(self, ip, username, password, secret=None,
                 disable_paging=True):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        # self.telnet.write(username.encode('ascii') + b'\n')
        self._write_line(username)

        self.telnet.read_until(b'Password:')
        # self.telnet.write(password.encode('ascii') + b'\n')
        self._write_line(password)
        if secret:
            self.telnet.write(b'enable\n')
            self.telnet.read_until(b'Password:')
            # self.telnet.write(secret.encode('ascii') + b'\n')
            self._write_line(secret)
        if disable_paging:
            self.telnet.write(b'terminal length 0\n')
        time.sleep(0.5)
        self.telnet.read_very_eager()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.telnet.close()

    def send_show_command(self, command, templates, parse=True):
        """
        The method takes the show command as an argument and returns the output received from the device
        :param command: for send to device
        :param parse: controls whether normal command output or a list of dictionaries received after processing with
        using TextFSM. If parse=True then return a list jf dictionaries. If parse=False read string from command output
        :param templates: path to directory with templates
        :return:
        """
        start_msg = '===> {} Connection TO: {}'
        received_msg = '<=== {} Received FROM:  {}'
        logging.info(start_msg.format(datetime.now().time(), self.ip))

        self._write_line(command)
        time.sleep(1)
        # read string from command output
        output = self.telnet.read_very_eager().decode('ascii')
        self.check_errors(output)

        if parse:
            # call method _parse
            result = self._parse(output, command, templates)
        else:
            # return just string from command output
            result = output

        logging.info(received_msg.format(datetime.now().time(), self.ip))

        return result

    def _parse(self, command_output, command, templates_path):
        """
        parsing result of command_output (with TextFSM)
        :return:  a list jf dictionaries
        """
        result = []
        vendor = 'cisco_ios'

        attributes = {'Command': command, 'Vendor': vendor}
        cli_table = clitable.CliTable('index', templates_path)
        cli_table.ParseCmd(command_output, attributes)
        header = list(cli_table.header)
        for item in cli_table:
            result_dict = dict(zip(header, item))
            result.append(result_dict)

        return result

    def close(self):
        self.telnet.close()

    def check_errors(self, command_output):
        if 'Invalid input detected' in command_output:
            raise ValueError("Возникла ошибка Invalid input detected")

    def config_mode(self):
        self.telnet.write(b'conf t\n')
        time.sleep(0.5)
        return self.telnet.read_very_eager().decode('ascii')

    def exit_config_mode(self):
        self.telnet.write(b'end\n')
        time.sleep(0.5)
        return self.telnet.read_very_eager().decode('ascii')

    def send_config_commands(self, commands):
        if type(commands) == str:
            commands = [commands]
        output = self.config_mode()
        for command in commands:
            self._write_line(command)
            time.sleep(0.2)
        output += self.telnet.read_very_eager().decode('ascii')
        output += self.exit_config_mode()
        return output

    def _write_line(self, line_for_send):
        """
        the method takes a string as an argument and sends the string converted to bytes to the device and adds the
        end of line at the end.
        """
        self.telnet.write(line_for_send.encode('ascii') + b'\n')
        return


if __name__ == '__main__':
    # r1 = CiscoTelnet(**r1_params)
    # print(r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))
    with CiscoTelnet(**r1_params) as connect_to_router:
        print(connect_to_router.send_show_command('sh ip int br', 'templates'))

