from proxmoxer import ProxmoxAPI
import yaml

def get_VM_from_MAC(mac):
    with open("proxmox.yaml") as stream:
        try:
            proxmox_conf = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    proxmox = ProxmoxAPI(
        proxmox_conf['proxmox_api_host'], user=proxmox_conf['proxmox_api_user'], password=proxmox_conf['proxmox_api_password'], verify_ssl=False
    )

    for node in proxmox.nodes.get():
        for vm in proxmox.nodes(node["node"]).qemu.get():
            if mac.upper() in proxmox.nodes(node["node"]).qemu(vm['vmid']).get('config')['net0']:
                return vm['name']