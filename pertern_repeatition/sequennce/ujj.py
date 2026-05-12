# Example: Detecting Palindromes
def is_palindrome(text):
    """
    Palindrome pattern: reads the same forwards and backwards
    Examples: 'racecar', 'madam', '12321'
    """
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

is_palindrome("madam")