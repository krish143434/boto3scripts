#list all s3 buckets

# import boto3

# aws_mgmt_console= boto3.session.Session(profile_name="default")
# s3_con= aws_mgmt_console.resource("s3")

# for each_bucket in s3_con.buckets.all():
#     print(each_bucket.name)

import boto3
aws_mgmt= boto3.session.Session(profile_name="default")
iam_console=aws_mgmt.client('s3')
for each in iam_console.list_buckets()['Buckets']:
    print(each['Name'])