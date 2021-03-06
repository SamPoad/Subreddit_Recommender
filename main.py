"""
This file is the main python file, designed to import the pickled clustering system,
get the new user's input data, process that input and predict the cluster to recommend subreddits
"""


# DEPENDENCIES
import pandas as pd
import numpy as np
# import joblib # for the pickled clustering model
from fuzzywuzzy import fuzz
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


# IMPORT THE PIPELINE'S FUNCTIONS
from askuser import new_user # SyntaxError: trailing comma not allowed without surrounding parentheses ?
from askuser import assignPreference
from askuser import fuzzy_matching
from transformetl import df_user_usage, mat_user_usage
from pull import sr_map


# GLOBAL VARIABLES


# DEFINE FUNCTIONS

     
#Creating dictionary for subreddits
def create_Dict_Mapper(key_series, value_series):
    dict_subreddits = key_series
    dict_subreddits.index = value_series
    dict_subreddits = dict_subreddits.to_dict()
#     inv_dict_sub = {v: k for k, v in dict_subreddits.items()}
    return dict_subreddits

def make_recommendation(data, mapper, model, subreddit, n_recommendations = 5):
    
    # fit
#     model.fit(data)
    
    # get input movie index
    print('You have input subreddit:', subreddit)
    
    idx = fuzzy_matching(
        mapper,
        subreddit
    )

    print('Recommendation system start to make inference')
    print('......\n')
    
    print(idx)

    distances, indices = model.kneighbors(
        data.query(f"subreddit_id == [{idx}]"), #data.loc[data['username_id']==idx,],
        n_neighbors=n_recommendations+1
    )
    
    # get list of raw idx of recommendations
    
    raw_recommends = sorted(
        list(
            zip(
                indices.squeeze().tolist(),
                distances.squeeze().tolist()
            )
        ),
        key=lambda x: x[1]
    )[:0:-1]
    
    # get reverse mapper
    reverse_mapper = {v: k for k, v in mapper.items()}
    
    # print recommendations
    print(f"Recommendations for {subreddit}:")
    print(raw_recommends)

    # uncomment me!    
    # for i, (idx, dist) in enumerate(raw_recommends):
        
    #     print(f"{i+1}: {reverse_mapper[idx]}, with distance of {dist}")

# BUILD THE MODEL


category_num_mapper = create_Dict_Mapper(sr_map['subreddit_id_mapper'], sr_map['subreddit'])


# Initialize the Model
model_knn = NearestNeighbors(n_neighbors=25) #metric='cosine', algorithm='brute', , n_jobs=-1

# fit the dataset
model_knn.fit(df_user_usage)


for user_selection in new_user:
    make_recommendation(
        model = model_knn,
        data = df_user_usage,
        subreddit = user_selection,
        mapper = category_num_mapper,
        n_recommendations=5
        )

# pass the user's input through the same data "processing" that the model's data was done

