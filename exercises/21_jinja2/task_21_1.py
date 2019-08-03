# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
# sys.path.append('..')



def generate_config(template, data_dict):
    """
    The function's result is generated string of configuration
    :param template: path to file with template( ex. "/templates/for.txt")
    :param data_dict: dictionary with values for template
    :return: strings of configuration
    """
    router = data_dict
    template_folder, file_name = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_folder),
        trim_blocks=True,
        lstrip_blocks=True)
    template = env.get_template(file_name)
    result = template.render(router)
    print(result)
    return result


if __name__ == '__main__':
    router = yaml.safe_load(open('data_files/for.yml'))
    generate_config('templates/for.txt', router)
