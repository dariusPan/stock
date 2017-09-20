import os

def get_deliveryserver_default_ip():
    s = os.popen("docker network inspect deliveryserver_default | grep Gateway").read()
    gateway, ip = s.split(':')
    ip = ip.strip().replace('"', '').split('/')[0]
    site = "http://" + str(ip) + ":3000"
    return site
