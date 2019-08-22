# -*- coding: utf-8 -*-

'''
Задание 26.1a

В этом задании надо сделать так, чтобы экземпляры класса Topology были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 25.1x или задания 26.1.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
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

    def __add__(self, other):
        """
        Addition of two instances of the Topology class
        """
        sum_instance = Topology(self.topology)
        sum_instance.topology.update(other.topology)
        return sum_instance

    def __iter__(self):
        return iter(self.topology.items())

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
    t1 = Topology(topology_example)
    for link in t1:
        print(link)