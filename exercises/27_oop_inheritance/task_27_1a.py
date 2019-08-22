# -*- coding: utf-8 -*-

'''
Задание 27.1a

Дополнить класс CiscoSSH из задания 27.1.

Перед подключением по SSH необходимо проверить если ли в словаре
с параметрами подключения такие параметры: username, password, secret.
Если нет, запросить их у пользователя, а затем выполнять подключение.

In [1]: from task_27_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'ip': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Введите имя пользователя: cisco
Введите пароль:
Введите пароль для режима enable:

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
from base_connect_class import BaseSSH


device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1'
}


class CiscoSSH(BaseSSH):
    def __init__(self, disable_paging=True, **device_params):
        if 'username' not in device_params.keys():
            device_params['username'] = input('Введите имя пользователя: ')
        if 'password' not in device_params.keys():
            device_params['password'] = input('Введите пароль: ')
        if 'secret' not in device_params.keys():
            device_params['secret'] = input('Введите пароль для режима enable: ')
        super().__init__(**device_params)



if __name__ == '__main__':
    r1 = CiscoSSH(**device_params)
    r1.send_show_command('sh ip int br')

# Все отлично
# только лучше этот код поместить в __init__

# вариант решения

from base_connect_class import BaseSSH
from getpass import getpass

class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        params = {'username': 'Введите имя пользователя: ',
                  'password': 'Введите пароль: ',
                  'secret': 'Введите пароль для режима enable: '}
        for param in params:
            if not param in device_params:
                if param == 'username':
                    device_params['username'] = input(params[param])
                else:
                    device_params[param] = getpass(params[param])
        super().__init__(**device_params)
        self.ssh.enable()

# еще один вариант
class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        params = {'username': (input, 'Введите имя пользователя: '),
                  'password': (getpass, 'Введите пароль: '),
                  'secret': (getpass, 'Введите пароль для режима enable: ')}
        for param in params:
            if not param in device_params:
                function, question = params[param]
                device_params[param] = function(question)
        super().__init__(**device_params)
        self.ssh.enable()
