import unittest
import tempfile
from pathlib import Path
from atlas.rag_pipeline import ask_atlas

class TestRagPipeline(unittest.TestCase):
    def test_ask_atlas_valid_search(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'doc.txt').write_text('Atlas uses Python for its backend.')
            
            prompt = ask_atlas (folder, 'Python', 5)
            
            self.assertIn('doc.txt', prompt)
            self.assertIn('Atlas uses Python', prompt)
            self.assertIn('QUESTION: Python', prompt)
            
    def test_ask_atlas_no_results(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'doc.txt').write_text('Atlas uses Python')
            
            prompt = ask_atlas(folder, 'Java', 5)
            
            self.assertEqual(prompt, 'No relevant information found or invalid search parameters.')
            
if __name__ == '__main__':
    unittest.main()