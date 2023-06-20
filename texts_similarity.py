import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

df = ['An array is a data structure that stores elements in contiguous memory locations, while a linked list stores elements in non-contiguous memory locations connected by pointers.',
    'An array is a contiguous block of memory used to store elements, while a linked list is a collection of nodes that are connected via pointers.',
    'Arrays have a fixed size, while linked lists can dynamically grow or shrink in size.',
    'Accessing an element in an array takes constant time, while accessing an element in a linked list takes linear time.',
    'Inserting or deleting an element in an array requires shifting all subsequent elements, while in a linked list it only requires updating pointers.']

sentences = [sentence.lower()\
             .replace('br','')\
             .replace('<',"")\
             .replace(">","")\
             .replace('\\',"")\
             .replace('\/',"")\
             for sentence in df]

our_sentence = "elements of arrays are stored in contiguous memory cells, while elements of linked lists are stored in different cells but connected with each other by pointers."
#our_sentence = 'Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees ...'

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
