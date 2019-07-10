# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re


def parse_sh_ip_int_br(dev_cfg):
    '''
    The function edits command show ip int br
    :param dev_cfg: file with output from command show ip int br
    :return: dev_status: Interface, IP-Address,  Status, Protocol - The list of tuples:
    '''
    # v.1
    # regex = (r'^(\S+) +'
    #          # r'([\d.]+|unassigned) +'
    #          r'(\S+) +'
    #          r'\w+ +\w+ +'
    #          r'(up|down|administratively down) +'
    #          r'(up|down)')

    # v.2
    regex = '(\S+) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'
    with open(dev_cfg) as f:
        line = f.read()
        match_iter = re.finditer(regex, line)
        dev_status = []
        for match in match_iter:
            dev_status.append(match.groups())
    return dev_status

dev_config = 'sh_ip_int_br.txt'
