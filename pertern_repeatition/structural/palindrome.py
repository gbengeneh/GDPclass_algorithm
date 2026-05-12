#Detecting palindrome
def is_palindrome(text):
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

# Test it
test_string = "madam"
test_string2 = "noon"
print(is_palindrome(test_string))
print(is_palindrome(test_string2))