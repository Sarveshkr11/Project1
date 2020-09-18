#! /usr/bin/pythopn3

print("content-type:text/html")
print()

import subprocess as sp 
import cgi

form=cgi.FieldStorage()

osname=form.getvalue("x")
print(osname)

cmd="docker run -d -i -t --name {0} ubuntu:14.04".format(osname)

output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]

if status==0
 print("os launched named {}".format(osname))
else:
 print("Error: {}".format(out))