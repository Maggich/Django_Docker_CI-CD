import pytest
from django.urls import reverse

def test_python_math():
    """Простейшая проверка, что 2+2 всё еще 4"""
    assert 2 + 2 == 4

@pytest.mark.django_db
def test_admin_page_available(client):
    """Проверяем, что страница логина в админку доступна"""
    url = reverse('admin:login')
    response = client.get(url)
    assert response.status_code == 200