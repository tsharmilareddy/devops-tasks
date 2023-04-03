from kubernetes import client, config


# load the Kubernetes configuration from the default location
config.load_kube_config()

# specify the name of the deployments and their namespace
deployments = [
    {'name': 'deployment', 'namespace': 'deployment'},
    {'name': 'nginx', 'namespace': 'nginx'}
]

# create an instance of the Kubernetes API client
api = client.AppsV1Api()

total_cpu_request = 0
total_cpu_limit = 0
total_memory_request = 0
total_memory_limit = 0

for deployment in deployments:
    # get the deployment object from the API server
    deployment_obj = api.read_namespaced_deployment(name=deployment['name'], namespace=deployment['namespace'])

    # extract the CPU and memory requests and limits from the deployment object
    cpu_request = deployment_obj.spec.template.spec.containers[0].resources.requests['cpu']
    print(cpu_request)
    cpu_limit = deployment_obj.spec.template.spec.containers[0].resources.limits['cpu']
    memory_request = deployment_obj.spec.template.spec.containers[0].resources.requests['memory']
    memory_limit = deployment_obj.spec.template.spec.containers[0].resources.limits['memory']



    #add the CPU and memory resources to the total
    total_cpu_request += int(cpu_request)
    total_cpu_limit += int(cpu_limit)
    total_memory_request +=int( memory_request)
    total_memory_limit +=int( memory_limit)

# print the total CPU and memory resources
print("Total CPU Request:", total_cpu_request)
print("Total CPU Limit:", total_cpu_limit)
print("Total Memory Request:", total_memory_request)
print("Total Memory Limit:", total_memory_limit)
