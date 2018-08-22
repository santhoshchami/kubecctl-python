#!/usr/bin/python

from kubernetes import client, config
from kubernetes.client import V1ServiceList

import sys

for i in dir(V1ServiceList): print i
