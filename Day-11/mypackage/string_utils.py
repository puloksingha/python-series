"""
string_utils.py — String manipulation utilities
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def count_vowels(text):
    """Count vowels in text."""
    return sum(1 for c in text.lower() if c in 'aeiou')
