import unittest
from src.nirvana.coalesce.coalesce import coalesce

class TestCoalesce(unittest.TestCase):
    def test_coalesce(self):
        # Given
        mock_insurance_data = {"data1": {"api1": 1, "api2": 2}, "data2": {"api1": 2, "api2": 3}}
        mock_strategy = lambda data: 10

        # When
        actual = coalesce(mock_insurance_data, mock_strategy)

        # Then
        self.assertEqual(actual, {"data1": 10, "data2": 10})