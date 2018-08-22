import yaml
with open('nginx.yaml', 'r') as f:
    config = yaml.load(f)
name = config["metadata"]["name"]
app = config["metadata"]["app"]
namespace = config["metadata"]["namespace"]
port = config["spec"]["port"]
tport = config["spec"]["tport"]
print name
print app
print namespace
print port
print tport
