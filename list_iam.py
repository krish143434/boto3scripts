#Manualsteps to check the IAM Users:
#==================================
#step1: Get AWS MGMT console
#step2: Get IAM console
#    options: Users, Groups, roles
# using resource and client method
#==================================


# import boto3

# aws_mgmt= boto3.session.Session(profile_name="default")
# iam_console= aws_mgmt.resource("iam")

# for each_user in iam_console.users.all():
#     print(each_user.name)

import boto3
aws_mgmt= boto3.session.Session(profile_name="default")
ian_console=aws_mgmt.client('iam')
for each in ian_console.list_users()['Users']:
    print(each['UserName'])
