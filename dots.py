# import threading
# import time

# def print_dots_and_message(message, dot_count=4, dot_delay=0.125):
#     def print_dots():
#         for _ in range(dot_count):
#             print(".", end="", flush=True)
#             time.sleep(dot_delay)
#         print(" " + message)

#     dot_thread = threading.Thread(target=print_dots)
#     dot_thread.start()
#     dot_thread.join()

# if __name__ == "__main__":
#     print_dots_and_message("Macarena")
#     print_dots_and_message("Bamba")

# import time

# def print_dots_and_message(message, dot_count=3, dot_delay=0.5):
#     dots = "." * dot_count
#     print(dots + " " + message)

# if __name__ == "__main__":
#     print_dots_and_message("Macarena")
#     print_dots_and_message("Bamba")

import time

def print_dots(message, dot_count=6, dot_delay=0.625, emoji="🎧"):
    print(emoji, end="", flush=True)
    for _ in range(dot_count):
        print(".", end="", flush=True)
        time.sleep(dot_delay)
    
    print(" ", end="", flush=True)
    print(message)
    # for char in message:
    #     print(char, end="", flush=True)
    #     time.sleep(dot_delay)
    
    # print()  # Move to the next line after printing the message

if __name__ == "__main__":
    print_dots("Macarena")
    print_dots("Bamba")