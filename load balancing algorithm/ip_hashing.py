import hashlib
class IPHash:
    def __init__(self,servers):
        self.servers=servers
    def get_next_Server(self,client_ip):
        hash_value=hashlib.md5(client_ip.encode()).hexdigest()
        index=int(hash_value,16)%len(self.servers)
        return self.servers[index]
servers=["server1","server2","server3"]
load_balancer=IPHash(servers)
client_ips=["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5"]
for ip in client_ips:
    server=load_balancer.get_next_Server(ip)
    print(f"Client {ip} is routed to {server}")


