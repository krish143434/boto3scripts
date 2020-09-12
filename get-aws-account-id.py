import boto3

#aws_mgmt_con = boto3.session.Session(profile_name="default")
sts_con = boto3.client('sts')

response = sts_con.get_caller_identity()
print(response['Account'])