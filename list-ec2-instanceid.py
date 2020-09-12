#lsit all instanceids

import boto3

#aws_mgmt=boto3.session.Session(profile_name="default")

#using client method and resource method

ec2_istanc=boto3.client('ec2')

response = ec2_istanc.describe_instances()

for each in (response['Reservations']):
    for instance in (each['Instances']):
        print(instance['InstanceId'])

#using resource method

ec2_instance=boto3.resource('ec2')
for each in (ec2_instance.instances.all()):
    print (each.image_id)