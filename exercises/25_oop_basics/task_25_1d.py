# -*- coding: utf-8 -*-

'''
Задание 25.1d

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


'''
from pprint import pprint


topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        topology = {}
        for l_device, r_device in topology_dict.items():
            if r_device not in topology:
                topology[l_device] = r_device
        return topology

    def delete_link(self, link1, link2):
        if (link1, link2) in self.topology.items():
            del(self.topology[link1])
        elif (link2, link1) in self.topology.items():
            del(self.topology[link2])
        else:
            print('Такого соединения нет ')
        # return self.topology

    def delete_node(self, node):
        ports_with_node = {}
        for src, dst in self.topology.items():
            if node not in src and node not in dst:
                ports_with_node[src] = dst
        if len(ports_with_node) == len(self.topology):
            print('Такого устройства нет')
        else:
            self.topology = ports_with_node

    def add_link(self, link_1, link_2):
        if (link_1, link_2) in self.topology.items():
            print('Такое соединение существует')
        elif (link_2, link_1) in self.topology.items():
            print('Такое соединение существует!')
        elif link_1 in self.topology.keys() or link_2 in self.topology.keys():
            print('Cоединение с одним из портов существует')
        elif link_1 in self.topology.values() or link_2 in self.topology.values():
            print('Cоединение с одним из портов существует!')
        else:
            self.topology[link_1] = link_2


if __name__ == '__main__':
    top = Topology(topology_example)
    pprint(top.topology)
    top.add_link(('SW1', 'Eth0/1'), ('R19', 'Eth0/0'))
    pprint(top.topology)
