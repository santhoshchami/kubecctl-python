#!/usr/bin/python
#------------------------------------------------------------------------------------------
#                                                                                         -
# Copyright 2018 The Authors.                                                             -
#                                                                                         -
# Created at : April-2018                                                                 -
#                                                                                         -
# Description : Kubernetes API client                                                     -
#                                                                                         -
#------------------------------------------------------------------------------------------

import os
import sys
import re
import yaml

from kubernetes import client, config


config.load_kube_config()
v1 = client.CoreV1Api()

service = client.V1Service()
service.api_version = "v1"
service.kind = "Service"

class calkube:

    '''
    This class is for lifecycle management of Kubernetes
    Kubernetes API using config file
    '''

    def getPods(self, *args):
        pod_list = v1.list_namespaced_pod (sys.argv[2])
        for pod in pod_list.items:
            print("%s\t%s\t%s" % (pod.metadata.name,
                                  pod.status.phase,
                                  pod.status.pod_ip))


    if __name__ == '__main__':
        if len(sys.argv) <2:
            print('Error: Required resource not specified')
            sys.exit(-1)

    # operation commands  functions for command line arguments

        opscmd = {'get-pods': getPods}
    
   # Error handling for unsupported command line arguments
        try:
            op_func = opscmd[sys.argv[1]]
        except KeyError:
            print('Error: Unsupported command operation!')
            sys.exit(-1)

        op_func(sys.argv[-1])


