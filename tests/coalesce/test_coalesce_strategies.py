import unittest
from src.nirvana.coalesce.coalesce_strategies import coalesce_weighted_mean, coalesce_mean_ignore_api1

class TestCoalesceStrategies(unittest.TestCase):
    def test_coalesce_weighted_mean(self):
        # Given
        mock_insurance_data =  {"api1": 20, "api2": 40, "api3": 25}

        # When
        actual = coalesce_weighted_mean(mock_insurance_data)

        # Then
        self.assertEqual(actual, 9)
    
    def coalesce_mean_ignore_api1(self):
        # Given
        mock_insurance_data =  {"api1": 20, "api2": 40, "api3": 20}

        # When
        actual = coalesce_mean_ignore_api1(mock_insurance_data)

        # Then
        self.assertEqual(actual, 30)
    