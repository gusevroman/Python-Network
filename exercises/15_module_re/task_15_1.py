# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def get_ip_from_cfg(dev_cfg):
    '''
    The function edits a configuration the device
    :return: ip_mask_cfg    # the list of tuples - ip-address, mask
    '''
    ip_mask_cfg = []
    regex = re.compile(' ip address +(?P<ip_address>\S+) +(?P<mask>\S+)')
    with open(dev_cfg) as f:
        for line in f.readlines():
            match = regex.search(line)
            if match:
                ip_mask_cfg.append(match.groups())
    return ip_mask_cfg

dev_config = 'config_r1.txt'
print(get_ip_from_cfg(dev_config))