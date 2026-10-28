import unittest
import tempfile
from pathlib import Path


from atlas.document_loader import discover_documents


class TestDocumentLoader(unittest.TestCase):
    
    def test_existing_folder_with_txt_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / 'first.txt').write_text('Hello')
            (folder / 'second.txt').write_text('World')
            
            result = discover_documents(folder)
            
            self.asserEqual(len(result), 2)
            self.assertTrue(all(path.suffix == ".txt" for path in result))
    def test_empty_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = discover_documents(temp_dir)
            
            self.assertEqual(result, [])
            
    def test_nonexisting_folder(self):
        result = discover_documents(
            Path(tempfile.gettempdir()) / "folder_that_does_not_exist_atlas"
        )
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()