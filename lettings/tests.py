import pytest

from django.urls import reverse
from .models import Letting


@pytest.mark.django_db
def test_lettings_index(client):
    url = reverse('lettings_index')
    r = client.get(url)
    assert r.status_code == 200
    assert '<title>Lettings</title>' in str(r.content)


@pytest.mark.django_db
def test_letting_page(client):
    letting_title = Letting.objects.get(id=1).title
    url = reverse('letting', kwargs={'letting_id': 1})
    r = client.get(url)
    assert r.status_code == 200
    assert f'<title>{letting_title}</title>' in str(r.content)
