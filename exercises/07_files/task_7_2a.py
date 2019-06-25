#!/home/vagrant/venv/pyneng-py3-7/bin/python3.7
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


from sys import argv

f = open(argv[1], 'r')
print('-' * 50)
for line in f:
    if not line.startswith('!') and not (set(ignore) & set(line.split())):
        print(line, end='')