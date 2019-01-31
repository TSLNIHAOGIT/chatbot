import pandas as pd
import re
df=pd.read_excel('/Users/ozintel/Downloads/Tsl_work_file/Collect_project_file/chatbot/话术节点/huashu_2018_6_28.xls')
column_name=df.columns[3:]
all_colunmn_content=[]
for each in column_name:
    # each_column_content = []
    m=re.search('\d{2}',each).group()
    # print(m)
    if m in ['01','04','07','10']:
        levels='1'
    elif m in ['02','05','08','11']:
        levels = '2'
    elif m in ['03','06','09','12']:
        levels = '3'
    else:
        levels=''

    if m in ['01','02','03']:
        name='与债务人核资并询问未还款原因时，债务人不承认欠款'
        node='cf_s1_n2_confirmLoan_q'
    elif m in ['04', '05', '06']:
        name='询问债务人还款意愿，能否在规定时间还款 ，债务人不能在规定时间还款'
        node='cf_s1_n15_verifyWill_q'
    elif m in ['07','08','09']:
        name='询问债务人将利息减免后，能否在规定时间还款 ，债务人不能在规定时间还款'
        node='cf_s1_n25_cutDebt_q'
    elif m in ['10','11','12']:
        name='询问债务人如果让其分期，能否在规定时间还款，债务人不能在规定时间还款'
        node='cf_s1_n32_splitDebt_q'
    elif m=='13':
        name='询问接听人是不是债务人本人的话术'
        node='cf_s1_n1_identity_q'
    elif m=='14':
        name='询问接听人是否认识债务人本人的话术'
        node='cf_s1_n5_ifAcquainted_q'
    elif m=='15':
        name='催收员打电话催款时，接听人不认识认识债务人本人时'
        node='cf_s1_n102_ifAcquainted_s'
    elif m=='16':
        name='催收员打电话催款时，接听人不是本人但其认识债务人时'
        node='cf_s1_n101_ifAcquainted_s'
    elif m=='17':
        name='催收员打电话催款时，债务人答应还款,告诉支付途径'
        node=''
    else:
        name='催收员打电话催款，未与债务人达成一致时'
        node=''



    # print(df[[each]])
    df['level']=levels
    df['name']=name
    df['node']=node
    a=df[['node','name',each,'level']]
    all_colunmn_content.append(a.rename(columns={each: 'text'}))
    # print(text)
# print('all_colunmn_content',all_colunmn_content)
df_concat=pd.concat(all_colunmn_content)
df_concat.to_excel('huashu_structure.xls')
print(df_concat)


