import unittest
from atlas.generator import build_prompt

class TestGenerator(unittest.TestCase):
    def test_build_prompt_formatting(self):
        mock_results = [{'chunk' : 'Test data.', 'source' : 'test.txt'}]
        query = 'Who is this?'
        
        prompt = build_prompt(query, mock_results)
        
        self.assertIn('Test data.', prompt)
        self.assertIn('test.txt', prompt)
        self.assertIn('Who is this?', prompt)
        self.assertIn('context below', prompt)
        
    if __name__ == '__main__':
        unittest.main()