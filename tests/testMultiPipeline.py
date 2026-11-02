
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
            self.assertEqual(
                {item['source'] for item in result},
                {'first.txt', 'second.txt'}
            )
            self.assertTrue(
                all("score" in item and "chunk" in item for item in result)
            )

    def test_invalid_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            invalid_folder = Path(temp_dir) / "does_not_exist"

            result = search_document(invalid_folder, "hello", 1)

            self.assertIsNone(result)
    def test_empty_query (self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'fisrt.txt').write_text('Hello Python')
            
            result = search_document(folder, "", 3)
            
            self.assertEqual(result, [])
            
    def test_whitespace_query(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            # Create a basic file so the folder isn't empty
            (folder / 'first.txt').write_text('Hello Python')
            
            # Pass a query containing only spaces
            result = search_document(folder, "   ", 3)
            
            # The regex \b\w+\b should find zero words, returning an empty list
            self.assertEqual(result, [])
            

if __name__ == "__main__":
    unittest.main()
