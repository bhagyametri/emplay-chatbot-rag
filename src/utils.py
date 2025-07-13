import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

def load_snippets_from_excel(file_path):
    df = pd.read_excel(file_path)
    snippets = df.iloc[:, 0].dropna().astype(str).tolist()
    return snippets

def embed_and_save(snippets, model_name="all-MiniLM-L6-v2", index_path="faiss_index", metadata_path="snippets.pkl"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(snippets, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, index_path)
    with open(metadata_path, "wb") as f:
        pickle.dump(snippets, f)
    print("Embedding & saving complete.")

def load_index(index_path="faiss_index", metadata_path="snippets.pkl"):
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        snippets = pickle.load(f)
    return index, snippets

