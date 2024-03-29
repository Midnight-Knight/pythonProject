import os

def load_config(filename):
    config = {}
    with open(filename) as f:
        code = compile(f.read(), os.path.abspath(filename), 'exec')
        exec(code, config)
    return config

"""
Плюсы использования импорта для загрузки конфигурации:

Конфигурационные переменные могут быть использованы как глобальные переменные в модуле, что может быть удобно для обращения к ним из разных функций.

Если файл конфигурации находится в том же каталоге, что и модуль, то его можно загрузить с помощью стандартного импорта, что делает использование 
конфигурации еще более простым.


Минусы использования импорта для загрузки конфигурации:

Можно нечаянно переопределить или использовать неизвестные переменные, что может привести к ошибкам в работе программы.

При изменении переменных в файле конфигурации может потребоваться перезапуск программы, чтобы изменения вступили в силу.


Плюсы использования прямого выполнения кода для загрузки конфигурации:

Все переменные в файле конфигурации будут загружены и доступны в словаре, что удобно для использования в коде программы.

Изменения в файле конфигурации вступят в силу немедленно, без необходимости перезапуска программы.


Минусы использования прямого выполнения кода для загрузки конфигурации:

Можно нечаянно переопределить или использовать неизвестные переменные, что может привести к ошибкам в работе программы.

Код в файле конфигу
"""