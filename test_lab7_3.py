# Testy - Zadanie 3
import unittest
import requests
import pickle
import sys
from lab7_3 import BagOfWords

class TestBagOfWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "http://www.gutenberg.org/cache/epub/1787/pg1787.txt"
        response = requests.get(url)
        cls.hamlet_text = response.text
        cls.other_text = "Some different text"

    def test_equality_same_text(self):
        bow1 = BagOfWords(self.hamlet_text)
        bow2 = BagOfWords(self.hamlet_text)
        self.assertEqual(bow1, bow2)

    def test_inequality_different_text(self):
        bow1 = BagOfWords(self.hamlet_text)
        bow2 = BagOfWords(self.other_text)
        self.assertNotEqual(bow1, bow2)

    def test_serialization_deserialization(self):
        bow_original = BagOfWords(self.hamlet_text)
        with open("test_bow.pkl", "wb") as file:
            pickle.dump(bow_original, file)
        with open("test_bow.pkl", "rb") as file:
            bow_loaded = pickle.load(file)
        self.assertEqual(bow_original, bow_loaded)

    def test_memory_size_comparison(self):
        bow_original = BagOfWords(self.hamlet_text)
        with open("test_bow.pkl", "wb") as file:
            pickle.dump(bow_original, file)
        with open("test_bow.pkl", "rb") as file:
            bow_loaded = pickle.load(file)
        size_original = sys.getsizeof(pickle.dumps(bow_original))
        size_loaded = sys.getsizeof(pickle.dumps(bow_loaded))
        self.assertEqual(size_original, size_loaded)

if __name__ == '__main__':
    unittest.main()
