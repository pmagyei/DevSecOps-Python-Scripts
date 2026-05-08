from deploy_infrastructure import  deploy_infra

from deploy_infrastructure import  show_completed_deployment as scd

to_deploy = ['Ubuntu Server', 'RHEL 9 Server', 'Windows Server']
deployed = []

deploy_infra(to_deploy, deployed)
scd(deployed)

print(to_deploy)

