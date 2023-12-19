# python -m unittest tests_unitaires.py
import unittest
import requests

class TestAPI(unittest.TestCase):
    """ Classe de test de l'API basic_api_items_documentation """
    BASE_URL = "http://localhost:5000"

    # Méthodes de test pour initialiser et nettoyer la base de données
    # Ce qui nous assure de son état avant et après chaque test
    # ----------------------------------------------------------------
    def setUp(self):
        """ Ajoute des éléments à la liste des éléments (pour être sûrs qu'ils existent). """
        requests.post(f"{self.BASE_URL}/create_item/", json={"name": "test_strawberry", "price": 3})
        requests.post(f"{self.BASE_URL}/create_item/", json={"name": "test_raspberry", "price": 4})

    def tearDown(self):
        """ Supprime les éléments de la liste des éléments. """
        requests.delete(f"{self.BASE_URL}/delete_items/")
    # ----------------------------------------------------------------

    def test_create_item(self):
        """ Teste l'endpoint /create_item pour créer un élément. """
        response = requests.post(f"{self.BASE_URL}/create_item/", json={"name": "test_watermelon", "price": 1000})
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_watermelon")

    def test_get_items(self):
        """ Teste l'endpoint /get_items pour obtenir la liste des éléments. """
        response = requests.get(f"{self.BASE_URL}/get_items")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["test_strawberry"]["price"], 3)
        self.assertEqual(response.json()["test_raspberry"]["price"], 4)

    def test_get_item_is_straberry(self):
        """ Teste l'endpoint /get_item/<name> pour obtenir un élément. """
        response = requests.get(f"{self.BASE_URL}/get_item/test_strawberry")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_strawberry")
        self.assertEqual(response.json()["price"], 3)

    def test_get_item_test_foo_does_not_exist(self):
        """ Teste l'endpoint /get_item/<name> pour obtenir un élément. """
        response = requests.get(f"{self.BASE_URL}/get_item/test_foo")
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)

    def test_put_item(self):
        """ Teste l'endpoint /put_item pour mettre à jour un élément. """
        response = requests.put(f"{self.BASE_URL}/put_item", json={"name": "test_strawberry", "price": 10})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_strawberry")
        self.assertEqual(response.json()["price"], 10)

if __name__ == '__main__':
    unittest.main()
