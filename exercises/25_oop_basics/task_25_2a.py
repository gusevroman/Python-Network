# -*- coding: utf-8 -*-
"""
Задание 25.2a

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, полученные после обработки с
помощью TextFSM. При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами



Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_25_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command('sh ip int br', parse=False)
Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

In [5]: r1.send_show_command('sh ip int br', parse=True)
Out[5]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '190.16.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.100',
  'address': '10.100.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.200',
  'address': '10.200.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.300',
  'address': '10.30.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback0',
  'address': '10.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback55',
  'address': '5.5.5.5',
  'status': 'up',
  'protocol': 'up'}]
"""
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

    def _write_line(self, line_for_send):
        """
        the method takes a string as an argument and sends the string converted to bytes to the device and adds the
        end of line at the end.
        """
        self.telnet.write(line_for_send.encode('ascii') + b'\n')
        return


if __name__ == '__main__':
    r1 = CiscoTelnet(**r1_params)
    pprint(r1.send_show_command('sh ip int br', templates='templates', parse=True))
