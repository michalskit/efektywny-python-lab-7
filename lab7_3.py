# Zadanie 3

# Zastąp pass Twoim kodem

import requests
import sys
import pickle
from lab7_2 import BagOfWords

# Dodaj odpowiednią metodę do BagOfWords, która pozwoli na porównanie 
# print(bow_hamlet == loaded_bow_hamlet) # True
class BagOfWords(BagOfWords):
    pass

# Uruchomienie na tekście Hamleta
url = "http://www.gutenberg.org/cache/epub/1787/pg1787.txt"
response = requests.get(url)
hamlet_text = response.text

bow_hamlet = BagOfWords(hamlet_text)

# Zapisanie obiektu bow_hamlet do pliku (pickle)
pass

# Odczytanie obiektu z pliku
pass

# Porównanie obiektów
print(bow_hamlet == loaded_bow_hamlet) # True

# Obliczenie rozmiaru instancji w pamięci
pass

print(size_loaded_bow_hamlet ==  size_bow_hamlet) # True