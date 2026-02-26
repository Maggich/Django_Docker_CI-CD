import pytest

@pytest.mark.django_db
def test_simple_check():
    assert 1 + 1 == 2

def test_admin_url(client):
    response = client.get('/admin/login/')
    assert response.status_code == 200