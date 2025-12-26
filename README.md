
# User Management API

Простой **REST API для управления пользователями** на FastAPI с сервисным слоем, Pydantic схемами и централизованной обработкой ошибок.

---

## Структура проекта

```
app/
├── main.py           # FastAPI приложение
├── routers/          # Роутеры API
├── services/         # Сервисный слой
├── repositories/     # Работа с БД
├── schemas/          # Pydantic схемы
└── exceptions/       # Кастомные ошибки и error mapper

tests/                # Тесты Pytest
├── conftest.py       # Фикстуры
└── test_users.py
```

---

## Установка

```bash
git clone <repo_url>
cd project
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Запуск

```bash
uvicorn app.main:app --reload
```

Swagger: `http://127.0.0.1:8000/docs`
ReDoc: `http://127.0.0.1:8000/redoc`

---

## Тестирование

```bash
pytest
```

* Тестируем роутеры через **TestClient**
* Unit-тесты для сервисного слоя с моками
* Проверка ошибок и схем

---

## Основные эндпоинты

| Метод  | URL                              | Описание                       |
| ------ | -------------------------------- | ------------------------------ |
| GET    | `/users/get_users`               | Список пользователей           |
| POST   | `/users/post_new_user`           | Создать пользователя           |
| GET    | `/users/get_user_by_id/{id}`     | Получить пользователя по ID    |
| GET    | `/users/get_user_by_name/{name}` | Получить пользователя по имени |
| PATCH  | `/users/update_user/{id}`        | Обновить имя                   |
| DELETE | `/users/delete_user/{id}`        | Удалить пользователя           |

Ошибки:

* 422 — некорректные данные
* 404 — пользователь не найден
* 409 — пользователь уже существует

---

## Архитектура

* **Роутеры** - принимают запросы, чистые от логики
* **Сервисы** — бизнес-логика и проверки
* **Репозитории** — доступ к БД
* **Exceptions / Mapper** — централизованная обработка ошибок

---

Хочешь, чтобы я это сделал?
