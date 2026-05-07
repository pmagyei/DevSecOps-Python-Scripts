from deploy_infrastructure import *

to_deploy = ['Ubuntu Server', 'RHEL 9 Server', 'Windows Server']
deployed = []

deploy_infra(to_deploy[:], deployed)
show_completed_deployment(deployed)

print(to_deploy)


#  parameter *args + **args