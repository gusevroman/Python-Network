# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (п чале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
    '''
    Функция обрабатывает конфигурационный файл коммутатора и возвращает словарь:
    - ключи - все команды верхнего уровня (глобального режима конфигурации)
    - если есть подкоманды, то они должны быть в значении ключа
    - если нет подкоманд, то значение будет пустым списком
    используется функция ignore_command для определения строки которую нужно игнорировать
    :return: словарь config_mode_template
    '''
    config_mode_template = {}

    with open(config_filename) as f:
        for line in f:
            if not line.startswith('!') and not ignore_command(line, ignore) and not line.startswith('\n') and not line.startswith(' '):
                intf = line.strip()
                config_mode_template.setdefault(intf, [])
                command = []
            if not line.startswith('!') and not ignore_command(line, ignore) and not line.startswith('\n') and line.startswith(' '):
                command.append(line.strip())
                config_mode_template[intf] = command

    return config_mode_template


print(convert_config_to_dict('config_sw1.txt'))