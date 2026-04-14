"""
vulnerable-app/utils.py — Вспомогательные функции с намеренными уязвимостями
==============================================================================
Курс OTUS DevSecOps: SonarQube от А до Я
Урок 2: Быстрый старт — этот файл добавлен для расширения результатов анализа

ВНИМАНИЕ: Этот код содержит НАМЕРЕННЫЕ уязвимости для учебных целей.
НЕ используйте этот код в production-окружении!

Детектируемые SonarQube CE:
  ├── SECURITY HOTSPOT:
  │   └── Insecure Random (S2245, CWE-330) — random вместо secrets ×2
  └── НЕ детектируемые CE:
      ├── Insecure deserialization (CWE-502) — pickle.loads
      ├── XML External Entity (CWE-611) — ElementTree
      ├── Open Redirect (CWE-601) — нет валидации URL
      └── SSRF (CWE-918) — urllib.request.urlopen
"""

import os
import pickle
import random
import string
import urllib.request
import xml.etree.ElementTree as ET  # noqa: S405 — намеренная уязвимость

# =============================================================================
# УЯЗВИМОСТЬ 1: Insecure Deserialization (CWE-502)
# CE: НЕ детектируется (правило S5135 существует, но не срабатывает на pickle)
# =============================================================================

def load_user_session(session_data: bytes) -> dict:
    """Загружает сессию пользователя из бинарных данных."""
    # УЯЗВИМОСТЬ: pickle.loads на данных из пользовательского ввода
    # Позволяет выполнить произвольный код при десериализации
    user = pickle.loads(session_data)  # noqa: S301 — намеренная уязвимость
    return user


def save_user_session(user: dict) -> bytes:
    """Сохраняет сессию пользователя в бинарные данные."""
    return pickle.dumps(user)


# =============================================================================
# УЯЗВИМОСТЬ 2: XML External Entity Injection — XXE (CWE-611)
# CE: НЕ детектируется (S2755 не срабатывает на xml.etree.ElementTree)
# =============================================================================

def parse_config(xml_content: str) -> dict:
    """Разбирает XML-конфигурацию пользователя."""
    # УЯЗВИМОСТЬ: стандартный ElementTree уязвим к XXE в некоторых версиях Python
    # В production нужно: defusedxml или lxml с resolve_entities=False
    root = ET.fromstring(xml_content)  # noqa: S314 — намеренная уязвимость

    config = {}
    for child in root:
        config[child.tag] = child.text
    return config


# =============================================================================
# УЯЗВИМОСТЬ 3: Insecure Random — предсказуемые токены (CWE-330)
# CE: S2245 — детектируется как Security Hotspot ×2 (строки 67 и 74)
# =============================================================================

# УЯЗВИМОСТЬ: использование random вместо secrets для генерации токенов
API_SECRET_KEY = "".join(random.choices(string.ascii_letters + string.digits, k=32))


def generate_password_reset_token(user_id: int) -> str:
    """Генерирует токен для сброса пароля."""
    # УЯЗВИМОСТЬ: random не является криптографически стойким ГПСЧ
    # Нужно использовать: secrets.token_urlsafe(32)
    token = "".join(random.choices(string.ascii_letters + string.digits, k=24))
    return f"{user_id}_{token}"


# =============================================================================
# УЯЗВИМОСТЬ 4: Server-Side Request Forgery — SSRF (CWE-918)
# CE: НЕ детектируется (нужен taint analysis → Enterprise Edition)
# =============================================================================

def fetch_remote_config(url: str) -> str:
    """Загружает конфигурацию с удалённого сервера."""
    # УЯЗВИМОСТЬ: URL передаётся из пользовательского ввода без валидации
    # Позволяет атакующему обращаться к внутренним сервисам (metadata, 169.254.x.x и т.д.)
    with urllib.request.urlopen(url) as response:  # noqa: S310 — намеренная уязвимость
        return response.read().decode("utf-8")


# =============================================================================
# УЯЗВИМОСТЬ 5: Open Redirect (CWE-601)
# CE: НЕ детектируется (нужен taint analysis → Enterprise Edition)
# =============================================================================

ALLOWED_HOSTS = ["example.com", "trusted-partner.com"]


def build_redirect_url(next_url: str, base: str = "https://example.com") -> str:
    """Формирует URL для редиректа после авторизации."""
    # УЯЗВИМОСТЬ: next_url не проверяется должным образом
    # Позволяет перенаправить пользователя на фишинговый сайт
    if next_url.startswith("/"):
        return base + next_url
    # НЕПРАВИЛЬНАЯ проверка — bypass: "https://evil.com" начинается с "http"
    if next_url.startswith("http"):
        return next_url  # УЯЗВИМОСТЬ: нет проверки хоста
    return base + "/" + next_url


# =============================================================================
# УЯЗВИМОСТЬ 6: Path Traversal в обработке файлов (CWE-22)
# CE: НЕ детектируется (нужен taint analysis → Enterprise Edition)
# =============================================================================

REPORTS_DIR = "/var/app/reports"


def read_report(report_name: str) -> str:
    """Читает отчёт по имени файла."""
    # УЯЗВИМОСТЬ: имя файла из пользовательского ввода без нормализации пути
    # Атакующий может передать: ../../etc/passwd
    report_path = os.path.join(REPORTS_DIR, report_name)
    with open(report_path) as f:  # noqa: PTH123 — намеренная уязвимость
        return f.read()


# =============================================================================
# Безопасные альтернативы (для сравнения на уроке)
# =============================================================================

def generate_secure_token(length: int = 32) -> str:
    """Правильный способ: генерация токена через secrets."""
    import secrets
    return secrets.token_urlsafe(length)


def safe_read_report(report_name: str) -> str:
    """Правильный способ: проверка пути перед чтением файла."""
    import secrets  # noqa: F401
    safe_name = os.path.basename(report_name)  # убираем path traversal
    report_path = os.path.realpath(os.path.join(REPORTS_DIR, safe_name))
    if not report_path.startswith(os.path.realpath(REPORTS_DIR)):
        raise ValueError(f"Недопустимый путь к файлу: {report_name}")
    with open(report_path) as f:
        return f.read()
