"""
PYTHON STRING MANIPULATION COMPREHENSIVE GUIDE
==============================================
Everything you need to know about Strings in Python
"""

# ============================================================================
# 1. STRING BASICS
# ============================================================================

print("="*70)
print("STRING BASICS")
print("="*70)

# --- Creating Strings ---
print("\nCreating Strings:")

# Single quotes
string1 = 'Hello, World!'

# Double quotes
string2 = "Hello, World!"

# Triple quotes (multi-line)
string3 = """This is a
multi-line
string"""

string4 = '''This also
works for
multi-line strings'''

# Raw strings (ignores escape characters)
raw_string = r"C:\Users\name\folder"

print(f"Single quotes: {string1}")
print(f"Double quotes: {string2}")
print(f"Multi-line:\n{string3}")
print(f"Raw string: {raw_string}")
print()


# --- String Properties ---
print("String Properties:")
text = "Python"

# Strings are immutable
print(f"Original: {text}")
# text[0] = 'J'  # This would raise TypeError!

# Strings are sequences
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print()


# ============================================================================
# 2. STRING SLICING
# ============================================================================

print("="*70)
print("STRING SLICING")
print("="*70)

text = "Python Programming"
print(f"\nOriginal string: '{text}'")
print(f"Indices:          0123456789...")
print()

# --- Basic Slicing ---
print("Basic Slicing:")
print(f"text[0:6] = '{text[0:6]}'")      # Python
print(f"text[7:18] = '{text[7:18]}'")    # Programming
print(f"text[:6] = '{text[:6]}'")        # Python (start from beginning)
print(f"text[7:] = '{text[7:]}'")        # Programming (to end)
print(f"text[:] = '{text[:]}'")          # Entire string (copy)
print()


# --- Negative Indexing ---
print("Negative Indexing:")
print(f"text[-4:] = '{text[-4:]}'")      # ming (last 4 chars)
print(f"text[:-4] = '{text[:-4]}'")      # Python Program
print(f"text[-11:-4] = '{text[-11:-4]}'")  # Program
print()


# --- Step in Slicing ---
print("Slicing with Step:")
print(f"text[::2] = '{text[::2]}'")      # Every 2nd character
print(f"text[1::2] = '{text[1::2]}'")    # Every 2nd, starting from index 1
print(f"text[::3] = '{text[::3]}'")      # Every 3rd character
print(f"text[::-1] = '{text[::-1]}'")    # Reverse string
print(f"text[::-2] = '{text[::-2]}'")    # Reverse, every 2nd char
print()


# --- Practical Slicing Examples ---
print("Practical Examples:")
email = "user@example.com"
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"Email: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")

url = "https://www.example.com/page"
protocol = url[:url.index('://')]
site = url[url.index('://')+3:]
print(f"\nURL: {url}")
print(f"Protocol: {protocol}")
print(f"Site: {site}")
print()


# ============================================================================
# 3. STRING FORMATTING
# ============================================================================

print("="*70)
print("STRING FORMATTING")
print("="*70)

name = "Alice"
age = 25
pi = 3.14159265359

# --- Old Style (%) Formatting ---
print("\n1. Old Style (%) Formatting:")
print("My name is %s and I'm %d years old." % (name, age))
print("Pi is approximately %.2f" % pi)
print()


# --- str.format() Method ---
print("2. str.format() Method:")
print("My name is {} and I'm {} years old.".format(name, age))
print("My name is {0} and I'm {1} years old.".format(name, age))
print("My name is {n} and I'm {a} years old.".format(n=name, a=age))
print()


# --- f-strings (Python 3.6+) - RECOMMENDED ---
print("3. f-strings (Recommended):")
print(f"My name is {name} and I'm {age} years old.")
print(f"Next year I'll be {age + 1} years old.")
print(f"Pi is approximately {pi:.2f}")
print()


# --- Advanced f-string Formatting ---
print("Advanced f-string Formatting:")

# Number formatting
number = 1234567.89
print(f"Comma separator: {number:,}")           # 1,234,567.89
print(f"Percentage: {0.95:.1%}")                # 95.0%
print(f"Scientific: {number:.2e}")              # 1.23e+06
print(f"Binary: {42:b}")                        # 101010
print(f"Hex: {255:x}")                          # ff
print(f"Octal: {64:o}")                         # 100
print()

