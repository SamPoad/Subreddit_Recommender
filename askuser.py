"""
This file is designed get the new user's input data, process that input in a similar fashion to
"""


# DEPENDENCIES
import pandas as pd
import numpy as np

# IMPORT THE MODEL

# IMPORT THE MAPPER
from pull import sr_map
# from transformetl import df_user_usage

# GLOBAL VARIABLES


# DEFINE FUNCTIONS
def build_emptydf(df_cols_we_need):
    """This function will take the user's inputted list of subreddits and return a single-row dataframe with matching columns"""
    user_df = pd.DataFrame().reindex_like(df_cols_we_need) # copy the structure of our final data format
    user_df = user_df[0:0] # empty this dataframe
    return user_df


# Ask the user's input
def getSubreddits():
    """This function will iterate through requesting 5 Subreddits from the user, 
    and running data validation on each"""

    print("We will be asking you for 5 Subreddits that interest you, in order of preference from greatest to least.")
    preferred_subreddits = [] # create an empty list

    while len(preferred_subreddits) < 5: # while we have less than 5 subreddits entered, keep running

        sr1 = input("Please enter a Subreddit you enjoy\n").lower().strip() # 
        potential_subreddits = sr_map['subreddit'].to_list()
        if sr1 in potential_subreddits and sr1 not in preferred_subreddits: # mapper was already lowered
            preferred_subreddits.append(sr1)

        print(f"You have entered {len(preferred_subreddits)} of 5")
    
    return preferred_subreddits

def assignPreference(sr_list):
    """this function will create a dictionary to assign Preference values to the User's subreddit inputs"""
    # user_input_ids = [sr_map['subreddit_id_mapper'][i] for i in sr_list]
    # user_input_ids = [i for i in sr_list]
    # print(user_input_ids)
    val_list = [0.45, 0.35, 0.1, 0.05, 0.05] # confirmed adds up to 1
    pref = {sr_list[i] : val_list[i] for i in range(len(sr_list))}
    # pref = {sr_map['subreddit'][i] : val_list[i] for i in range(len(sr_list))}
    # pref = {sr_map['subreddit'][i] : val_list[i] for i in range(len(sr_list))}
    # pref = {sr_map['subreddit'][i] : val_list[i] for i in sr_list}
    # print([sr_map[ sr_map['subreddit'] == i]['subreddit_id_mapper'] for i in sr_list])
    # pref = {}
    # list2 = []
    # print(sr_list)
    # for i in sr_list:
    #     for values in sr_map['subreddit']:
    #         if i in values:
    #             list2.append(i)
    # print(list2)
    # pref[sr_map[ sr_map['subreddit'] == i]['subreddit_id_mapper']] = val_list[[i]]
    # pref = { sr_map[ sr_map['subreddit'] == i]['subreddit_id_mapper'] : val_list[i] for i in sr_list }
    # overwrite the user_dictionary's subreddit names with subreddit ids 
    # so that when we turn that back into a df, it has the subreddit ids like our data
    # print(pref)
    return pref



    # access the mapper and convert the KEYS into subreddit_ids to be used later
    # init_list = []
    # list_keys = pref.keys()
    # for i in list_keys:
    #     init_list.append(np.where(sr_map['subreddit'] == i, # conditional
    #     sr_map['subreddit_id_mapper'], # return if True
    #     0, # return if False
    #     ))
    # print(init_list)

    # for i in pref.keys():
    #     print((sr_map.loc[sr_map['subreddit'] == i,'subreddit_id_mapper']))
    



    # ini_list = [m]
    # final_dict = dict(
    #     zip(
    #         ini_list, # the list of subreddit ids we want to use to overwrite our Keys
    #         list(ini_dict.values()
    #         ))) 

    # return pref



# replace the KEYS from dict from assignPreference with the subredditid
# dictionary back to mapper to get subreddit ids,
# then add a row to the df with the new user's preference for each matching subredditid column in user_df


# new_user = ['100DaysofKeto', 'python', 'datascience', '1200isplenty', '100pushups']

# new_user = ['pcgaming', 'Spartacus_TV', 'vmware', 'trashy', 'gifsthatendtoosoon']
new_user = getSubreddits()
# assignPreference(new_user)
# print(assignPreference(new_user))
# build_emptydf(df_user_usage)






# Pandas Update column with Dictionary values matching dataframe Index as Keys
# df.birth_Month.update(pd.Series(dictionary_values))
# how to apply this across multiple columns? 