# import os
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import Pinecone
# from langchain.document_loaders import TextLoader
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chat_models import ChatOpenAI
# import pinecone



# loader = TextLoader("data/data.txt")
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# docs = text_splitter.split_documents(documents)

# print(docs[7])

# embeddings = OpenAIEmbeddings()

# pinecone.init(
#     api_key=PINECONE_API_KEY,  # find at app.pinecone.io
#     environment=PINECONE_ENV,  # next to api key in console
# )

# index_name = "langchainbot"
# texts = [d.page_content for d in docs]
# metadatas = [d.metadata for d in docs]

# docsearch = Pinecone.from_texts(
#     texts,
#     embeddings,
#     metadatas,
#     index_name=index_name,
# )
# query = "cybersecurity"
# docs = docsearch.similarity_search(query)