# Padding and alignment
text = "Python"
print(f"Left aligned: '{text:<10}'")            # 'Python    '
print(f"Right aligned: '{text:>10}'")           # '    Python'
print(f"Center aligned: '{text:^10}'")          # '  Python  '
print(f"Zero padding: '{42:05d}'")              # '00042'
print()

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")                  # 2024-01-15
print(f"Time: {now:%H:%M:%S}")                  # 14:30:45
print(f"Full: {now:%Y-%m-%d %H:%M:%S}")         # 2024-01-15 14:30:45
print()

# Expressions in f-strings
x, y = 10, 20
print(f"Sum: {x + y}")                          # Sum: 30
print(f"Product: {x * y}")                      # Product: 200
print(f"Uppercase: {name.upper()}")             # Uppercase: ALICE
print()

# Nested f-strings
width = 10
print(f"{'Python':^{width}}")                   # '  Python  '
print()

# Multi-line f-strings
message = f"""
Hello {name},
You are {age} years old.
Next year you'll be {age + 1}.
"""
print(message)


# ============================================================================
# 4. COMMON STRING METHODS - CASE CONVERSION
# ============================================================================

print("="*70)
print("STRING METHODS - CASE CONVERSION")
print("="*70)

text = "hello world"
print(f"\nOriginal: '{text}'")
print()

print(f"upper(): '{text.upper()}'")              # HELLO WORLD
print(f"lower(): '{text.lower()}'")              # hello world
print(f"capitalize(): '{text.capitalize()}'")    # Hello world
print(f"title(): '{text.title()}'")              # Hello World
print(f"swapcase(): '{text.swapcase()}'")        # HELLO WORLD -> hello world

mixed = "Hello World"
print(f"\nMixed case: '{mixed}'")
print(f"swapcase(): '{mixed.swapcase()}'")       # hELLO wORLD
print()


# ============================================================================
# 5. SEARCHING AND CHECKING
# ============================================================================

print("="*70)
print("STRING METHODS - SEARCHING AND CHECKING")
print("="*70)

text = "Python Programming is fun!"
print(f"\nText: '{text}'")
print()

# --- Finding substrings ---
print("Finding Substrings:")
print(f"find('Python'): {text.find('Python')}")              # 0 (index)
print(f"find('is'): {text.find('is')}")                      # 19
print(f"find('Java'): {text.find('Java')}")                  # -1 (not found)
print(f"index('is'): {text.index('is')}")                    # 19
# print(f"index('Java'): {text.index('Java')}")              # Raises ValueError!
print(f"rfind('n'): {text.rfind('n')}")                      # 23 (last occurrence)
print(f"count('n'): {text.count('n')}")                      # 2
print()

# --- Checking conditions ---
print("Checking Conditions:")
print(f"startswith('Python'): {text.startswith('Python')}")  # True
print(f"endswith('fun!'): {text.endswith('fun!')}")          # True
print(f"'is' in text: {'is' in text}")                       # True
print(f"'Java' in text: {'Java' in text}")                   # False
print()

# --- Character type checking ---
print("Character Type Checking:")
print(f"'Python'.isalpha(): {'Python'.isalpha()}")           # True (all letters)
print(f"'Python123'.isalnum(): {'Python123'.isalnum()}")     # True (letters + numbers)
print(f"'12345'.isdigit(): {'12345'.isdigit()}")             # True (all digits)
print(f"'12345'.isnumeric(): {'12345'.isnumeric()}")         # True (numeric chars)
print(f"'   '.isspace(): {'   '.isspace()}")                 # True (all whitespace)
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")             # True (all uppercase)
print(f"'hello'.islower(): {'hello'.islower()}")             # True (all lowercase)
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")  # True (title case)
print()


# ============================================================================
# 6. SPLITTING AND JOINING
# ============================================================================

print("="*70)
print("STRING METHODS - SPLITTING AND JOINING")
print("="*70)

