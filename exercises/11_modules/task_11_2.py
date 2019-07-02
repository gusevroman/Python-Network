# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится
вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью
функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

from task_11_1 import parse_cdp_neighbors


def create_network_map(filenames):
    topology = {}
    for file in filenames:
        with open(file) as f:
            sh_command = f.read()
            #print(parse_cdp_neighbors(sh_command))
            topology.update(parse_cdp_neighbors(sh_command))
    print('topology: ', topology)
    top_keys = topology.keys()
    print('top keys: ', top_keys)
    top_values = topology.values()
    print('topology.values: ', top_values)
    top_it = top_keys & top_values
    print('top it: ', top_it)
    for dic in top_keys:
        if dic in topology[dic]:
            print('dic: ', dic)
            print('topology[dic].values() ', topology[dic].values())
        #print('dic - - ', topology[dic])
        #if topology[dic] in top_keys:
            #del topology[dic]
            print(topology[dic])
    return 1


files = ['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_sw1.txt']

create_network_map(files)
'''
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), 
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'), 
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'), 
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0'), 
 ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'), 
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'), 
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'), 
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}
 
 top keys:  dict_keys([('R1', 'Eth0/0'), ('R2', 'Eth0/0'), ('R2', 'Eth0/1'), ('R3', 'Eth0/0'), ('R3', 'Eth0/1'), ('R3', 'Eth0/2'), ('SW1', 'Eth0/1'), ('SW1', 'Eth0/2'), ('SW1', 'Eth0/3'), ('SW1', 'Eth0/5')])
topology.values:  dict_values([('SW1', 'Eth0/1'), ('SW1', 'Eth0/2'), ('SW2', 'Eth0/11'), ('SW1', 'Eth0/3'), ('R4', 'Eth0/0'), ('R5', 'Eth0/0'), ('R1', 'Eth0/0'), ('R2', 'Eth0/0'), ('R3', 'Eth0/0'), ('R6', 'Eth0/1')])
top it:  {('R2', 'Eth0/0'), ('SW1', 'Eth0/3'), ('SW1', 'Eth0/1'), ('SW1', 'Eth0/2'), ('R3', 'Eth0/0'), ('R1', 'Eth0/0')}

    correct_return_value = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                            ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                            ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                            ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                            ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                            ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                            ('R6', 'Eth0/1'): ('SW1', 'Eth0/5')}

'''



