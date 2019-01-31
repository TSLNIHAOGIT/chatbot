import pandas as pd
df_ori=pd.read_csv('/Users/ozintel/Downloads/Tsl_work_file/Collect_project_file/chatbot/hrx/话术节点_confirm/node_message.csv')
df_new=pd.read_csv('/Users/ozintel/Downloads/Tsl_work_file/Collect_project_file/chatbot/hrx/话术节点_confirm/node_message_lz.csv')

for each in zip(df_ori['message'],df_new['message']):
    if not each[1]==each[0]:
        print(each[0],'\n',each[1])

# each_temp=[]
# for index ,each in enumerate(df['message']):
#     if index%2!=0:
#         each_temp.append(each)
#
#
#     print(each)

# print('a'=='b')