import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from lib.network import *
from lib.proxmox import *

app = FastAPI()

app.mount("/media", StaticFiles(directory="../installation/media"), name="media")
app.mount("/installation", StaticFiles(directory="../installation"), name="installation")

@app.get("/http-ignition")
def root(request: Request):
    mac = get_MAC_from_IP(request.client.host)
    vm_name = get_VM_from_MAC(mac)
    print("INFO: {}: Responding {} configuration ".format(request.client.host, vm_name))
    f = open("../installation/{}.ign".format(vm_name), "r")
    json = f.read()
    return Response(content=json, media_type="application/json")

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0', reload=True)