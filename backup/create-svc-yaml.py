#!/usr/bin/python

from kubernetes import client, config

import sys
import yaml
config.load_kube_config()
fh = sys.argv[1]
fh1 = sys.argv[2]
if fh.lower() == '-f':

    with open(fh1)as f:
        config = yaml.load(f)
        name = config["metadata"]["name"]
        app = config["metadata"]["app"]
        namespace = config["metadata"]["namespace"]
        port = config["spec"]["port"]
        target_port = config["spec"]["target_port"]

        api_instance = client.CoreV1Api()
        service = client.V1Service()
        service.api_version = "v1"
        service.kind = "Service"
        service.metadata = client.V1ObjectMeta(name=name)
        spec = client.V1ServiceSpec()
        spec.selector = {"app": app}
        spec.ports = [client.V1ServicePort(
                                           protocol="TCP",
                                           port=port,
                                           target_port=target_port)]
        service.spec = spec
        api_instance.create_namespaced_service(namespace=namespace, body=service)
