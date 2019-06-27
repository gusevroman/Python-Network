#!/home/vagrant/venv/pyneng-py3-7/bin/python3.7
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


from sys import argv

f = open(argv[1], 'r')
f_output = open(argv[2], 'a')

for line in f:
    if not (set(ignore) & set(line.split())):
        f_output.writelines(line)

f.close()
f_output.close()
