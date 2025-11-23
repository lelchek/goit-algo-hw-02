from collections import deque


def is_palindrome(string: str):
    cleaned = string.replace(" ", "").lower()
    d = deque(cleaned)

    while len(d) >= 2:
        first_char = d.popleft()
        last_char = d.pop()

        if first_char != last_char:
            return False

    return True
