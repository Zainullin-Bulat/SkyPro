import pytest
import requests

# Вписать сущ. ключ
API_KEY = "key"
BASE_URL = "https://ru.yougile.com/api-v2"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


class TestProjects:

    @pytest.fixture(scope="class")
# Создание и привязка по ID
    def project_id(self):
        project_data = {
            "title": "Тест 1"
        }

        response = requests.post(
            f"{BASE_URL}/projects",
            json=project_data,
            headers=headers
        )
        assert response.status_code == 201
        return response.json()["id"]

    def test_create_project_positive(self, project_id):
        response = requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id

# Создание без названия
    def test_create_project_negative_no_data(self):
        response = requests.post(
            f"{BASE_URL}/projects",
            json={},
            headers=headers
        )
        assert response.status_code == 400

# Получение по сущ. ID
    def test_get_project_positive(self, project_id):
        response = requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id

# Получение по несущ. ID
    def test_get_project_negative_invalid_id(self):
        response = requests.get(
            f"{BASE_URL}/projects/000",
            headers=headers
        )
        assert response.status_code in [400, 404]

# Обновление по сущ. ID
    def test_update_project_positive(self, project_id):
        """Позитивный тест обновления проекта"""
        update_data = {
            "title": "Тест 2"
        }
        response = requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=update_data,
            headers=headers
        )
        assert response.status_code == 200

# Обновление по несущ. ID
    def test_update_project_negative_invalid_id(self):
        update_data = {
            "title": "Тест 3"
        }
        response = requests.put(
            f"{BASE_URL}/projects/000",
            json=update_data,
            headers=headers
        )
        assert response.status_code in [400, 404]
