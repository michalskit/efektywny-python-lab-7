# Testy - Zadanie 4
import unittest
import os
import json
from lab7_4 import BagOfWords 

class TestBagOfWords(unittest.TestCase):

    def setUp(self):
        self.test_text = "Hello world. Hello again!"
        self.test_file = "test_bow.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        bow = BagOfWords(self.test_text)
        bow.save(self.test_file)

        # Ensure file is saved
        self.assertTrue(os.path.exists(self.test_file))

        # Check the contents of the saved file
        with open(self.test_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, bow.word_counts)

        # Load the data and check if it matches
        new_bow = BagOfWords("")
        new_bow.load(self.test_file)
        self.assertEqual(new_bow.word_counts, bow.word_counts)


if __name__ == '__main__':
    unittest.main()
