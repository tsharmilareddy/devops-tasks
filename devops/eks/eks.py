from kubernetes import client, config


# load the Kubernetes configuration from the default location
config.load_kube_config()

# specify the name of the deployments and their namespace
deployments = []
with open('deployments.txt', 'r') as f:
    for line in f:
        name, namespace = line.strip().split(",")
        deployments.append({'name': name, 'namespace': namespace})

# create an instance of the Kubernetes API client
api = client.AppsV1Api()

total_cpu_request = 0
total_cpu_limit = 0
# total_memory_request = 0
# total_memory_limit = 0

for deployment in deployments:
    # get the deployment object from the API server
    deployment_obj = api.read_namespaced_deployment(name=deployment['name'], namespace=deployment['namespace'])

    # extract the CPU and memory requests and limits from the deployment object
    cpu_request_str = deployment_obj.spec.template.spec.containers[0].resources.requests['cpu']
    cpu_limit_str = deployment_obj.spec.template.spec.containers[0].resources.limits['cpu']

    # convert CPU requests and limits from milli CPUs to CPUs
    cpu_request = float(cpu_request_str.replace("m", "")) / 1000
    cpu_limit = float(cpu_limit_str.replace("m", "")) / 1000

    # add the CPU and memory resources to the total
    total_cpu_request = total_cpu_request+ cpu_request
    total_cpu_limit = total_cpu_limit + cpu_limit


# print the total CPU and memory resources
print("Total CPU Request:", total_cpu_request)
print("Total CPU Limit:", total_cpu_limit)
# print("Total Memory Request:", total_memory_request)
# print("Total Memory Limit:", total_memory_limit)
