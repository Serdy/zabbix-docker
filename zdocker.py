#!/bin/python
# import docker
import sys
import json
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')
args = '7e82f243affde6807a44b9c1725abb4da8e1980992fe05c81e48ace10c6be358'
docker_inspect = cli.inspect_container(args)
test = cli.containers()
# print test
# docker_inspect2 = json.loads(docker_inspect)
# print docker_inspect

def container_name(cli):
	count_containers = 0
	docker_run_name = []
	containers = cli.containers(all=True)
	for container in containers:
		status = container['Status']
		if status.startswith("Up"):
			docker_run_name.append('{{#DOCKER_NAME}:' + str(container['Names']) + '}')
			# docker_run_name = container['Names']
			docker_run_id = container['Id']
			# print json.dumps({
	  #                   "{#DOCKER_NAME}": docker_run_name,    	  
	  #                   },)
	return docker_run_name


print (json.dumps({'data': (container_name(cli))}, indent=4))
# print (container_name(cli))
# print(json.dumps("date": {"c": 0, "b": 0, "a": 0}))
# print container_name(cli)

# print (json.dumps({'data': ({'bar': 23},{'bar': 55})}))



# print docker_run_name