# --- split() ---
print("\nSplitting Strings:")
sentence = "Python is awesome"
words = sentence.split()
print(f"Original: '{sentence}'")
print(f"split(): {words}")

csv_data = "apple,banana,cherry"
fruits = csv_data.split(',')
print(f"\nCSV: '{csv_data}'")
print(f"split(','): {fruits}")

# Split with maxsplit
text = "one-two-three-four-five"
parts = text.split('-', 2)
print(f"\nText: '{text}'")
print(f"split('-', 2): {parts}")

# splitlines()
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(f"\nMultiline text split: {lines}")
print()


# --- join() ---
print("Joining Strings:")
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"Words: {words}")
print(f"' '.join(): '{joined}'")

csv = ",".join(words)
print(f"','.join(): '{csv}'")

path_parts = ["folder", "subfolder", "file.txt"]
path = "/".join(path_parts)
print(f"Path parts: {path_parts}")
print(f"'/'.join(): '{path}'")
print()


# --- partition() and rpartition() ---
print("Partition:")
email = "user@example.com"
before, sep, after = email.partition('@')
print(f"Email: '{email}'")
print(f"partition('@'): {before}, '{sep}', {after}")

path = "folder/subfolder/file.txt"
head, sep, tail = path.rpartition('/')
print(f"\nPath: '{path}'")
print(f"rpartition('/'): '{head}', '{sep}', '{tail}'")
print()


# ============================================================================
# 7. STRIPPING AND REPLACING
# ============================================================================

print("="*70)
print("STRING METHODS - STRIPPING AND REPLACING")
print("="*70)

# --- strip(), lstrip(), rstrip() ---
print("\nStripping Whitespace:")
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")                # 'Hello World'
print(f"lstrip(): '{text.lstrip()}'")              # 'Hello World   '
print(f"rstrip(): '{text.rstrip()}'")              # '   Hello World'

# Strip specific characters
text = "***Hello***"
print(f"\nOriginal: '{text}'")
print(f"strip('*'): '{text.strip('*')}'")          # 'Hello'

url = "https://example.com/"
clean_url = url.rstrip('/')
print(f"\nURL: '{url}'")
print(f"rstrip('/'): '{clean_url}'")
print()


# --- replace() ---
print("Replacing:")
text = "Hello World"
new_text = text.replace("World", "Python")
print(f"Original: '{text}'")
print(f"replace('World', 'Python'): '{new_text}'")

# Replace with count limit
text = "one one one one"
replaced = text.replace("one", "two", 2)
print(f"\nOriginal: '{text}'")
print(f"replace('one', 'two', 2): '{replaced}'")
print()


# --- translate() and maketrans() ---
print("Translate (advanced replacement):")
# Create translation table
translation_table = str.maketrans("aeiou", "12345")
text = "hello world"
translated = text.translate(translation_table)
print(f"Original: '{text}'")
print(f"Vowels to numbers: '{translated}'")

# Remove characters
remove_digits = str.maketrans("", "", "0123456789")
text = "Hello123World456"
clean = text.translate(remove_digits)
print(f"\nWith digits: '{text}'")
print(f"Digits removed: '{clean}'")
print()


# ============================================================================
# 8. PADDING AND ALIGNMENT
# ============================================================================

print("="*70)
print("STRING METHODS - PADDING AND ALIGNMENT")
print("="*70)

text = "Python"
print(f"\nOriginal: '{text}'")
print()

print(f"ljust(10): '{text.ljust(10)}'")           # 'Python    '
print(f"rjust(10): '{text.rjust(10)}'")           # '    Python'
print(f"center(10): '{text.center(10)}'")         # '  Python  '
print(f"ljust(10, '*'): '{text.ljust(10, '*')}'") # 'Python****'
print(f"rjust(10, '-'): '{text.rjust(10, '-')}'") # '----Python'
print(f"center(10, '='): '{text.center(10, '=')}'")  # '==Python=='
print()

# zfill() - pad with zeros
print("Zero Padding:")
print(f"'42'.zfill(5): '{'42'.zfill(5)}'")        # '00042'
print(f"'-42'.zfill(5): '{'-42'.zfill(5)}'")      # '-0042'
print(f"'3.14'.zfill(7): '{'3.14'.zfill(7)}'")    # '0003.14'
print()


