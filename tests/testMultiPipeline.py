import unittest
from atlas.search import cosine_similarity, search_vectors


class TestSearch(unittest.TestCase):
    def test_returns_top_k_sorted(self):
        # Regression test: search_vectors used to return after scoring
        # only the first chunk because sort/return were inside the loop.
        data = [
            ('far', [0.0, 1.0]),
            ('exact', [1.0, 0.0]),
            ('close', [1.0, 1.0]),
        ]
        results = search_vectors([1.0, 0.0], data, top_k=2)

        self.assertEqual(len(results), 2)
        self.assertEqual([r['chunk'] for r in results], ['exact', 'close'])
        self.assertEqual([r['index'] for r in results], [1, 2])
        self.assertGreater(results[0]['score'], results[1]['score'])

    def test_skips_empty_vectors_and_keeps_original_index(self):
        data = [('bad', []), ('good', [1.0, 0.0])]
        results = search_vectors([1.0, 0.0], data, top_k=5)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['chunk'], 'good')
        self.assertEqual(results[0]['index'], 1)

    def test_zero_vector_scores_zero(self):
        self.assertEqual(cosine_similarity([0, 0], [1, 1]), 0.0)


if __name__ == '__main__':
    unittest.main()