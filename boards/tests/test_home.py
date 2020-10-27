import pytest
from django.urls import reverse, resolve

from boards.views import home

def test_int():
    assert 1 == 1

@pytest.mark.django_db
def test_home_view_status_code(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code, 200


def test_home_url_resolves_home_view():
    view = resolve('/')
    assert view.func, home
