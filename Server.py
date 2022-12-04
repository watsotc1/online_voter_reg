from utils import *
from Security import *
import socket
import threading

lock = threading.Lock()

def client_thread(connection):

    #Receiving voter details 
    data = connection.recv(1024)

    #Verify voter details
    log = (data.decode()).split(' ')
    userID = log[0]
    password = log[1]
    otp = log[2]
    totp = log[3]
    
    #Authenticate
    if(verify(userID,password,otp,totp)):                                
        if(isEligible(userID)):
            print('Voter Logged in... ID:' + str(userID))
            connection.send('Authenticate'.encode())
        else:
            print('Vote Already Cast by ID:' + str(userID))
            connection.send('VoteCasted'.encode())
    else:
        print('Invalid Voter')
        connection.send('InvalidVoter'.encode())


    #Get Vote
    data = connection.recv(1024)                                   
    print('Vote Received from ID: ' + str(userID) + '  Processing...')
    lock.acquire()

    #Update Database
    if(vote_update(data.decode(),userID)):
        print('Vote Casted Successfully by voter ID = ' + str(userID))
        connection.send('Successful'.encode())
    else:
        print('Vote Update Failed by voter ID = ' + str(userID))
        connection.send('Vote Update Failed'.encode())

    lock.release()
    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print('Waiting for the connection')

    serversocket.listen(10)

    print( 'Listening on ' + str(host) + ':' + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send('Connection Established'.encode())   ### 1
        t = threading.Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
