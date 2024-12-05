# Test Automation Framework

## Налаштування

1. Клонуйте репозиторій
2. Створіть віртуальне середовище та активуйте його
3. Встановіть залежності
4. Запустіть встановлення Playwright
5. Запустіть тести за допомогою pytest

```bash
git clone <repository-url>
cd test_automation_framework
python -m venv venv
source venv/bin/activate  # Для Windows використовуйте `venv\Scripts\activate`
pip install -r requirements.txt
playwright install
pytest
```

## Структура
*   config/: Конфігураційні файли
*   pages/: Класи об'єктів сторінок
*   tests/: Тестові випадки, організовані за типом
*   utils/: Утиліти
*   .github/: Конфігурація CI/CD
##Запуск Тестів
Щоб запустити тести, виконайте наступну команду:
```bash
pytest
```
## Конфігурація Середовища
Встановіть змінну середовища ENV для перемикання між конфігураціями:
```bash
export ENV=staging
```
