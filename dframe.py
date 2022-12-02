import pandas as pd
from pathlib import Path

# path = Path("C:/Users/Desktop/Sem-5/CS301 CN/Project/Voting/database")
path = Path("database")

def count_reset():
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    for index, row in df.iterrows():
        df['hasVoted'].iloc[index]=0
    df.to_csv(path/'voterList.csv')

    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Party','Name','Vote Count']]
    for index, row in df.iterrows():
        df['Vote Count'].iloc[index]=0
    df.to_csv (path/'cand_list.csv')


def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id','Name','Gender','County','State','UserID','Password','hasVoted'])
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    df.to_csv(path/'voterList.csv')

def reset_cand_list():
    df = pd.DataFrame(columns=['Party','Name','Vote Count'])
    df=df[['Party','Name','Vote Count']]
    df.to_csv(path/'cand_list.csv')


def verify(userID,password):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    for index, row in df.iterrows():
        if df['UserID'].iloc[index]==userID and df['Password'].iloc[index]==password:
            return True
    return False


def isEligible(userID):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    for index, row in df.iterrows():
        if df['UserID'].iloc[index]==userID and df['hasVoted'].iloc[index]==0:
            return True
    return False


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'cand_list.csv')
        df=df[['Party','Name','Vote Count']]
        for index, row in df.iterrows():
            if df['Party'].iloc[index]==st:
                df['Vote Count'].iloc[index]+=1

        df.to_csv (path/'cand_list.csv')

        df=pd.read_csv(path/'voterList.csv')
        df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
        for index, row in df.iterrows():
            if df['voter_id'].iloc[index]==vid:
                df['hasVoted'].iloc[index]=1

        df.to_csv(path/'voterList.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Party','Name','Vote Count']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Party'].iloc[index]] = df['Vote Count'].iloc[index]
    # print(v_cnt)
    return v_cnt


def taking_data_voter(name,gender,county,state,userID,password):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "County":[county],
                    "State":[state],
                    "UserID":[userID],
                    "Password":[password],
                    "hasVoted":[0]},)
    else:
        vid=df['voter_id'].iloc[-1]+1
        df1 = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "County":[county],
                    "State":[state],
                    "UserID":[userID],
                    "Password":[password],
                    "hasVoted":[0]},)

        df=df.append(df1,ignore_index=True)

    df.to_csv(path/'voterList.csv')

    return vid