# ============================================================================
# 9. ENCODING AND DECODING
# ============================================================================

print("="*70)
print("STRING ENCODING AND DECODING")
print("="*70)

# --- encode() and decode() ---
print("\nEncoding and Decoding:")
text = "Hello, 世界!"
print(f"Original: '{text}'")

# Encode to bytes
encoded_utf8 = text.encode('utf-8')
encoded_ascii = text.encode('ascii', errors='ignore')
print(f"UTF-8 encoded: {encoded_utf8}")
print(f"ASCII encoded (ignore errors): {encoded_ascii}")

# Decode back to string
decoded = encoded_utf8.decode('utf-8')
print(f"Decoded: '{decoded}'")
print()


# ============================================================================
# 10. PRACTICAL STRING OPERATIONS
# ============================================================================

print("="*70)
print("PRACTICAL STRING OPERATIONS")
print("="*70)

# --- Email validation ---
print("\n1. Email Validation:")
def is_valid_email(email):
    """Simple email validation."""
    return '@' in email and '.' in email.split('@')[1]

emails = ["user@example.com", "invalid.email", "test@domain.co"]
for email in emails:
    print(f"  {email}: {is_valid_email(email)}")
print()


# --- Password strength check ---
print("2. Password Strength Check:")
def check_password_strength(password):
    """Check if password meets basic requirements."""
    checks = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(not c.isalnum() for c in password)
    }
    return checks

password = "MyP@ssw0rd"
strength = check_password_strength(password)
print(f"  Password: {password}")
for check, passed in strength.items():
    print(f"    {check}: {'✓' if passed else '✗'}")
print()


# --- Text cleaning ---
print("3. Text Cleaning:")
def clean_text(text):
    """Remove extra whitespace and convert to lowercase."""
    # Remove leading/trailing whitespace
    text = text.strip()
    # Replace multiple spaces with single space
    text = ' '.join(text.split())
    # Convert to lowercase
    text = text.lower()
    return text

dirty = "  Hello    WORLD   from   PYTHON  "
clean = clean_text(dirty)
print(f"  Original: '{dirty}'")
print(f"  Cleaned: '{clean}'")
print()


# --- Extract numbers from string ---
print("4. Extract Numbers:")
def extract_numbers(text):
    """Extract all numbers from a string."""
    return [int(word) for word in text.split() if word.isdigit()]

text = "I have 5 apples and 10 oranges, total 15 fruits"
numbers = extract_numbers(text)
print(f"  Text: '{text}'")
print(f"  Numbers: {numbers}")
print()


# --- Title case with exceptions ---
print("5. Smart Title Case:")
def smart_title(text):
    """Title case but keep small words lowercase."""
    small_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'by'}
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return ' '.join(result)

title = "the lord of the rings"
formatted = smart_title(title)
print(f"  Original: '{title}'")
print(f"  Smart title: '{formatted}'")
print()


