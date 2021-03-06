#!/bin/python
# import docker
import sys
import json
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')
# args = '7e82f243affde6807a44b9c1725abb4da8e1980992fe05c81e48ace10c6be358'
# docker_inspect = cli.inspect_container(args)
# test = cli.containers()

def container_name(cli):
	count_containers = 0
	docker_run_name = []
	containers = cli.containers(all=True)
	for container in containers:
		status = container['Status']
		if status.startswith("Up"):
			docker_run_name.append(dict([('{{#DOCKER_NAME}', str(container['Names'][0][1:])) ]))
			docker_run_id = container['Id']
	return docker_run_name
# print (json.dumps({'data': (container_name(cli))}, indent=4))

def container_top(cli):
	count_containers = 0
	docker_run_name = []
	containers = cli.containers(all=True)
	for container in containers:
		print (container)
		# for x in container:
		# 	print (x)
		Id = container['Id']
		top = cli.top(Id)
		stats = cli.stats(Id)
		a = 1
		for stat in stats:
			stat_dec = str(stat.decode("utf-8"))
			statistic = json.loads(stat_dec)
			print (statistic['network']['tx_bytes'])
			print (statistic)
			if a == 1 :
				break
			a+=1



container_top(cli)














