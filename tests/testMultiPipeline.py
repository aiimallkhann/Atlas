
import unittest
import tempfile
from pathlib import Path

from atlas.multipipeline import search_document


class TestMultiPipeline(unittest.TestCase):
    def test_multiple_folders_with_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "first.txt").write_text("Hello Python")
            (folder / "second.txt").write_text("Hello World")

            result = search_document(folder, "Hello", 3)

            self.assertIsNotNone(result)
            self.assertTrue(result)
            self.assertEqual(len(result), 2)

    def test_invalid_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            invalid_folder = Path(temp_dir) / "does_not_exist"

            result = search_document(invalid_folder, "hello", 1)

            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
