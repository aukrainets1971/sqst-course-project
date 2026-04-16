# Урок 14: Best practices и антипаттерны работы с SonarQube

## Что добавлено в этом уроке

| Файл | Описание |
|------|---------|
| `audit/configuration-audit.md` | Аудит конфигурации SonarQube и best practices |

## Структура проекта

```
github_project/
├── .gitlab/
│   └── merge_request_templates/
│       └── Default.md
├── .sonarlint/
│   └── settings.json
├── access-policy.md
├── docker-compose.yml
├── Jenkinsfile
├── fp-analysis.md
├── hotspot-review.md
├── quality-gate.json
├── setup-check.sh
├── setup-quality-gate.sh
├── scan.sh
├── sonar-project.properties
├── audit/
│   └── configuration-audit.md
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── sonar-project.properties
│   └── utils.py
├── frontend/
│   ├── app.js
│   └── sonar-project.properties
├── performance/
│   ├── docker-compose.prod.yml
│   ├── performance-baseline.md
│   └── postgresql.conf
└── vulnerable-app/
    ├── app.py
    ├── requirements.txt
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

5. Установите Quality Gate:
   ```bash
   bash setup-quality-gate.sh
   ```

6. Выполните сканирование проекта:
   ```bash
   bash scan.sh
   ```

## Эволюция проекта

| Урок | Название | Новые файлы |
|------|----------|------------|
| 1 | Введение в SonarQube и его роль в безопасности | docker-compose.yml, setup-check.sh, sonar-project.properties, vulnerable-app/app.py |
| 2 | Быстрый старт: установка SonarQube и локальное сканирование | scan.sh, vulnerable-app/utils.py |
| 3 | Основы SAST, OWASP Top 10 и Secure SDLC | (без новых файлов) |
| 4 | Интеграция SonarQube с CI/CD (GitLab, Jenkins) | Jenkinsfile |
| 5 | Кастомизация Quality Gate, правил и работа с замечаниями | quality-gate.json, setup-quality-gate.sh |
| 6 | False Positive / False Negative: системный подход | fp-analysis.md |
| 7 | Security Hotspots и митигация уязвимостей | hotspot-review.md |
| 8 | Анализ разных языков и фреймворков | frontend/app.js, frontend/sonar-project.properties |
| 9 | Анализ open-source компонентов и зависимостей | vulnerable-app/requirements.txt |
| 10 | Взаимодействие с разработкой и код-ревью | .sonarlint/settings.json, .gitlab/merge_request_templates/Default.md |
| 11 | Монорепозитории и многомодульные проекты | backend/app.py, backend/utils.py, backend/requirements.txt, backend/sonar-project.properties |
| 12 | Безопасность платформы и контроль доступа в SonarQube | access-policy.md |
| 13 | Масштабирование и производительность SonarQube | performance/docker-compose.prod.yml, performance/postgresql.conf, performance/performance-baseline.md |
| 14 | Best practices и антипаттерны работы с SonarQube | audit/configuration-audit.md |

## Требования

- **Docker** и Docker Compose
- **Оперативная память**: минимум 4GB, рекомендуется 8GB (для production рекомендуется 16GB+)
- **Свободное место на диске**: минимум 5GB (для production рекомендуется 50GB+)
- **Порт 9000** должен быть свободен для SonarQube

## Описание компонентов

### audit/configuration-audit.md
Полный аудит конфигурации SonarQube включающий:
- Best practices по настройке и управлению платформой
- Антипаттерны и типичные ошибки при внедрении
- Рекомендации по оптимизации работы команды
- Чек-листы для обеспечения качества и безопасности
- Метрики и KPI для оценки эффективности работы с SonarQube
