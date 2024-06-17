import warnings
warnings.filterwarnings('ignore')

from datasets import load_dataset
from pinecone import Pinecone, ServerlessSpec
from tqdm.auto import tqdm
from DLAIUtils import Utils

import ast
import os
import pandas as pd
from openai import OpenAI

# get api key
utils = Utils()
PINECONE_API_KEY = utils.get_pinecone_api_key()

pinecone = Pinecone(api_key=PINECONE_API_KEY)

utils = Utils()
INDEX_NAME = utils.create_dlai_index_name('dl-ai')
if INDEX_NAME in [index.name for index in pinecone.list_indexes()]:
  pinecone.delete_index(INDEX_NAME)

pinecone.create_index(name=INDEX_NAME, dimension=1536, metric='cosine',
  spec=ServerlessSpec(cloud='aws', region='us-west-2'))

index = pinecone.Index(INDEX_NAME)

max_articles_num = 500
df = pd.read_csv('./data/wiki.csv', nrows=max_articles_num)
df_head = df.head()

print(df_head)

