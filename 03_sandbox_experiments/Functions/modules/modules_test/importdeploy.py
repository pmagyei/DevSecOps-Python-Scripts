import deploy_infrastructure as de # imports module and assigns an alias

to_deploy = ['Ubuntu Server', 'RHEL 9 Server', 'Windows Server']
deployed = []

de.deploy_infra(to_deploy[:], deployed)
de.show_completed_deployment(deployed)

