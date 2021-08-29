import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles_index')
    r = client.get(url)
    assert r.status_code == 200
    assert '<title>Profiles</title>' in str(r.content)


@pytest.mark.django_db
def test_profile_page(client):
    url = reverse('profile', kwargs={'username': 'HeadlinesGazer'})
    r = client.get(url)
    assert r.status_code == 200
    assert '<title>HeadlinesGazer</title>' in str(r.content)
