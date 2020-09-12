#!/usr/bin/python

# Python script to update new stacknames in environment json file
# Example run command "python main.py navify dev106"
# used to insert tags as sent by positinal parameters
import boto3
import sys
import json

s3_obj =boto3.client('s3')


s3_clientobj = s3_obj.get_object(Bucket='mybucketname', Key='images_ecr.json')
s3_obj.download_file('mybucketname', 'images_ecr.json', 'images_ecr.json')
s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')

print("printing s3_clientdata")
print(s3_clientdata)
environment=sys.argv[1]
imagetag=sys.argv[2]
servicename=sys.argv[3]

with open('images_ecr.json', 'r+') as f:
    data_dict = json.load(f)
    for key in data_dict:
        if key == environment:
            if imagetag in data_dict[environment][servicename]:
                print ("{0} image alredy exists in this {1} repo".format(imagetag, servicename))
                sys.exit()
            else:
                data_dict[environment][servicename].append(imagetag)
                print ("Added new image {0} into {1} repo".format(imagetag, servicename))
                print (json.dumps(data_dict, indent=4))
                f.seek(0)
                json.dump(data_dict, f, indent=4)
                f.truncate()

# Uploads the new file to S3 bucket if new stack added to environment
s3_obj.upload_file(Bucket ='ow-bitbucket-url', Filename='images_ecr.json', Key='images_ecr.json', ExtraArgs={'ACL': 'public-read'} )

# #aws s3api put-object-acl --bucket ow-bitbucket-url --key dev-test.json --acl public-read
