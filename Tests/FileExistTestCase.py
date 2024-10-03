import unittest
import os


class FileExistTestCase(unittest.TestCase):
    def test_file_existence(self):
        path = "../Data Types/Strings/excesses.py"
        self.assertTrue(os.path.exists(path))  # add assertion here

if __name__ == '__main__':
    unittest.main()
