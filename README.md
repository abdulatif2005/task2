# Task2 Project

## Структура репозитория

1. **tests** = tests (папка с тестами)
2. **code** = patient (основная папка с кодом)
3. **docker** = dockerfile (файл Docker для сборки контейнера)
4. **migrations** = patient/migrations (путь до файлов миграций в БД)

---

## Инструкции по локальному запуску

### Шаг 1: Убедитесь, что у вас установлены:
- Docker

---

### Шаг 2: Сборка и запуск контейнера
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/abdulatif2005/task2.git
   cd task2
2. Соберите Docker-образ:
   ```bash
   docker build -t task2-app .
3. Запустите контейнер:
   ```bash
   docker run --name task2 -p 8000:8000 task2-app
   
### Шаг 3: Отправка запросов к серверу
1. После запуска сервер будет доступен по адресу:
   http://localhost:8000
2. Используйте curl, Postman или любую библиотеку (например, requests в Python) для отправки запросов.

### Тестирование
1. Для запуска тестов выполните:
   ```bash
   
   docker exec -it task2 pytest --cov=. --cov-report=html
2. Для просмотра отчета тестов:
   1. сначало выполните(это скопирует отчет из контейнера в хост)
      ```bash
      docker cp task:/htmlcov ./htmlcov
      ```
   2. теперь после того как вы скопировали **htmlcov** перейдите на эту папку и откройте файл **index.html**
