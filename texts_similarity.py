import pandas as pd
from sentence_transformers import SentenceTransformer, util
from database import get_database
import string

model = SentenceTransformer('all-MiniLM-L6-v2')

df = []

cursor = get_database(id=8)
for i in cursor[2:]:
    df.append(i)

print("This is my question:\n", cursor[1])

sentences = [sentence.lower().translate(str.maketrans('', '', string.punctuation))
              for sentence in df]

our_sentence = "elements of arrays are stored in contiguous memory cells, while elements of linked lists are stored in different cells, but connected with each other by pointers."
print("This is your answer\n", our_sentence)

our_sentence = our_sentence.lower().translate(str.maketrans('','',string.punctuation))


my_embedding = model.encode(our_sentence)

embeddings = model.encode(sentences)

cos_sim = util.cos_sim(my_embedding, embeddings)

winners = []
for arr in cos_sim:
    for i, each_val in enumerate(arr):
        winners.append([sentences[i],each_val])

final_winners = sorted(winners, key=lambda x: x[1], reverse=True)

print("The best score ", final_winners[0][1])

# for arr in final_winners[0:2]:
#     print(f'\nScore : \n\n  {arr[1]}')
#     print(f'\nSentence : \n\n {arr[0]}')
