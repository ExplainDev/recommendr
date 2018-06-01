import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import json

with open("programs.example.json") as json_file:
  data = json.load(json_file)

metadata = pd.DataFrame(data=data['programs'])

# Create the tfidf vectorizer object
tfidf = TfidfVectorizer(stop_words='english')

metadata['shortDescription'] = metadata['shortDescription'].fillna('')

tfidf_matrix = tfidf.fit_transform(metadata['shortDescription'])

# Using cosine similarity between descriptions.
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(metadata.index, index=metadata['cliName']).\
    drop_duplicates()


def get_recommendations(cliName, cosine_sim=cosine_sim, k=None):
    # Get the index of the program that matches the cliName
    idx = indices[cliName]
    
    # If the Index object is iterable, it means there is ambiguity because of same program name.
    # Curently, we are choosing one and moving ahead, but this will be changed in future.
    if hasattr(idx, '__iter__'):
        z = [x for x in idx]
        idx = z[1]

    # Get the pairwsie similarity scores of all programs with that program
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the programs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the k or 5 most similar programs
    sim_scores = sim_scores[1:k] if k else sim_scores[1:6]

    # Get the program indices
    program_indices = [i[0] for i in sim_scores]

    # import pdb; pdb.set_trace()

    # Return the top k or 5 most similar programs
    names = metadata['cliName'].iloc[program_indices].tolist()
    description = metadata['shortDescription'].iloc[program_indices].tolist()
    recs = {}

    for x, y in zip(names, description):
        recs[x] = y

    return recs
