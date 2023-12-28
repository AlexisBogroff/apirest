# python -m unittest tests_unitaires.py
import unittest
import requests
import pandas as pd
import basic_api_items_documentation as api_script


class TestAPI(unittest.TestCase):
    """ Classe de test de l'API basic_api_items_documentation """
    BASE_URL = "http://localhost:5000"

    def __init__(self, *args, **kwargs):
        super(TestAPI, self).__init__(*args, **kwargs)
        self.df = pd.DataFrame({'id': [1, 2, 3], 'name': ['j', 'k', 'l'], 'price': [40, 28, 210]})

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

    def test_mult_2_fois_3_egal_6(self):
        self.assertEqual(api_script.mult(2, 3), 6)

    def test_mult_2_fois_3_egal_7(self):
        self.assertNotEqual(api_script.mult(2, 3), 7)

    def test_mult_2_fois_3_egal_6_avec_une_precision_de_2(self):
        self.assertAlmostEqual(api_script.mult(2, 3), 6, places=2)

    def test_mult_2_fois_3_egal_6_avec_une_precision_de_3(self):
        self.assertAlmostEqual(api_script.mult(2.0001, 3.000001), 6, places=3)

    def test_create_item(self):
        # Exécuter la fonction à tester et récupérer le résultat
        response = requests.post(f"{self.BASE_URL}/create_item/", json={"name": "test_watermelon", "price": 1000})
        # Vérifier que le résultat est comme attendu
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_watermelon")

    def test_get_items_status_code_is_200(self):
        response = requests.get(f"{self.BASE_URL}/get_items")
        self.assertEqual(response.status_code, 200)

    def test_get_items_response_format_is_dict(self):
        response = requests.get(f"{self.BASE_URL}/get_items")
        self.assertIsInstance(response.json(), dict)
        
    def test_get_items_response_contains_test_strawberry_with_correct_price(self):
        response = requests.get(f"{self.BASE_URL}/get_items")
        self.assertEqual(response.json()["test_strawberry"]["price"], 3)
        self.assertEqual(response.json()["test_raspberry"]["price"], 4)

    def test_get_item_is_straberry(self):
        response = requests.get(f"{self.BASE_URL}/get_item/test_strawberry")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_strawberry")
        self.assertEqual(response.json()["price"], 3)

    def test_get_item_test_foo_does_not_exist(self):
        response = requests.get(f"{self.BASE_URL}/get_item/test_foo")
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)

    def test_put_item(self):
        response = requests.put(f"{self.BASE_URL}/put_item", json={"name": "test_strawberry", "price": 10})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["name"], "test_strawberry")
        self.assertEqual(response.json()["price"], 10)

if __name__ == '__main__':
    unittest.main()
