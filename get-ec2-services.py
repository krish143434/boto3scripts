import boto3
from pprint import pprint

#to get the state of instance and its subsideries

ec2_con = boto3.client('ec2')
#data to get availabile instance

# response=ec2_con.describe_instances()
# for each in (response.get('Reservations')):
#     for each_item in each['Instances']:
#            print("======================")
#            print("The instance id is: {}\nThe instance image used is: {}\nThe instance Launch time is: {}".format(each_item['InstanceId'],each_item['ImageId'],each_item['LaunchTime'].strftime("%y-%m-%d")))

response=ec2_con.describe_volumes()['Volumes']
for each in response:
    #print(each)
    print("The volume id is: {}\nThe volume state is: {}".format(each['VolumeId'],each['State']))