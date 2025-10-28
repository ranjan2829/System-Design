import time
class FixedWindow:
    def __init__(self,max_requests,window_size):
        self.window_size=window_size
        self.max_requests=max_requests
        self.current_window=time.time()
        self.requests_count=0
    def allow_request(self):
        current_time=time.time()
        window=current_time//self.window_size
        if window!=self.current_window:
            self.current_window=window
            self.requests_count=0
        if self.requests_count<self.max_requests:
            self.requests_count+=1
            return True
        return False
rate_limiter=FixedWindow(10,60)
for i in range(12):
    if rate_limiter.allow_request():
        print(f"Request {i+1} is allowed")
    else:
        print(f"Request {i+1} is denied")