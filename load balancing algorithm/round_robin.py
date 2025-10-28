class RoundRobin:
    def __init__(self,servers):
        self.servers=servers
        self.current_index=0
    def get_next_server(self):
        self.current_index=(self.current_index+1)%len(self.servers)
        return self.servers[self.current_index]
servers=["server1","server2","server3"]
load_balancer=RoundRobin(servers)
for i in range(10):
    server=load_balancer.get_next_server()
    print(f"Request {i+1} is routed to {server}")

