import boto3
#using filters to get required informations
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")
filter1={"Name": "instance-state-name", "Values":['running','stopped']}
filter2={"Name":"instance-type","Values":['t2.micro']}
for each in ec2_con_re.instances.filter(Filters=[filter1,filter2]):
	print(each)