import logging
import boto3
import sys
import json
import admin

logger = admin.setup_logging()

class Service(object):
       
    def __init__(self, config):
      pass
        #self.name = config['name']
    

    def ansible_cookbook():
      pass
    def deploy(self):
        #source a deploy event, then get orchestrator to orchestrate the stuff
        client = boto3.client('ec2')

        ami_id = 'ami-6869aa05'
        VpcId = 'vpc-d8fdadbf'
        subnet_id = 'subnet-fdd44d8a'

        result = client.run_instances(ImageId=ami_id, MinCount=1, MaxCount=1, InstanceType='t2.small',SubnetId=subnet_id)

        instance_id = result['Instances'][0]['InstanceId']
        logging.info('launching instance %s' %instance_id)
        waiter = client.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id,])


