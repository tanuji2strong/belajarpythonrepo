def is_palindrome(s):
    # Clean: lowercase, remove spaces
    cleaned = ''.join(char.lower() for char in s if char != ' ')
    return cleaned == cleaned[::-1]

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))                   # False
