# Testy - Zadanie 5
import unittest
from lab7_5 import get_current_time_in_countries


class TestGetCurrentTimeInCountries(unittest.TestCase):

    def test_single_country_single_timezone(self):
        test_countries = [
            {'timezones': ['Europe/London'], 'code': 'GB', 'continent': 'Europe', 'name': 'United Kingdom', 'capital': 'London'}
        ]
        result = get_current_time_in_countries(test_countries)
        self.assertIn('Europe', result)
        self.assertIn('United Kingdom', result['Europe'])
        self.assertIsInstance(result['Europe']['United Kingdom'], str)

    def test_multiple_countries_single_timezone(self):
        test_countries = [
            {'timezones': ['Europe/London'], 'code': 'GB', 'continent': 'Europe', 'name': 'United Kingdom', 'capital': 'London'},
            {'timezones': ['Europe/Paris'], 'code': 'FR', 'continent': 'Europe', 'name': 'France', 'capital': 'Paris'}
        ]
        result = get_current_time_in_countries(test_countries)
        self.assertIn('Europe', result)
        self.assertIn('United Kingdom', result['Europe'])
        self.assertIn('France', result['Europe'])
        self.assertIsInstance(result['Europe']['United Kingdom'], str)
        self.assertIsInstance(result['Europe']['France'], str)

    def test_single_country_multiple_timezones(self):
        test_countries = [
            {'timezones': ['America/New_York', 'America/Los_Angeles'], 'code': 'US', 'continent': 'North America', 'name': 'United States', 'capital': 'Washington, D.C.'}
        ]
        result = get_current_time_in_countries(test_countries)
        self.assertIn('North America', result)
        self.assertIn('United States', result['North America'])
        self.assertIsInstance(result['North America']['United States'], str)


unittest.main(argv=[''], exit=False)
