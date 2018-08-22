import sys

fh = sys.argv[1]
if fh.lower() == '-f':

    with open('fh.txt', 'r') as f:
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
        print  (data1[2])
        ##########
        data = lines[3]
        data1 = data.split()
        print (data1[2])
        ###########
        data = lines[4]
        data1 = data.split()
        namespace = data1[2]
else:
    print ('configuration file not found')

