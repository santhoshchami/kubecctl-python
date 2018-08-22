#!/usr/bin/python

def cmdLine(*args):
   var = "this is test variable"
   var1 = "this is second test variable"
   return "var1, var"

def output(*args):
   var = cmdLine(*args)
   print (var)
output()

