# Урок 2: Быстрый старт: установка SonarQube и локальное сканирование

## Что добавлено в этом уроке

| Файл | Описание |
|------|---------|
| `scan.sh` | Скрипт для запуска сканирования проекта в SonarQube |
| `vulnerable-app/utils.py` | Вспомогательные функции Python приложения |

## Структура проекта

```
github_project/
├── docker-compose.yml
├── setup-check.sh
├── scan.sh
├── sonar-project.properties
└── vulnerable-app/
    ├── app.py
    └── utils.py
```

## Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone <repository-url>
   cd github_project
   ```

2. Проверьте предварительные требования:
   ```bash
   bash setup-check.sh
   ```

3. Запустите SonarQube:
   ```bash
   docker compose up -d
   ```

4. Откройте SonarQube в браузере:
   ```
   http://localhost:9000
   ```

5. Выполните сканирование проекта:
   ```bash
   bash scan.sh
   ```

## Эволюция проекта

| Урок | Название | Новые файлы |
|------|----------|------------|
| 1 | Введение в SonarQube и его роль в безопасности | docker-compose.yml, setup-check.sh, sonar-project.properties, vulnerable-app/app.py |
| 2 | Быстрый старт: установка SonarQube и локальное сканирование | scan.sh, vulnerable-app/utils.py |

## Требования

- **Docker** и Docker Compose
- **Оперативная память**: минимум 4GB, рекомендуется 8GB
- **Свободное место на диске**: минимум 5GB
- **Порт 9000** должен быть свободен для SonarQube

## Описание компонентов

### scan.sh
Автоматизированный скрипт для запуска SonarQube Scanner и отправки результатов сканирования на сервер.

### vulnerable-app/utils.py
Вспомогательные функции приложения, содержащие примеры различных типов уязвимостей.
