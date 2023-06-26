import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(text, answers):
    sentences = [sentence.lower()\
                .replace('br','')\
                .replace('<',"")\
                .replace(">","")\
                .replace('\\',"")\
                .replace('\/',"")\
                for sentence in answers]
    my_embedding = model.encode(text)
    embeddings = model.encode(sentences)

    cos_sim = util.cos_sim(my_embedding, embeddings)

    winners = []
    for arr in cos_sim:
        for i, each_val in enumerate(arr):
            winners.append([sentences[i],each_val])

    final_winners = sorted(winners, key=lambda x: x[1], reverse=True)

    return final_winners[0][1].item()