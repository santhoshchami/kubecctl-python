#!/usr/bin/python


from kubernetes import client, config

#config.load_incluster_config()
config.load_kube_config()

v1=client.CoreV1Api()

pod=client.V1Pod()
#import pdb; pdb.set_trace()
spec=client.V1PodSpec(containers='Test')
pod.metadata=client.V1ObjectMeta(name="busybox")

container=client.V1Container(name='Temp')
container.image="busybox"
#container.args=["sleep", "3600"]
container.name="busybox"

spec.containers = [container]
pod.spec = spec

ret = v1.list_namespaced_pod(namespace="default")
for i in ret.items:
    print("%s  %s  %s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

v1.create_namespaced_pod(namespace="default",body=pod)

ret = v1.list_namespaced_pod(namespace="default")
for i in ret.items:
    print("%s  %s  %s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
