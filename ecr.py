#!/usr/bin/python3

import boto3
import sys
import json
#updating json file with ecr image tags for each repo
environment=sys.argv[1]
servicename=sys.argv[2]
accountid=sys.argv[3]

s3_obj =boto3.client('s3')
s3_clientobj = s3_obj.get_object(Bucket='Bucketname', Key='images_ecr.json')
s3_obj.download_file('Bucketname', 'images_ecr.json', 'images_ecr.json')
s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
ecr_obj=boto3.client('ecr')
response = ecr_obj.list_images(
    registryId=accountid,
    repositoryName=servicename,
    filter={
        'tagStatus': 'TAGGED'
    }
)

imageid=[]

for tags in response['imageIds']:
    imageid.append(tags['imageTag'])

with open('images_ecr.json', 'r+') as f:
    data_dict = json.load(f)
    for key in data_dict:
        if key == environment:
            data_dict[environment][servicename].clear()
            for i in imageid:
                if i not in  data_dict[environment][servicename]:
                    data_dict[environment][servicename].append(i)                
                    print (json.dumps(data_dict, indent=4))
                    f.seek(0)
                    json.dump(data_dict, f, indent=4)
                    f.truncate()

# Uploads the new file to S3 bucket
s3_obj.upload_file(Bucket ='bucketname', Filename='images_ecr.json', Key='images_ecr.json', ExtraArgs={'ACL': 'public-read'} )

