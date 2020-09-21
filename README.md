# Highload_2020_1

## Описание

Архитектура сервер - prefork + coroutines.

- открывается сокет
- создается заданное количество рабочих процессов, каждый из которых слушает сокет
- как только процесс получает клиента по скоету, создаётся корутина, которая будет обслуживать клиента

## Подготовка

- Проинициализировать сабмодуль http-test-suite

``git submodule update --init --recursive``

- Скопировать http-test-suite/httptest/ в nginx/

``cp -r http-test-suite/httptest nginx``

## Тестирование

- чтобы запустить сервер

``sudo docker build -t pythonserver . && sudo docker run -p 80:3000 pythonserver``

- чтобы запустить nginx

``sudo docker build -t pythonserver:nginx ./nginx &&  sudo docker run -p 80:3000 pythonserver:nginx``

В таблице ниже представлены результаты прогона тестов через `httptest.py`


| №  | Nginx  | Python | Python \(aiofiles\) | Python \(sendfile\) |
|----|--------|--------|---------------------|---------------------|
| 1  | 0\.019 | 0\.055 | ?\.???              | ?\.???              |
| 2  | 0\.021 | 0\.063 | ?\.???              | ?\.???              |
| 3  | 0\.020 | 0\.086 | ?\.???              | ?\.???              |
| 4  | 0\.020 | 0\.064 | ?\.???              | ?\.???              |
| 5  | 0\.021 | 0\.069 | ?\.???              | ?\.???              |
| 6  | 0\.021 | 0\.072 | ?\.???              | ?\.???              |
| 7  | 0\.020 | 0\.072 | ?\.???              | ?\.???              |
| 8  | 0\.020 | 0\.080 | ?\.???              | ?\.???              |
| 9  | 0\.021 | 0\.075 | ?\.???              | ?\.???              |
| 10 | 0\.019 | 0\.079 | ?\.???              | ?\.???              |

 
