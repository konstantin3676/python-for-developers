import threading
import time

def print_numbers(thread_name):
    for i in range(1, 11):
        print(f"[{thread_name}] {i}")
        time.sleep(1)

if __name__ == "__main__":
    threads = []
    num_threads = 3

    for i in range(num_threads):
        thread = threading.Thread(target=print_numbers, args=(f"Thread-{i+1}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()