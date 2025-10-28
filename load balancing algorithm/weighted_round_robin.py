class WeightedRoundRobin:
    def __init__(self,servers):
        self.servers=servers
        self.current_index=0
        self.current_weight=max(server[1] for server in self.servers)
    def get_next_server(self):
        while True:
            self.current_index=(self.current_index+1)%len(self.servers)
            if self.current_index==0:
                self.current_weight-=1
                if self.current_weight<=0:
                    self.current_weight=max(server[1] for server in self.servers)
            if self.servers[self.current_index][1]>=self.current_weight:
                return self.servers[self.current_index][0]
servers=[("server1",1),("server2",2),("server3",3)]
load_balancer=WeightedRoundRobin(servers)
for i in range(10):
    server=load_balancer.get_next_server()
    print(f"Request {i+1} is routed to {server}")