import pandas as pd
import chromadb

class Portfolio:
    def __init__(self):
        client = chromadb.Client()
        # ✅ Check if collection already exists
        try:
            self.vector_store = client.get_collection("portfolio")
        except:
            self.vector_store = client.create_collection("portfolio")

    def load_portfolio(self, filepath="my_portfolio.csv"):
        self.data = pd.read_csv(filepath)
        self._index_projects()

    def upload_portfolio(self, df):
        self.data = df
        self._index_projects()

    def _index_projects(self):
        for i, row in self.data.iterrows():
            self.vector_store.add(
                documents=[row['Techstack']],
                ids=[str(i)],
                metadatas=[{
                    "title": f"Project {i+1}",
                    "link": row['Links']
                }]
            )
    def load_portfolio(self):
        # You can mock loading here — or skip if not needed
        self.links = [
            "https://github.com/vaibhavgaikwad7/Credibility-Detection-of-Health-Web-Blogs-Using-Explainable-AI",
            "https://github.com/vaibhavgaikwad7/Portfolio-Optimization-Using-Bidirectional-CNN-LSTM-with-Attention-Mechanism",
            "https://github.com/vaibhavgaikwad7/Energy-Consumption-Predictor"
        ]

    def query_links(self, skills):
        query = " ".join(skills)
        results = self.vector_store.query(query_texts=[query], n_results=3)
        if results['metadatas'] and len(results['metadatas']) > 0:
            return [doc['link'] for doc in results['metadatas'][0]]
        return []

        # Always return all 3 links (or you can return based on skills later)
        return self.links
