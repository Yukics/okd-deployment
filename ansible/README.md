# Infra needed:
1. Opnsense
    1. Unbound DNS
    2. KEA DHCPv4
        1. Add to subnet conf
            + Next server: loadbalancer IP
            + TFTP bootfile name: ipxe-x86_64.efi (menu/boot.ipxe)
2. Proxmox
    1. RHEL like template (ex. Rocky)

# Configuration
1. conf/infra.yaml
2. conf/redhat.yaml -> remove .modify extension
3. conf/opnsense.yaml -> remove .modify extension
4. conf/proxmox.yaml

# Launch cluster
```bash
dnf install sshpass # or apt
pip install proxmoxer httpx requests_toolbelt jmespath
ansible-galaxy collection install ansibleguy.opnsense kwoodson.yedit
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i inventory.ini main.yaml
```
