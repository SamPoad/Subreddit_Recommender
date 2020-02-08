"""This file will manage the transformation of the data as well as training the model."""

# IMPORT DEPENDENCIES
from pull import data
from scipy.sparse import csr_matrix

# still need to add in the model training code

# DEFINE FUNCTIONS
def calculate_usage(df):
    """This function assigns a weight to user's subreddit preference based on activity in each subreddit as an average. We calculate
    this activity by how many times a user posted to a specific subreddit, divided by their total posting activity"""
    df['usage'] = 0
    for user in df['username_id'].unique():
        sum_ = df[ df['username_id'] == user]['visits'].sum()
        indices_ = df[ df['username_id'] == user].index
        df['usage'].iloc[indices_] = df['visits'].iloc[indices_] / sum_
    return df

def to_matrix(df):
    # function takes in our usage dataframe and transforms it to a pivot table
    return df.pivot(
        index='subreddit_id',
        columns='username_id',
        values='usage'
    ).fillna(0)


# CALL FUNCTIONS
df_user_usage = to_matrix(calculate_usage(data))
print(df_user_usage.head())
# mat_user_usage = csr_matrix(df_user_usage.values) # compress our matrix
# print(mat_user_usage)