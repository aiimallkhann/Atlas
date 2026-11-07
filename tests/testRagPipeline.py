import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from atlas.rag_pipeline import ask_atlas


def fake_embedding(text):
    vec = [0.0] * 8
    for word in text.lower().split():
        vec[sum(map(ord, word.strip('.,!?'))) % 8] += 1.0
    return vec


class TestRagPipeline(unittest.TestCase):
    @patch('atlas.multipipeline.get_embedding', side_effect=fake_embedding)
    def test_ask_atlas_valid_search(self, _mock):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'doc.txt').write_text('Atlas uses Python for its backend.')

            prompt = ask_atlas(folder, 'Python', 5)

            self.assertIn('doc.txt', prompt)
            self.assertIn('Atlas uses Python', prompt)
            self.assertIn('QUESTION: Python', prompt)

    @patch('atlas.multipipeline.get_embedding', return_value=[])
    def test_ask_atlas_no_results(self, _mock):
        # Vector search always returns the nearest chunks, so "no results"
        # now means the embedding step failed (e.g. Ollama is down).
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'doc.txt').write_text('Atlas uses Python')

            prompt = ask_atlas(folder, 'Java', 5)

            self.assertEqual(prompt, 'No relevant information found or invalid search parameters.')


if __name__ == '__main__':
    unittest.main()