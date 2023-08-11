from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Milvus

class Query():

    def __init__(self):
        self.model_name = "firqaaa/indo-sentence-bert-base"
        self.model = HuggingFaceEmbeddings(model_name=self.model_name)


    def query_data(self, query):
        qry = Milvus(collection_name="legalKan",
             embedding_function=self.model,
             connection_args={"host": "127.0.0.1", "port": "19530"})
        
        search = qry.similarity_search_with_score(query, k=1)
        
        for result in search:
            content = result[0]
            score = result[1]
            
            if score < 500:
                page_content = content.page_content
            else:
                page_content = "Hasil tidak ditemukan. Developer akan segera melakukan pembaruan"

        return page_content