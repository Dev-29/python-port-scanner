# Python Port Scanner
# This script checks for any open ports
import socket
import threading
from queue import Queue

# Local machine inet
target = "127.0.0.1"
queue = Queue()
open_ports = []


def port_scan(port):
    try:
        # AF_INET specifies we are using Internet rather than UNIX Socket
        # SOCK_STREAM specifies we are using TCP instead of UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print(f'Port {port} is open')
            open_ports.append(port)


port_list = range(1, 20000)
fill_queue(port_list)

# Using threading to speed up process
thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Open Ports are {open_ports}')
