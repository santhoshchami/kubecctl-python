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

from src import kube

import sys

if len(sys.argv) < 2:

    print('Error: Required resource not specified')

    sys.exit(-1)

# operation commands  functions for command line arguments
calkube_obj = kube.calkube()

opscmd = {'get-pods': calkube_obj.getPods,
          'create-svc': calkube_obj.createSvc,
          'create-dc': calkube_obj.createDc,
          'update-dc': calkube_obj.updateDc,
          'del-dc': calkube_obj.deleteDc,
          'del-pod': calkube_obj.delPods,
          'del-svc': calkube_obj.delSvc}

# Error handling for unsupported command line arguments
try:
    op_func = opscmd[sys.argv[1]]
except KeyError:
    print('Error: Unsupported command operation!')
    sys.exit(-1)

op_func(sys.argv[-1])
