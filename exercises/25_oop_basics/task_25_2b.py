# -*- coding: utf-8 -*-

'''
Задание 25.2b

Скопировать класс CiscoTelnet из задания 25.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного режима или список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_25_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

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
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))
