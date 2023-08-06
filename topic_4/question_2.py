import unittest
import statistics

from typing import List

def calculate_statistics(data: List[float]) -> dict:
    """
    Calculate mean, median, and standard deviation of numerical data.

    Args:
        data (list[float]): List of numerical data.

    Returns:
        dict: A dictionary containing calculated mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("Input data cannot be empty")

    mean = sum(data) / len(data)
    median = statistics.median(data)

    # Calculate standard deviation only if there are at least two data points
    if len(data) >= 2:
        std_dev = statistics.stdev(data)
    else:
        std_dev = 0

    result = {"mean": mean, "median": median, "std_dev": std_dev}

    return result


class TestStatisticsCalculation(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element(self):
        result = calculate_statistics([5])
        self.assertEqual(result["mean"], 5)
        self.assertEqual(result["median"], 5)
        self.assertEqual(result["std_dev"], 0)

    def test_even_number_of_elements(self):
        data = [10, 20, 30, 40]
        result = calculate_statistics(data)
        self.assertEqual(result["mean"], 25)
        self.assertEqual(result["median"], 25)
        self.assertAlmostEqual(result["std_dev"], 12.91, places=2)

    def test_odd_number_of_elements(self):
        data = [15, 25, 35, 45, 55]
        result = calculate_statistics(data)
        self.assertEqual(result["mean"], 35)
        self.assertEqual(result["median"], 35)
        self.assertAlmostEqual(result["std_dev"], 15.8113, places=2)


if __name__ == "__main__":
    unittest.main()