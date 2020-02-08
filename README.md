# Subreddit_Recommender
based on your subreddit usage, which other subreddits might you like? 

####
Dependency item
pip install fuzzywuzzy
pip install python-Levenshtein


Requirements: 
    deliver a recommender system
    use a clustering algorithm somewhere in the process (with too much data)
        would have to 'joblib' save and train the model
    Functional Programming (pipelines)
    implement a custom module
    command line application - argument for number of subreddits (input() function), based on those entries, recommends the subreddits to the user, set a cap on the number of subreddits returned
    error handling so program doesn't crash
    Github Repo

database structure
Username | subreddit | Timestamp of comment
14m Rows
22,610 Users
34,967 subreddit

Reference Material: 
https://towardsdatascience.com/build-your-own-clustering-based-recommendation-engine-in-15-minutes-bdddd591d394
https://www.kaggle.com/supratimhaldar/clustering-movies-with-collaborative-filtering
https://medium.com/analytics-vidhya/k-nearest-neighbors-all-you-need-to-know-1333eb5f0ed0


Process:
Create Github Repo - Ramon
Import the data - 
Exploratory Data Analysis - class balance (distribution), 


Build
Final Product

SQL Script
    import the data to CSV (save the SQL Script for the code review)
         our SQL query was designed to Group by User, count of UTC, 

pull.py - Pipeline Start
    Query the Database, collect 100k rows (only the IDs)
    create a map of subreddit IDs to subreddit Names
    return the DataFrame and the map


clean.py - Pipeline
    get the DataFrame from pull.py
        pipepline to transform the data - 
    return the transformed DataFrame  
        
cluster.py
    import the Transformed DataFrame
    run the selected Clustering Model on it. Evaluate the Model. Pickle that Trained Model
    using "cosine similarity" as distance metric in KNearestNeighbors instead of Euclidean Distance due to high dimensionality, Euclidean distance is often repetitive
    https://medium.com/analytics-vidhya/k-nearest-neighbors-all-you-need-to-know-1333eb5f0ed0 <!-- drop the fuzzy matching from here, but use the rest -->


main.py - our command-line interface, accepting the inputted arguments
    error handling on the inputs
    try/except to import that pickled model from cluster.py <!-- our clustered module -->
    import the inputted arguments from the command line, return the desired number of results





Work still left to complete
install mapper to get ids back
https://www.geeksforgeeks.org/python-ways-to-change-keys-in-dictionary/
on a failed input, run the fuzzy matching to provide options back
on a failed input, let the user know that their input failed


Potential future options
filter out NSFW Reddits from db
weight user's inputs according to preference, and include that in the model's input
test the recommendations with Agglomerative Clustering instead
test the sample proportions from our dataset to make sure it is representative of the population