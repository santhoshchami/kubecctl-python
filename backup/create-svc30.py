#!/usr/bin/python

from kubernetes import client, config

import sys

fh = sys.argv[1]
fh1 = sys.argv[2]
if fh.lower() == '-f':

    with open(fh1)as f:
        lines = f.readlines()
        data = lines[0]
        data1 = data.split()
        name = data1[2]
        ###########
        data = lines[1]
        data1 = data.split()
        app = data1[2]
        ###########
        data = lines[2]
        data1 = data.split()
        port = data1[2]
        ##########
        data = lines[3]
        data1 = data.split()
        tport = data1[2]
        ###########
        data = lines[4]
        data1 = data.split()
        namespace = data1[2]

        config.load_kube_config()
        api_instance = client.CoreV1Api()
        service = client.V1Service()
        service.api_version = "v1"
        service.kind = "Service"
        service.metadata = client.V1ObjectMeta(name=name)
        spec = client.V1ServiceSpec()
        spec.selector = {"app": app}
        spec.ports = [client.V1ServicePort(
                                           protocol="TCP",
                                           port=80,
                                           target_port=9370)]
        service.spec = spec
        api_instance.create_namespaced_service(namespace=namespace, body=service)
