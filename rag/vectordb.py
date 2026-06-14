class DummyDB:
    def similarity_search(self, query, k=3):
        return []

def get_vector_db():
    return DummyDB()