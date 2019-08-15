# -*- coding: utf-8 -*-

'''
Задание 25.2

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
* _write_line - принимает как аргумент строку и отправляет на оборудование строку преобразованную в байты и добавляет
перевод строки в конце.
  Метод _write_line должен использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод полученный с обрудования

Пример создания экземпляра класса:
In [2]: from task_25_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command('sh ip int br')
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthern<<et0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

'''
import telnetlib
import time


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

    def send_show_command(self, command):
        """
        The method takes the show command as an argument and returns the output received from the device
        :param command:
        :return:
        """
        self._write_line(command)
        time.sleep(1)
        output = self.telnet.read_very_eager().decode('ascii')
        self.check_errors(output)
        return output

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
    print(r1.send_show_command('sh ip int br'))
    # r1.close()
