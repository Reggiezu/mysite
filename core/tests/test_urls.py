from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import index, settings


class TestUrl(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def settings_url_is_resolved(self):
        url = reverse('settings')
        self.assertEquals(resolve(url).func.view_class, settings)
