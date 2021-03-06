# Highload_2020_1

## Описание

Архитектура сервер - prefork + coroutines.

- открывается сокет
- создается заданное количество рабочих процессов, каждый из которых слушает сокет
- как только процесс получает клиента по сокету, создаётся корутина, которая будет обслуживать клиента

## Подготовка

- Проинициализировать сабмодуль http-test-suite

``git submodule update --init --recursive``

- Скопировать http-test-suite/httptest/ в nginx/

``cp -r http-test-suite/httptest nginx``

## Тестирование

### Python

**ВНИМАНИЕ:** сервер поддерживает использование _**sendfile**_. \
При включении в конфиге опции _**sendfile**_ не рекомендуется использовать данный докер 
(он почему-то не дружит с _**sendfile**_ и, насколько я понял, обрывает его на середине)

**ВНИМАНИЕ:** у сервера есть **максимальное количество одновременных подключений
(`max_connections * workers_process_amount`).** 
Если количество параллельных подключений превысит максимальное,
то некоторые запросы могут остаться в "подвешенном" состоянии (без ответа и закрытия).
Если вы хотите увеличить количесвто одновременных параллельных подключений,
измените переменную `max_connections` в файле `config.py`

- чтобы запустить сервер без _**sendfile**_

``sudo docker build -t pythonserver . && sudo docker run -p 80:3000 pythonserver``

- чтобы запустить сервер с _**sendfile**_

    - установить python 3.6.9 (другие версии не проверялись)
    
    - создать и активировать виртуальное окружение
    
    ``python3.6 -m venv env && . env/bin/activate``
    
    - установить зависимости
    
    `` pip install -r requirements.txt``
    
    - выставить `sendfile = True` в config.py
    
    - запустить сервер (он будет работать на 3000 порту)
    
    ``python main.py``
    

### Nginx

- чтобы запустить nginx

``sudo docker build -t pythonserver:nginx ./nginx &&  sudo docker run -p 80:3000 pythonserver:nginx``

## Результаты

Параметры системы:

- OS: Ubuntu 18.04.4 LTS
- Processor: Intel® Core™ i7-7700 CPU @ 3.60GHz × 8 
- Hard drive: WDC WD10EZEX-08W
- Python: 3.6.9

#### Тесты

![Тесты](/test_results/test_results.png)

#### Nginx (4 ядра, докер)

![Nginx, cpu = 4, docker](/test_results/nginx_cpu4_docker.png)

#### Python (1 ядро, докер, sendfile = False)

![Python, cpu = 1, docker, sendfile off](/test_results/python_cpu1_docker.png)

#### Python (4 ядра, докер, sendfile = False)

![Python, cpu = 4, docker, sendfile off](/test_results/python_cpu4_docker.png)

#### Python (1 ядро, ~~докер~~, sendfile = True)

![Python, cpu = 1, no docker, sendfile on](/test_results/python_cpu1_nodocker_sendfile.png)

#### Python (4 ядро, ~~докер~~, sendfile = True)

![Python, cpu = 4, no docker, sendfile on](/test_results/python_cpu4_nodocker_sendfile.png)