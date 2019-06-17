# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# Variant 1
'''
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

ospf_route = ospf_route.replace('[', '')
ospf_route = ospf_route.replace(']', '')
ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.split()
protocol = 'OSPF'

print('{:23}{}'.format(ospf_keys[0]+':', protocol))
print('{:23}{}'.format(ospf_keys[1]+':', ospf_route[1]))
print('{:23}{}'.format(ospf_keys[2]+':', ospf_route[2]))
print('{:23}{}'.format(ospf_keys[3]+':', ospf_route[4]))
print('{:23}{}'.format(ospf_keys[4]+':', ospf_route[5]))
print('{:23}{}'.format(ospf_keys[5]+':', ospf_route[6]))
'''
# Variant 2:

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('[', '') # убираем лишние квадратные скобки
ospf_route = ospf_route.replace(']', '') # убираем лишние квадратные скобки
ospf_route = ospf_route.replace(',', '') # убираем лишние запятые
f = ospf_route.split() # получился список

ip_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface     {}
'''
print(ip_template.format('OSPF', f[1], f[2], f[4], f[5], f[6]))

# Все отлично

# вариант решения

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = '''
{:25} {}
{:25} {}
{:25} {}
{:25} {}
{:25} {}
{:25} {}
'''

## еще один вариант шаблона
output = '\n{:25} {}'*6

#### Первый вариант: использование срезов
route = ospf_route.split()

print(output.format('Protocol:', 'OSPF',
                    'Prefix:', route[1],
                    'AD/Metric:', route[2][1:-1],
                    'Next-Hop:', route[4][:-1],
                    'Last update:', route[5][:-1],
                    'Outbound Interface:', route[6]))

#### Второй вариант: предварительная обработка строки

# удаляем лишние символы
route = ospf_route.replace(',', ' ').replace('[','').replace(']', '')

# Таким образом можно присвоить несколько переменных за один раз:
_, prefix, ad_metric, _, nhop, update, intf = route.split()

# Тут символ нижнего подчеркивания выполняет специальную роль -
# это те значения, которые нам не нужны и мы хотим их просто выбросить.
# Как вариант, можно было написать и нормальные имена переменных,
# но таким образом, мы явно указываем, что нам не нужны эти значения
# и мы их просто выбрасываем.


print( output.format("Protocol:", "OSPF",
                     "Prefix:", prefix,
                     "AD/Metric:", ad_metric,
                     "Next-Hop:", nhop,
                     "Last update:", update,
                     "Outbound Interface:", intf))

