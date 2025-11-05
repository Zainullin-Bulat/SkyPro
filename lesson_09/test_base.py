import pytest
from sqlalchemy import create_engine, text

# Подключение к БД
db_connection_string = "postgresql://postgres:1103@localhost:5432/postgres"
engine = create_engine(db_connection_string)


@pytest.fixture
def db():
    with engine.connect() as conn:
        yield conn


def test_add(db):
    # Добавление
    with db.begin():
        db.execute(text("INSERT INTO students "
                        "(name, email) VALUES ('Булат', 'bulat@test.ru')"))

    # Проверка
    result = db.execute(text("SELECT * FROM students "
                        "WHERE email = 'bulat@test.ru'")).fetchone()
    assert result[1] == 'Булат'

    # Очистка
    with db.begin():
        db.execute(text("DELETE FROM students WHERE email = 'bulat@test.ru'"))


def test_update(db):
    # Добавляем для изменения
    with db.begin():
        db.execute(text("INSERT INTO students"
                        " (name, email) VALUES ('Булат', 'bulat@test.ru')"))

    # Изменение
    with db.begin():
        db.execute(text("UPDATE students "
                        "SET name = 'Булат Зайнуллин' "
                        "WHERE email = 'bulat@test.ru'"))

    # Проверка
    result = db.execute(text("SELECT * FROM students "
                        "WHERE email = 'bulat@test.ru'")).fetchone()
    assert result[1] == 'Булат Зайнуллин'

    # Очистка
    with db.begin():
        db.execute(text("DELETE FROM students WHERE email = 'bulat@test.ru'"))


def test_delete(db):
    # Добавляем для удаления
    with db.begin():
        db.execute(text("INSERT INTO students "
                        "(name, email) VALUES ('Булат', 'bulat@test.ru')"))

    # Удаление
    with db.begin():
        db.execute(text("DELETE FROM students WHERE email = 'bulat@test.ru'"))

    # Проверка
    result = db.execute(text("SELECT * FROM students "
                        "WHERE email = 'bulat@test.ru'")).fetchone()
    assert result is None
