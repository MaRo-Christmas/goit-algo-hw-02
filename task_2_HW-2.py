
from collections import deque

def is_palindrome(s):
    cleaned_str = ''.join(filter(str.isalnum, s)).lower()
    char_deque = deque(cleaned_str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

while True:
    user_input = input("Введіть рядок або 'exit' для виходу: ")
    
    if user_input.lower() == 'exit':
        print("Програма завершена.")
        break
    
    if is_palindrome(user_input):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")