import unittest

from sample_project import calculate_total, normalize_name


class TestSampleProject(unittest.TestCase):
    def test_normalize_name(self):
        self.assertEqual(normalize_name("  jane   doe "), "Jane Doe")

    def test_normalize_name_rejects_empty(self):
        with self.assertRaises(ValueError):
            normalize_name("   ")

    def test_calculate_total(self):
        self.assertAlmostEqual(calculate_total([10, 20], 0.10), 33)

    def test_calculate_total_rejects_negative_tax(self):
        with self.assertRaises(ValueError):
            calculate_total([10], -0.1)


if __name__ == "__main__":
    unittest.main()
