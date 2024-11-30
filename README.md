# OKD Deployment

This repo is meant to help people on deploying OKD on their infraestructure

## Infraestructure

+ 2 x Proxmox Nodes (platon, socrates)
+ 1 x Opnsense (dhcp, bind9)

## Repo structure

### ./ansible

Refer to the ansible README.md where you will find everything you need to correctly deploy the cluster, including configuration files

### ./http-ignition

Is a very lightweight fastapi service that will response the correct ignition file to each host booting on iPXE

### ./kubernetes

Basic cluster configuration and applications I do think are necessary
