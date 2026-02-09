import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

class SemanticSearchEngine:
    def __init__(self, index_path, mapping_path, model_name = 'all-MiniLM-L6-v2'):
        self.index = faiss.read_index(index_path)

        with open(mapping_path, 'r') as f:
            self.metadata = json.load(f)

        self.model = SentenceTransformer(model_name)

    def search(self, query, k = 5):
        query_emb = self.model.encode([query], convert_to_numpy = True)
        query_emb = query_emb/np.linalg.norm(query_emb, axis = 1)

        D, I = self.index.search(query_emb.astype('float32'), k)

        results = []
        for score, idx in zip(D[0], I[0]):
            chunk = self.metadata[idx]
            result = {
                'Text': chunk,
                'Score': float(score)
            }
            results.append(result)

        return results

        