import sys
import re

file_name=sys.argv[1]

with open(file_name) as fh:

    def svcFile(value):
        for line in fh:
            if(re.search("^name=", line)):
                data = re.findall('".*"', line)
                name=re.sub('"', '', data[0])
                print(name)
    svcFile('name')
                      

