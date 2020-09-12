import boto3
# to get all groups in IAM
iam_con=boto3.client('iam')

response = iam_con.list_groups()
for each_group in response['Groups']:
    #print(each_group['GroupName'])
    print ("GroupName={}\nGroupID={}".format(each_group['GroupName'],each_group['GroupId']))