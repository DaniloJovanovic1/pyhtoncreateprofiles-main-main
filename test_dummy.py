import unittest
import csv
import json

class TestControl(unittest.TestCase):
    def test_always_passes(self):
        # ARRANGE → inga data behövs
        # ACT → inga beräkningar
        # ASSERT → går alltid igenom
        self.assertTrue(True)

    #def test_always_fails(self):
        # ARRANGE → inga data behövs
        # ACT → inga beräkningar
        # ASSERT → detta ska faila (kan kommenteras bort efter test)
       # self.assertTrue(False)

class TestCSV(unittest.TestCase):
    def test_csv_should_have_12_columns(self):
        # ARRANGE
        with open("profiles1.csv", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
        # ACT
        column_count = len(headers)
        # ASSERT
        self.assertEqual(column_count, 12)

    def test_csv_should_have_900_plus_rows(self):
        # ARRANGE
        with open("profiles1.csv", newline='', encoding='utf-8') as f:
            rows = list(csv.reader(f))[1:]  # skip header
        # ACT
        row_count = len(rows)
        # ASSERT
        self.assertGreaterEqual(row_count, 900)


class TestJSON(unittest.TestCase):
    def test_json_should_have_900_plus_rows(self):
        # ARRANGE
        with open("web/data.json", encoding='utf-8') as f:
            data = json.load(f)
        # ACT
        row_count = len(data)
        # ASSERT
        self.assertGreaterEqual(row_count, 900)

    def test_json_entries_should_have_12_properties(self):
        # ARRANGE
        with open("web/data.json", encoding='utf-8') as f:
            data = json.load(f)
        sample = data[0]
        # ACT
        property_count = len(sample.keys())
        # ASSERT
        self.assertEqual(property_count, 12)

    def test_json_should_be_a_list(self):
        # ARRANGE
        with open("web/data.json", encoding='utf-8') as f:
            data = json.load(f)
        # ASSERT
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
