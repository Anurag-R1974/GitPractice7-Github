






import boto3

ent = boto3.client('ec2', region_name='us-east-1')  # You can change region as needed

response = client.run_instances(
   ImageId='ami-00a929b66ed6e0de6',



    InstanceType='t2.nano', #windows user created and changed to nano

    KeyName='USKEY1',
    MinCount=1,
    MaxCount=1
)

print("EC2 Instance launched!")


print(response['Instances'][0]['InstanceId'])
# linux created & changed micro to large
# merged and kept windows changes in linux


