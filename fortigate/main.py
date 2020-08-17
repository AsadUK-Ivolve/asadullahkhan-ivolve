from bean import *
import json
import subprocess
import yaml
from keystoneauth1 import loading
from keystoneauth1 import session
#from cinderclient import client
#from heatclient.client import Client
from utils import *
from neutronclient.v2_0 import client
from credentials import get_credentials


with open('machine.json') as f:
  distros_dict = json.load(f)


loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url="http://10.81.1.100:5000/v3",
                                 username="admin",
                                 password="2Mqy0S0xPBjMQireJRAD5NfDf",
                                 user_domain_name='default',
                                 project_domain_id='default',
                                 project_id="f39d2d131e0848d68b65c77bc731f568")

sess = session.Session(auth=auth)


createNetwork1 =True
createNetwork2 =True


if(createNetwork1)

    network_name1 = distros_dict['machines'][0]['external_network']
    neutron = client.Client(session=sess)

    try:
        body_sample = {'network': {'name': network_name1,
                       'admin_state_up': True}}

        netw = neutron.create_network(body=body_sample)
        net_dict = netw['network']
        network_id = net_dict['id']
        print('Network %s created' % network_id)

        body_create_subnet = {'subnets': [{'cidr': '192.168.199.0/24',
                              'ip_version': 4, 'network_id': network_id}]}

        subnet = neutron.create_subnet(body=body_create_subnet)
        print('Created subnet %s' % subnet)
    finally:
        print("Execution completed")



if(createNetwork2)


    network_name2 = distros_dict['machines'][0]['private_netowrk']
    neutron = client.Client(session=sess)

    try:
        body_sample = {'network': {'name': network_name,
                   'admin_state_up': True}}

        netw = neutron.create_network(body=body_sample)
        net_dict = netw['network']
        network_id = net_dict['id']
        print('Network %s created' % network_id)

        body_create_subnet = {'subnets': [{'cidr': '10.0.99.0/24',
                              'ip_version': 4, 'network_id': network_id}]}

        subnet = neutron.create_subnet(body=body_create_subnet)
        print('Created subnet %s' % subnet)
    finally:
        print("Execution completed")










#beow code for running  multiple bash commands
# proc1 = subprocess.Popen(['l
# s'], stdout=subprocess.PIPE)
# proc2 = subprocess.Popen(['grep', 'main.py'], stdin=proc1.stdout,
#                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
# out, err = proc2.communicate()
# print(out)
# #print('err: {0}'.format(err))



    
with open("env.yaml", 'r+') as stream:
    try:
        loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

loaded['parameters']['key_name']=distros_dict['machines'][0]['key_pair']
loaded['parameters']['image']= distros_dict['machines'][0]['image']
loaded['parameters']['vm_name']= distros_dict['machines'][0]['vm_name']
loaded['parameters']['flavour']= distros_dict['machines'][0]['flavour']
loaded['parameters']['network-ext']= distros_dict['machines'][0]['external_network']
loaded['parameters']['network-pvt']= distros_dict['machines'][0]['private_netowrk']


try:
    yaml.safe_dump(loaded, file("env.yaml",'w'), encoding='utf-8', allow_unicode=True)
except yaml.YAMLError as exc:
        print(exc)




# loader = loading.get_plugin_loader('password')
# auth = loader.load_from_options(auth_url="http://10.81.1.155:5000/v3",
#                                  username="sahal",
#                                  password="1234",
#                                  user_domain_name='default',
#                                  project_domain_id='default',
#                                 project_id="08e259cda26d4044a12e29860c0237f4")
sess = session.Sheat = client.Client('1', session=sess)
heat.stacks.create("mystack",)
ession(auth=auth)
# print(heat.stacks.list())
# print list(heat.stacks.list())