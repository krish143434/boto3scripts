import boto3
from random import choice
import sys

def password_maker():
    len_of_passwd = 15
    things_tobe_in = "abcdefghijklmnopqrstuvwxyz0987654321ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    random_pass = "".join(choice(things_tobe_in) for i in range(len_of_passwd))
    return random_pass

def session_creation():
    aws_mg=boto3.session.Session(profile_name='default')
    iam_console=aws_mg.client('iam')
    return iam_console

def main():
    iam_con= session_creation()
    User_NAME= 'test@roche.com'
    password=password_maker()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    print("creating your user") 
    try:
        iam_con.create_user(UserName=User_NAME)
    except Exception as e:
        if e.response['Error']['Code']== "EntityAlreadyExists":
            print("The mentioned users already exists: {}".format(User_NAME))
            sys.exit(0)                                                                                                     
        else:                                                                                                               
            print("Please verify the following error and retry")
            print(e)                                                                                                          
            sys.exit(0)
    iam_con.create_login_profile(UserName=User_NAME,Password=password,PasswordResetRequired=False)
    iam_con.attach_user_policy(UserName=User_NAME,PolicyArn=PolicyArn)
    response = iam_con.create_access_key(UserName=User_NAME)                                                        
    print ("IAM User Name={}".format(User_NAME))                                                                         
    print ("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))
    print("IAM users: {}\nIAM_passwd: {}".format(User_NAME,password))
    return None
    
if __name__ == "__main__":
    main()