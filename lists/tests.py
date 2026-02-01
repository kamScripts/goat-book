from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
class HomePageTests(TestCase):
#    def test_home_page_returns_correct_html(self):
#        request = HttpRequest()
#        response = home_page(request)
#        html = response.content.decode('utf-8')
#        self.assertIn('<title>To-Do Lists</title>', html)
#        self.assertTrue(html.startswith('<html>'))
#        self.assertTrue(html.endswith('</html>'))
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>To-Do Lists</title>')
        self.assertContains(response, '<html lang="en">')
        self.assertContains(response, '</html>')
        self.assertTemplateUsed(response, 'home.html')
    def test_renders_homepage_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'To-Do')