import unittest
import tempfile
from pathlib import Path
from atlas.pipeline import search_document

class TestPipeline(unittest.TestCase):
    def test_missing_file(self):
        result = search_document('does not exist.txt', 'hello', 5)
        self.assertIsNone(result)

    def test_valid_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / 'sample.txt'
            path.write_text('love gives life meaning', encoding='utf-8')
            
            result = search_document(path, 'love', 2)
            
            self.assertEqual(result['source'], 'sample.txt')
            self.assertEqual(result['statistics']['Number Of Words'], 4)
            self.assertTrue(result["results"])
    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "empty.txt"
            path.write_text("", encoding="utf-8")

            result = search_document(path, "hello", 5)

            self.assertEqual(result["statistics"]["length"], 0)
            self.assertEqual(result["statistics"]["Number Of Words"], 0)
            self.assertEqual(result["results"], [])
            self.assertEqual(result["source"], "empty.txt")
    def test_invalid_chunk_size(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.txt"
            path.write_text("hello world", encoding="utf-8")

            with self.assertRaises(ValueError):
                search_document(path, "hello", 0)
    def test_search_ranking(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.txt"
            path.write_text(
                "love gives meaning to life. love is powerful.",
                encoding="utf-8"
            )

            result = search_document(path, "love meaning", 5)
            scores = [score for score, chunk in result["results"]]

            self.assertGreaterEqual(scores[0], scores[-1])
            self.assertEqual(scores[0], 2)

if __name__ == '__main__':
    unittest.main()