# --- URL slug generation ---
print("6. Generate URL Slug:")
def generate_slug(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = text.replace(' ', '-')
    # Remove non-alphanumeric characters except hyphens
    text = ''.join(c for c in text if c.isalnum() or c == '-')
    # Remove consecutive hyphens
    while '--' in text:
        text = text.replace('--', '-')
    return text.strip('-')

title = "Python String Manipulation: A Complete Guide!"
slug = generate_slug(title)
print(f"  Title: '{title}'")
print(f"  Slug: '{slug}'")
print()


# --- Word wrap ---
print("7. Word Wrap:")
def word_wrap(text, width):
    """Wrap text to specified width."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)

long_text = "This is a very long sentence that needs to be wrapped to fit within a specific width constraint."
wrapped = word_wrap(long_text, 30)
print(f"  Original: '{long_text}'")
print(f"  Wrapped (width=30):\n{wrapped}")
print()


# ============================================================================
# 11. STRING COMPARISON
# ============================================================================

print("="*70)
print("STRING COMPARISON")
print("="*70)

print("\nCase-sensitive comparison:")
print(f"'Python' == 'python': {'Python' == 'python'}")
print(f"'Python' == 'Python': {'Python' == 'Python'}")

print("\nCase-insensitive comparison:")
text1 = "Python"
text2 = "python"
print(f"text1.lower() == text2.lower(): {text1.lower() == text2.lower()}")

print("\nLexicographic comparison:")
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'zebra' > 'apple': {'zebra' > 'apple'}")
print(f"'10' < '2': {'10' < '2'}")  # String comparison, not numeric!
print()


# ============================================================================
# 12. ESCAPE CHARACTERS
# ============================================================================

print("="*70)
print("ESCAPE CHARACTERS")
print("="*70)

print("\nCommon Escape Sequences:")
print(f"Newline: 'Line1\\nLine2':\nLine1\nLine2")
print(f"Tab: 'Col1\\tCol2':\nCol1\tCol2")
print(f"Backslash: 'C:\\\\Users':\nC:\\Users")
print(f"Quote: 'She said \\'Hello\\'':\nShe said 'Hello'")
print(f"Double quote: \"He said \\\"Hi\\\"\":\nHe said \"Hi\"")
print()


# ============================================================================
# 13. MULTI-LINE STRINGS AND TEMPLATES
# ============================================================================

print("="*70)
print("MULTI-LINE STRINGS")
print("="*70)

# --- Triple-quoted strings ---
print("\nTriple-quoted string:")
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)

# --- String templates ---
print("String Templates:")
from string import Template

template = Template("Hello, $name! You have $count new messages.")
message = template.substitute(name="Alice", count=5)
print(message)

# Safe substitute (doesn't raise error for missing keys)
template2 = Template("Hello, $name! You have $count new messages.")
message2 = template2.safe_substitute(name="Bob")
print(message2)
print()


# ============================================================================
# 14. PERFORMANCE TIPS
# ============================================================================

print("="*70)
print("PERFORMANCE TIPS")
print("="*70)

print("""
1. Use join() instead of + for concatenating many strings:
   GOOD: ''.join(list_of_strings)
   BAD:  string1 + string2 + string3 + ...

2. Use f-strings for formatting (fastest):
   GOOD: f"Hello {name}"
   OKAY: "Hello {}".format(name)
   SLOW: "Hello %s" % name

3. Use 'in' for substring checking:
   GOOD: 'sub' in string
   OKAY: string.find('sub') != -1

4. Use startswith()/endswith() for prefix/suffix:
   GOOD: string.startswith('prefix')
   OKAY: string[:6] == 'prefix'

5. String methods return new strings (immutable):
   text = "hello"
   text.upper()  # Returns "HELLO" but text is still "hello"
   text = text.upper()  # Need to reassign
""")


# ============================================================================
# 15. COMMON PATTERNS AND IDIOMS
# ============================================================================

print("="*70)
print("COMMON PATTERNS")
print("="*70)

print("\n1. Reverse a string:")
text = "Python"
print(f"   {text} -> {text[::-1]}")

print("\n2. Check if palindrome:")
text = "racecar"
is_palindrome = text == text[::-1]
print(f"   '{text}' is palindrome: {is_palindrome}")

print("\n3. Remove vowels:")
text = "Hello World"
no_vowels = ''.join(c for c in text if c.lower() not in 'aeiou')
print(f"   '{text}' -> '{no_vowels}'")

print("\n4. Count words:")
sentence = "Python is awesome and Python is fun"
word_count = len(sentence.split())
print(f"   '{sentence}'")
print(f"   Word count: {word_count}")

print("\n5. Capitalize each word:")
text = "hello world from python"
capitalized = ' '.join(word.capitalize() for word in text.split())
print(f"   '{text}' -> '{capitalized}'")

print("\n6. Remove duplicates (preserve order):")
text = "programming"
unique = ''.join(dict.fromkeys(text))
print(f"   '{text}' -> '{unique}'")

print("\n7. Repeat string:")
text = "Ha"
repeated = text * 3
print(f"   '{text}' * 3 = '{repeated}'")

print()

print("="*70)
print("END OF STRING MANIPULATION GUIDE")
print("="*70)