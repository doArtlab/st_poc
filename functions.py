from langchain_community.vectorstores import SupabaseVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from config import Config
from supabase import create_client

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

supabase = create_client(
    Config.supabase_url,
    Config.supabase_key
)

def get_brand_contents_from_query(query: str):
    vectorstore = SupabaseVectorStore(
        client=supabase,
        embedding=embedding,
        table_name="brand_documents",
        query_name="match_brand_documents"
    )
    docs = vectorstore.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]

def get_product_contents_from_query(query: str):
    vectorstore = SupabaseVectorStore(
        client=supabase,
        embedding=embedding,
        table_name="product_combined_documents",
        query_name="match_combined_documents"
    )
    docs = vectorstore.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]

def get_ingredients_from_query(query: str):
    vectorstore = SupabaseVectorStore(
        client=supabase,
        embedding=embedding,
        table_name="product_ingredient_documents",
        query_name="match_ingredient_documents"
    )
    docs = vectorstore.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]

def get_customer_sales_from_query(query: str):
    vectorstore = SupabaseVectorStore(
        client=supabase,
        embedding=embedding,
        table_name="customers",
        query_name="match_customers"
    )
    docs = vectorstore.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]