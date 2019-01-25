#!/usr/bin/python
#------------------------------------------------------------------------------------------
#                                                                                         -
# Copyright 2018 The Authors.                                                             -
#                                                                                         -
# Created at : April-2018                                                                 -
#                                                                                         -
# Authors Santhosh Chami                                                                  -
#                                                                                         -
# Description : Kubernetes API client                                                     -
#                                                                                         -
#------------------------------------------------------------------------------------------

import os
import sys
import re
import yaml

from kubernetes import client, config

config.load_kube_config(
    os.path.join(os.environ["HOME"], 'calkube/conf/config'))

v1 = client.CoreV1Api()

service = client.V1Service()
service.api_version = "v1"
service.kind = "Service"

#------------------------> Class to kubernetes lifecycle management <----

class calkube:

    '''
    This class is for lifecycle management of Kubernetes
    Kubernetes API using config file
    '''


    def getPods(*args):
        """
        Function to call kubernetes API and get the pods details
        pod name, pod status and pod ips
        """
        try:
            ns = sys.argv[2]
            ns1 = sys.argv[3]
            if ns.lower() == '-n':
                pod_list = v1.list_namespaced_pod(ns1)
                for pod in pod_list.items:
                    print("%s\t%s\t%s" % (pod.metadata.name,
                                          pod.status.phase,
                                          pod.status.pod_ip))
        except IndexError:
            print("Error: unknown command")


    def create_deployment_object(*args):
        """
        Function to create deplyment with replication
        configuration details fetch from yaml input
        """
        fh = sys.argv[2]
        fh1 = sys.argv[3]
        if fh.lower() == '-f':
            with open(fh1)as f:
                config = yaml.load(f)
                name = config["metadata"]["name"]
                image = config["metadata"]["image"]
                app = config["metadata"]["app"]
                namespace = config["metadata"]["namespace"]
                port = config["spec"]["port"]
                replicas = config["spec"]["replicas"]
                container = client.V1Container(
                    name=name,
                    image=image,
                    ports=[client.V1ContainerPort(container_port=port)])

                template = client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={"app": app}),
                    spec=client.V1PodSpec(containers=[container]))

                spec = client.ExtensionsV1beta1DeploymentSpec(
                    replicas=replicas,
                    template=template)

                deployment = client.ExtensionsV1beta1Deployment(
                    api_version="extensions/v1beta1",
                    kind="Deployment",
                    metadata=client.V1ObjectMeta(name=name),
                    spec=spec)

        return deployment

    def create_deployment(api_instance, deployment):
        '''
        Function is to create deployment
        need to pass required information through yaml
        '''
        fh = sys.argv[2]
        fh1 = sys.argv[3]
        if fh.lower() == '-f':
            with open(fh1)as f:
                config = yaml.load(f)
                namespace = config["metadata"]["namespace"]
                name = config["metadata"]["name"]
                api_response = api_instance.create_namespaced_deployment(
                    body=deployment,
                    namespace=namespace)
        print("Deployment %s has been created successfully" % name)


    def createDc(self, *args):
        '''
        Call function to create Deployment
        '''
        try:

            extensions_v1beta1 = client.ExtensionsV1beta1Api()
            deployment = self.create_deployment_object()
            create_deployment(
                extensions_v1beta1,
                deployment)

        except KeyError:
            print('Configuration Key Error:')

        except client.rest.ApiException:
            print("Error: deployment already exists!")
            return

    def createSvc(*args):
        """
        Function to create service with ports

        Using Yaml module to fetch information from yaml file
        """

        fh = sys.argv[2]
        fh1 = sys.argv[3]
        if fh.lower() == '-f':
            try:
                with open(fh1)as f:
                    config = yaml.load(f)
                    name = config["metadata"]["name"]
                    app = config["metadata"]["app"]
                    namespace = config["metadata"]["namespace"]
                    port = config["spec"]["port"]
                    target_port = config["spec"]["target_port"]
                    service.metadata = client.V1ObjectMeta(
                        name=name)
                    spec = client.V1ServiceSpec()
                    spec.selector = {"app": app}
                    spec.ports = [client.V1ServicePort(
                        protocol="TCP",
                        port=port,
                        target_port=target_port)]
                    service.spec = spec
                    v1.create_namespaced_service(
                        namespace=namespace,
                        body=service)
            except KeyError:
                print('Configuration Key Error:')

            except client.rest.ApiException:
                print("Error: service already exists!")
                return

            print("service created successfully!")

        else:
            print("Missing the required parameter")



    def update_deployment(self, api_instance, deployment):
        '''
        Function to update existing deployment
        value will be taken from yaml
        '''
        fh = sys.argv[2]
        fh1 = sys.argv[3]
        if fh.lower() == '-f':
            with open(fh1)as f:
                config = yaml.load(f)
                name = config["metadata"]["name"]
                image = config["metadata"]["image"]
                app = config["metadata"]["app"]
                namespace = config["metadata"]["namespace"]
                port = config["spec"]["port"]
                replicas = config["spec"]["replicas"]

                deployment.spec.template.spec.containers[0].image = image
                api_response = api_instance.patch_namespaced_deployment(
                    name=name,
                    namespace=namespace,
                    body=deployment)

        print("Deployment updated Successfully!")

    def updateDc(self, *args):
        '''
        Call function to update Deployment
        '''
        try:

            extensions_v1beta1 = client.ExtensionsV1beta1Api()
            deployment = self.create_deployment_object()
            self.update_deployment(extensions_v1beta1, deployment)

        except KeyError:

            print('Configuration Key Error:')

        except client.rest.ApiException:

            print("Error: deployment not found!")

            return



    def delPods(*args):
        """
        Function to delete pods in a provided namespace
        if pods or namespace not found through the same error
        """
        try:
            name = sys.argv[2]
            ns = sys.argv[3]
            ns1 = sys.argv[4]
            if ns.lower() == '-n':
                v1.delete_namespaced_pod(
                    name=name,
                    namespace=ns1,
                    body=client.V1DeleteOptions())
        except client.rest.ApiException:
            print("Error: POD %s not found" % name)
        except IndexError:
            print("Error: unknown command")
            return

            print('POD deleted successfully!')


    def delSvc(*args):
        """
        Function to delete service in a provided name space
        If service or namespace not found through the same error
        """
        try:
            name = sys.argv[2]
            ns = sys.argv[3]
            ns1 = sys.argv[4]
            if ns.lower() == '-n':
                v1.delete_namespaced_service(
                    name=name,
                    namespace=ns1,
                    body=client.V1DeleteOptions())
        except client.rest.ApiException:
            print("Error: service %s not found" % name)
        except IndexError:
            print("Error: unknown command")
            return

            print('Service deleted successfully!')


    def delete_deployment(self, api_instance):
        '''
        Funcion to delete deployment
        '''

        fh = sys.argv[2]
        fh1 = sys.argv[3]
        if fh.lower() == '-f':
            with open(fh1)as f:
                config = yaml.load(f)
                namespace = config["metadata"]["namespace"]
                name = config["metadata"]["name"]

                api_response = api_instance.delete_namespaced_deployment(
                    name=name,
                    namespace=namespace,
                body=client.V1DeleteOptions(
                    propagation_policy='Foreground',
                    grace_period_seconds=5))

        print("Deployment %s has been deleted successfully!" % name)


    def deleteDc(self, *args):
        '''
        Call function to update Deployment
        '''
        try:

            extensions_v1beta1 = client.ExtensionsV1beta1Api()
            deployment = self.create_deployment_object()
            self.delete_deployment(extensions_v1beta1)

        except KeyError:
            print('Configuration Key Error:')

        except client.rest.ApiException:
            print("Error: deployment not found!")
            return

    # check the length of command line argument
    # If less than 2 then exit the program

if __name__ == '__main__':
     calkube_obj = calkube()
# END....
