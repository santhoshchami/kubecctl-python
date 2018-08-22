#!/usr/bin/python
import os
import sys
import re
import yaml

from kubernetes import client, config

config.load_kube_config()
v1 = client.V1ServiceList()

ret = v1.V1ServiAceList()
print (ret)
#for i in ret.items:
#    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
