from kubernetes import client, config


# load the Kubernetes configuration from the default location
config.load_kube_config()

# specify the name of the deployment and its namespace
deployment_name = 'my-app'
namespace = 'default'

# create an instance of the Kubernetes API client
api = client.AppsV1Api()

# get the deployment object from the API server
deployment = api.read_namespaced_deployment(name=deployment_name, namespace=namespace)


#extract the CPU and memory requests and limits from the deployment object
cpu_request = deployment.spec.template.spec.containers[0].resources.requests['cpu']
cpu_limit = deployment.spec.template.spec.containers[0].resources.limits['cpu']
# memory_limit = deployment.spec.template.spec.containers[0].resources.limits['memory']
# memory_request = deployment.spec.template.spec.containers[0].resources.requests['memory']

#print the CPU and memory resources
print("CPU Request:", cpu_request)
print("CPU Limit:", cpu_limit)
# print("Memory Request:",memory_request)
# print("Memory Limit:",memory_limit)







