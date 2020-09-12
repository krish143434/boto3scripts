#!/usr/bin/python3
import boto3
import os
import sys
import json

Aws=boto3.session.Session()
EC2=boto3.client('ec2',region_name='ap-south-1')
response=EC2.describe_security_groups()
sg_group_name=os.environ.get('GROUP_NAME')
sg_group_id=os.environ.get('GROUP_ID')

# Expected_Rules=[{'FromPort': 80, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '172.16.0.1/32', 'Description': 'rule3'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 80, 'UserIdGroupPairs': []}, {'FromPort': 0, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '192.168.1.0/32', 'Description': 'rule1'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 65535, 'UserIdGroupPairs': []}, {'FromPort': 22, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/32', 'Description': 'rule2'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 22, 'UserIdGroupPairs': []}, {'FromPort': 0, 'IpProtocol': 'udp', 'IpRanges': [{'CidrIp': '2.2.2.2/32', 'Description': 'rule5'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 65535, 'UserIdGroupPairs': []}]
# with open("rules", "w") as f:
#     json.dump(Expected_Rules, f)

with open('rules') as f:
    Expected_Rules = json.load(f)

# Getting current inbound rules of security group "Test_SG"
Current_Rules=[]
for i in response['SecurityGroups']:
       if i['GroupName'] == sg_group_name :
           for j in i['IpPermissions']:
               Current_Rules.append(j)

# Comparing Current rules with Expected rules.
try:
    if Expected_Rules == Current_Rules :
        print("Rules are identical")
    else :
        print("Rules are not identical")
        for i in Current_Rules:
            # Removing all in bound rules
            data=EC2.revoke_security_group_ingress(
            GroupId=sg_group_id,
            IpPermissions=[i]
            )
        print("Updating correct rules")
        for i in Expected_Rules:
            # adding all expected rules
            data=EC2.authorize_security_group_ingress(
                GroupId=sg_group_id,
                IpPermissions=[i]
                )
# throw error or exception, whatever comes first
except Exception as e:
    sys.exit(e)


