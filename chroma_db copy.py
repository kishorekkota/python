import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")


collection.add(
    documents=["This is a document", "This is another document", "This is some other document", "Kishore K Kota"], 
    metadatas=[{"source": "my_source1"}, {"source": "my_source2"}, {"source": "my_source3"}, {"source": "my_source4"}],
    ids=["id1", "id2", "id3", "id4"]
)


results = collection.query(
    query_texts=["Kisore Kata"],
    n_results=2
)

print(results)
