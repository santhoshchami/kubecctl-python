# Run commands based on the below syntacs:

# List pods in a specific namespace:

python calkube get-pods -n default
 
# Create services in a specific namespace:
# Need to prepare yaml file based on the below format:

# Copy config file from /home/usr/.kube/conf to pwd 

metadata:
    name: nginx
    app: nginx
    namespace: default
spec:
    port: 80
    target_port: 9370

   # calkube create-svc -f nginx.yaml      

# Create deployment with yaml file

metadata:
    name: nginx
    app: nginx
    namespace: default
    image: nginx
spec:
    replicas: 2
    port: 80

   # calkube create-dc -f deployment.yaml

# Update deployment with the same as above yaml file and changed values

  # calkube update-dc -f deployment.yaml

# Delete deployment from yaml file

   # calkube del-dc -f deployment.yaml

# Delete Pods
   # calkube del-pod pod-name default

# delete service
  #/calkube del-svc service name default


