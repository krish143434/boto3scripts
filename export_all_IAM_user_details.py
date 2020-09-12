import boto3
import csv
#script to pull all IAM users to CSV

aws_mag_con=boto3.session.Session(profile_name="default")
iam_con_re=aws_mag_con.client(service_name="iam",region_name="us-west-2")
cnt=1
csv_ob=open("iam_data.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","IAM User Name",'User Id','User ARN','User Creation Date'])
for each in iam_con_re.list_users()['Users']:
    print(cnt,each['UserName'],each['UserId'],each['Arn'],each['CreateDate'].strftime("%Y-%m-%d"))
    csv_w.writerow([cnt,each['UserName'],each['UserId'],each['Arn'],each['CreateDate'].strftime("%Y-%m-%d")])
    cnt+=1
csv_ob.close()