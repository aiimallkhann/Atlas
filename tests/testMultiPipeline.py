import unittest
import tempfile
from pathlib import Path

from atlas.multipipeline import search_document

class TestMultiPipeline(unittest.TestCase):
    def test_multiple_folders_with_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'first.txt').write_text ('Hello Python')
            (folder / 'second.txt').write_text('Hello World')
            
            result = search_document (folder, 'Hello', 3)
            
            self.assertEqual(len(result), 2)
            self.assertEqual(
                {item['source'] for item in result},
                {'first.txt', 'second.txt'}
            )
            

path = Path(r"D:\New folder\My Works")
if __name__ == '__main__':
    search_document(path, 'hello', 2)