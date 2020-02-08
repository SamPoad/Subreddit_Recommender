"""
This file is designed get the new user's input data, process that input in a similar fashion to
"""


# DEPENDENCIES
import pandas as pd
import numpy as np

# IMPORT THE MODEL

# IMPORT THE MAPPER
from pull import sr_map

# GLOBAL VARIABLES


# DEFINE FUNCTIONS
def build_userdf(sr_list):
    """This function will take the user's inputted list of subreddits and return a single-row dataframe with matching columns"""
    user_df = pd.DataFrame().reindex_like(data)
    # empty this dataframe

    
    # our user dict
    

    print(user_df)
    # user_df.append(sr_list)
    # return user_df

# create the dataframe directly from the dict
# df = pd.DataFrame.from_dict(self, orient = 'index').fillna(0)



# Ask the user's input
def getSubreddits():
    """This function will iterate through requesting 5 Subreddits from the user, 
    and running data validation on each"""

    print("We will be asking you for 5 Subreddits that interest you, in order of preference from greatest to least.")
    preferred_subreddits = [] # create an empty list

    while len(preferred_subreddits) < 5: # while we have less than 5 subreddits entered, keep running

        sr1 = input("Please enter a Subreddit you enjoy\n").lower().strip() # 
        if sr1 in sr_map.values() and sr1 not in preferred_subreddits: # mapper was already lowered
            preferred_subreddits.append(sr1)
        # try:
        #     if sr1 in inv_dict_sub.values():

        # except:
        #     Print("I'm sorry, I don't recognize that Subreddit. Please try again.")

        # preferred_subreddits.append(sr1)
        print(f"You have entered {len(preferred_subreddits)} of 5")
    
    return preferred_subreddits

def assignPreference(sr_list):
    """this function will create a dictionary to assign Preference values to the User's subreddit inputs"""
    val_list = [0.45, 0.35, 0.1, 0.05, 0.05]
    pref = {sr_list[i] : val_list[i] for i in range(len(sr_list))}
    return pref



# new_user = getSubreddits()
new_user = ['007', 'python', 'datascience', '1200isplenty', '100pushups']

print(new_user)
print(assignPreference(new_user))
# print(build_userdf(new_user))

# pass the user's input through the same data "processing" that the model's data was done

