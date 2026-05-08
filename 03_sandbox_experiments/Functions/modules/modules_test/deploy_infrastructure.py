def deploy_infra(not_deployed, deploying):
    """
    Simulate deploying rach server, until none are left.
    Move each server to deployed after deployment
    """
    while not_deployed:
        process_deployment = not_deployed.pop()
        print(f"Deploying: {process_deployment}")
        deploying.append(process_deployment)

def show_completed_deployment(completed_deployment):
    """Show all the deployments."""

    print("\nThe Following servers have been deployed:")
    for deployment in completed_deployment:
        print(deployment)

to_deploy = ['Ubuntu Server', 'RHEL 9 Server', 'Windows Server']
deployed = []

deploy_infra(to_deploy[:], deployed)
show_completed_deployment(deployed)

