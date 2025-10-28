import time

class SlidingWindowCounter:
    def __init__(self, window_size, max_requests):
        self.window_size = window_size
        self.max_requests = max_requests
        self.current_window = time.time() // window_size
        self.request_count = 0
        self.previous_count = 0

    def allow_request(self):
        now = time.time()
        window = now // self.window_size

        if window != self.current_window:
            self.previous_count = self.request_count
            self.request_count = 0
            self.current_window = window

        window_elapsed = (now % self.window_size) / self.window_size
        threshold = self.previous_count * (1 - window_elapsed) + self.request_count

        if threshold < self.max_requests:
            self.request_count += 1
            return True
        return False

limiter = SlidingWindowCounter(window_size=60, max_requests=5)

for _ in range(10):
    print(limiter.allow_request())
    time.sleep(0.1)

time.sleep(30)
print(limiter.allow_request())