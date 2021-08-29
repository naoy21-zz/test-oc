from django.urls import reverse


def test_index(client):
    url = reverse('index')
    r = client.get(url)
    assert r.status_code == 200
    assert '<title>Holiday Homes</title>' in str(r.content)
