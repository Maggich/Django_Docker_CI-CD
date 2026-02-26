import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_products():
    client = Client()
    response = client.get("/api/products/")
    assert response.status_code == 200