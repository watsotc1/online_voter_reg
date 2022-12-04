from pathlib import Path
import pandas as pd
import pyqrcode
import random
import string
import pyotp
# import png

path = Path("database")

##########################
#Verify User
##########################
def verify(userID,password,otp,totp):
    df=pd.read_csv(path/'voter_list.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    for index, row in df.iterrows():
        if (df['UserID'].iloc[index] == userID) and (df['Password'].iloc[index] == password):
            if otp == totp:
                return True
    return False


##########################
#Verify Eligibility 
##########################
def isEligible(userID):
    df=pd.read_csv(path/'voter_list.csv')
    df=df[['voter_id','Name','Gender','County','State','UserID','Password','hasVoted']]
    for index, row in df.iterrows():
        if df['UserID'].iloc[index]==userID and df['hasVoted'].iloc[index]==0:
            return True
    return False


##########################
#Generate OTP QR Code
##########################
def generate_qr(keyword='base32secret3232'):
    #Generate OTP
    totp = pyotp.TOTP(keyword)
    s = totp.provisioning_uri(name='alice@google.com', issuer_name='Secure Voting System')

    #Make QR Code
    save_path = 'img/' + ''.join(random.choices(string.ascii_lowercase, k=5)) + '.png'
    url = pyqrcode.create(s)
    url.png(save_path, scale = 6)

    #Return OTP
    return totp.now(), save_path