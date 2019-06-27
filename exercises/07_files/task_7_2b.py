#!/home/vagrant/venv/pyneng-py3-7/bin/python3.7
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

f = open(argv[1], 'r')
f_output = open('config_sw1_cleared.txt', 'a')

for line in f:
    if not (set(ignore) & set(line.split())):
        f_output.writelines(line)

f.close()
f_output.close()
