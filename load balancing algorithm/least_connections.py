import random
class LeastConnections:
    def __init__(self,servers):
        self.servers=servers
    def get_next_Server(self,client_ip):
        min_conn=min(self.servers.values())
        least=[server for server, conns in self.servers.items() if conns==min_conn]
        selected_server=random.choice(least)
        return selected_server
    def release_connection(self,server):
        if self.servers[server]>0:
            self.servers[server]-=1
servers={"server1":0,"server2":0,"server3":0}
load_balancer=LeastConnections(servers)
client_ips=["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5"]
for ip in client_ips:
    server=load_balancer.get_next_Server(ip)
    print(f"Client {ip} is routed to {server}")
    load_balancer.release_connection(server)
