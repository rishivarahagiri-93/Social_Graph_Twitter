# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:10:15 2019

@author: Rishi
"""

import pandas as pd
import re

df = pd.read_csv('AsianMen_User.csv')
                     
Edge_Tweet = (df[df['Tweet'].str.contains("@")])

No_of_Rows = (Edge_Tweet.shape[0])

H1 = (Edge_Tweet['Handle'].str.replace('(',''))

H2 = (H1.str.replace(')',''))

H3 = (H2.str.replace(',',''))

Match_List = pd.DataFrame()

user = []

match_list = []

for i in range(0,No_of_Rows):
    match = re.findall(r'\@\w+', Edge_Tweet['Tweet'].iloc[i])
    user.append(H3.iloc[i])
    match_list.append(match)

Match_List['User'] = user

Match_List['Edge'] = match_list

df_new = Match_List.groupby('User').Edge.apply(lambda x: pd.DataFrame(x.values[0])).reset_index().drop('level_1', axis = 1)

df_new.columns = ['User','Edge']

df_new.to_excel('AsianMen_User.xlsx', sheet_name= 'EdgeList',index = False)
    


