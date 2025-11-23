import random
import time
from queue import Queue


class Request:
    counter = 0

    def __init__(self, data):
        Request.counter += 1
        self.id = Request.counter
        self.data = data


queue = Queue()


def generate_request(number_of_requests):
    print(f" >> Generating {number_of_requests} requests <<")
    for _ in range(number_of_requests):
        request = Request(str(int(time.time() * 1000)))
        queue.put(request)


def process_request(number_of_requests):
    print(f" >> Going to process {number_of_requests} requests <<")
    for _ in range(number_of_requests):
        if not queue.empty():
            request = queue.get()
            print(f"    >> processing request {request.id}")
            queue.task_done()
        else:
            print("  >> queue is empty")
            break


while True:
    generate_request(random.randint(1, 10))
    process_request(random.randint(1, 10))
    print(f"\nQUEUE SIZE: {queue.qsize()}\n")
    time.sleep(1)
