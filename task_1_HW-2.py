
import queue
import threading
import time
import random

request_queue = queue.Queue()


def generate_request_id():
    return int(time.time() * 1000) + random.randint(0, 999)


def generate_request():
    request_id = generate_request_id()
    request_queue.put(request_id)
    print(f"Нова заявка додана до черги: {request_id}")


def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Обробка заявки: {request_id}")
            time.sleep(random.uniform(0.5, 1.5))
            print(f"Заявку {request_id} оброблено")
        else:
            print("Черга пуста")
            time.sleep(1)


def main():
    try:
        threading.Thread(target=process_request, daemon=True).start()

        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 2))
    except KeyboardInterrupt:
        print("Програма завершена користувачем")


if __name__ == "__main__":
    main()
