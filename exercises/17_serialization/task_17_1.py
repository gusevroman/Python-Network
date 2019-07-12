# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
# print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']


def parse_sh_version(sh_version):
    '''
    The function parsing string using regular expressions and returns tuple consisting of 3 elements.
    :param sh_version: One string from output - the command sh version.(not filename)
    :return: tuple - (ios, image, uptime)
    '''
    regex = (r'Cisco IOS Software, .+Version (?P<ios>\S+),'
             r'|System image file is "(?P<image>\S+)"'
             r'|uptime is (?P<uptime>.+)')
    result = []
    match_iter = re.finditer(regex, sh_version)
    for match in match_iter:
        if match.lastgroup == 'ios':
            ios = match.group(match.lastgroup)
        if match.lastgroup == 'uptime':
            uptime = match.group(match.lastgroup)
        if match.lastgroup == 'image':
            image = match.group(match.lastgroup)
            result.append(ios)
            result.append(image)
            result.append(uptime)
    return tuple(result)


def write_inventory_to_csv(sh_version_files, csv_filename):
    '''
    The function edits information from files in list.
    :param sh_version_files:
    :param csv_filename:
    :return: write info to file routers_inventory.csv with columns: hostname, ios, image, uptime.
    '''
    regex = r'sh_version_(?P<hostname>\S+)\.'
    result = []
    result.append(headers)

    for file in sh_version_files:
        with open(file) as f:
            hostnames = []
            sh_version = f.read()
            match = re.search(regex, file)
            hostnames.append(match.group('hostname'))
            hostnames.extend(list(parse_sh_version(sh_version)))
            result.append(hostnames)
    with open(csv_filename, 'w') as dest:
        writer = csv.writer(dest)
        for row in result:
            writer.writerow(row)


csv_filename = 'routers_inventory.csv'
write_inventory_to_csv(sh_version_files, csv_filename)
