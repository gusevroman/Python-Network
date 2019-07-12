# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут оlдинаковыми (inside,outside).
'''
import re


def convert_ios_nat_to_asa(nat_ios, nat_asa):
    '''
    The Function converts rules NAT from Cisco IOS into Cisco ASA
    :param nat_ios: file with rules Cisco IOS, for example cisco_nat_config.txt
    :param nat_asa: file with converted rules
    :return:
    '''
    regex = re.compile(r'(?P<host>[\d.]+) '
                      r'(?P<port>[\d.]+).+'
                      r' (?P<ports>[\d.]+)')


    with open(nat_ios) as src, open(nat_asa, 'w') as dest:
        for line in src.readlines():
            match = re.finditer(regex, line)
            for m in match:
                host, port, ports = m.groups()
                line_dest = f'''
object network LOCAL_{host}
 host {host}
 nat (inside,outside) static interface service tcp {port} {ports}'''
                dest.write(line_dest)


convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_nat_asa.txt')