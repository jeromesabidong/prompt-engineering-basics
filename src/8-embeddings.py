from utils import authenticate
credentials, PROJECT_ID = authenticate() # Get credentials and project ID

REGION = 'us-central1'
# Import and initialize the Vertex AI Python SDK

import vertexai
vertexai.init(project = PROJECT_ID, 
              location = REGION, 
              credentials = credentials)

#  ==========================================================

# NOTES
# 
# Converting to embeddings from a model
from vertexai.language_models import TextEmbeddingModel

# specify the embedding model, here it's `textembedding-gecko@001`
embedding_model = TextEmbeddingModel.from_pretrained(
    "textembedding-gecko@001")

# generate embedding for a piece of text
embedding = embedding_model.get_embeddings(
    ["life"])

vector = embedding[0].values
print(f"Length = {len(vector)}")
print(vector[:10])

#  ==========================================================

# NOTES
# 
# Calculating similarity
from sklearn.metrics.pairwise import cosine_similarity
emb_1 = embedding_model.get_embeddings(
    ["What is the meaning of life?"]) # 42!

emb_2 = embedding_model.get_embeddings(
    ["How does one spend their time well on Earth?"])

emb_3 = embedding_model.get_embeddings(
    ["Would you like a salad?"])

vec_1 = [emb_1[0].values] # supposed to be higher compared to other embeddings below
vec_2 = [emb_2[0].values]
vec_3 = [emb_3[0].values]

# NOTES
# 
# Sentence embeddings are better than word embeddings
# Sentence embeddings that have similar thought have close data points in the 
# embedding vector space