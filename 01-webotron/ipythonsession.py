# coding: utf-8
import boto3

session = boto3.Session(profile_name='testing')
s3 = session.resource('s3')


for bucket in s3.buckets.all(): print(bucket)

get_ipython().run_line_magic('history', '')
#new_bucket = s3.create_bucket(Bucket='demoautomatingawsrobin-boto3', CreateBucketConfiguration={'LocationConstraint':'us-east-2'})

get_ipython().run_line_magic('history', '')

print(dir(s3))

my_west_resources = boto3.Session(region_name='us-west-2',profile_name='testing')
print(dir(my_west_resources))

bucket = s3.Bucket('testenvglacierbucket')
print(dir(bucket))
for obj in bucket.objects.all(): print(obj.key)
ec2_client = session.client('ec2')
#get_ipython().run_line_magic('save', 'ipythonsession.py 1-46')
