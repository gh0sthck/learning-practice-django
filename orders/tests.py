from django.test import Client, TestCase

URL_PATH = "/order"

class TemplateTest(TestCase):
    client = Client()
    
    def test_order_page(self):
        response=  self.client.get(f"{URL_PATH}/current/")
        self.assertTemplateUsed(response, template_name="orders_order.html")

    def test_barista_page(self):
        response = self.client.get(f"{URL_PATH}/queue/")
        self.assertTemplateUsed(response, template_name="orders_barista.html")


class ViewsTest(TestCase):
    client = Client()
    def test_barista_page(self):
        response = self.client.get(f"{URL_PATH}/queue/")
        self.assertEqual(response.status_code, 200)
        
    def test_current_order(self):
        response = self.client.get(f"{URL_PATH}/current/")
        self.assertEqual(response.status_code, 200)
