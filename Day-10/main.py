"""
PYTHON FILE HANDLING COMPREHENSIVE GUIDE
=========================================
Reading/Writing Files · CSV · JSON
"""

import os
import csv
import json
import shutil
from pathlib import Path
from datetime import datetime


# ============================================================================
# 1. BASIC FILE OPERATIONS
# ============================================================================

print("=" * 70)
print("1. BASIC FILE OPERATIONS")
print("=" * 70)


# --- Writing a file ---
print("\n1a. Writing to a file:")

with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python file handling is easy.\n")
    f.write("This is line 3.\n")

print("  Created: sample.txt")


# --- Reading entire file ---
print("\n1b. Reading an entire file:")

with open("sample.txt", "r") as f:
    content = f.read()

print(f"  Content:\n{content}")


# --- Reading line by line ---
print("1c. Reading line by line:")

with open("sample.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"  Line {i}: {line.rstrip()}")


# --- readlines() vs readline() ---
print("\n1d. readlines() — all lines as a list:")

with open("sample.txt", "r") as f:
    lines = f.readlines()

print(f"  {lines}")

print("\n1e. readline() — one line at a time:")

with open("sample.txt", "r") as f:
    first  = f.readline()
    second = f.readline()

print(f"  First : {first.rstrip()}")
print(f"  Second: {second.rstrip()}")


# --- Appending to a file ---
print("\n1f. Appending to a file:")

with open("sample.txt", "a") as f:
    f.write("This line was appended.\n")
    f.write(f"Timestamp: {datetime.now():%Y-%m-%d %H:%M:%S}\n")

with open("sample.txt", "r") as f:
    print(f"  File now has {len(f.readlines())} lines")


# --- Writing multiple lines with writelines() ---
print("\n1g. writelines():")

lines_to_write = [
    "First item\n",
    "Second item\n",
    "Third item\n",
]

with open("items.txt", "w") as f:
    f.writelines(lines_to_write)

print("  Created: items.txt")


# ============================================================================
# 2. FILE MODES
# ============================================================================

print("\n" + "=" * 70)
print("2. FILE MODES")
print("=" * 70)

modes = """
  MODE  │ DESCRIPTION
  ──────┼──────────────────────────────────────────────────────────────
  "r"   │ Read (default). Error if file doesn't exist.
  "w"   │ Write. Creates file; OVERWRITES if it exists.
  "a"   │ Append. Creates file; adds to end if it exists.
  "x"   │ Exclusive create. Error if file already exists.
  "r+"  │ Read + Write. Error if file doesn't exist.
  "w+"  │ Read + Write. Overwrites existing content.
  "a+"  │ Read + Append.
  "rb"  │ Read Binary  (images, PDFs, executables…)
  "wb"  │ Write Binary
  "ab"  │ Append Binary
"""
print(modes)


# --- Binary mode example ---
print("2a. Binary mode (copy an image-like byte sequence):")

data = bytes(range(256))                        # 256 raw bytes
with open("binary_demo.bin", "wb") as f:
    f.write(data)

with open("binary_demo.bin", "rb") as f:
    read_back = f.read()

print(f"  Wrote and read back {len(read_back)} bytes")


# ============================================================================
# 3. FILE POSITION & SEEKING
# ============================================================================

print("\n" + "=" * 70)
print("3. FILE POSITION & SEEKING")
print("=" * 70)

with open("sample.txt", "r") as f:
    print(f"\n  Position at open : {f.tell()}")
    chunk = f.read(13)
    print(f"  After read(13)   : pos={f.tell()}  read='{chunk}'")

    f.seek(0)                       # Back to start
    print(f"  After seek(0)    : pos={f.tell()}")

    f.seek(0, 2)                    # Seek to end  (whence=2)
    print(f"  After seek(0,2)  : pos={f.tell()}  (= file size in bytes)")


# ============================================================================
# 4. PATHLIB — MODERN PATH HANDLING
# ============================================================================

print("\n" + "=" * 70)
print("4. PATHLIB — MODERN PATH HANDLING")
print("=" * 70)

p = Path("sample.txt")

print(f"\n  Path object   : {p}")
print(f"  Absolute      : {p.resolve()}")
print(f"  Name          : {p.name}")
print(f"  Stem          : {p.stem}")
print(f"  Suffix        : {p.suffix}")
print(f"  Parent        : {p.parent}")
print(f"  Exists?       : {p.exists()}")
print(f"  Is file?      : {p.is_file()}")
print(f"  Is dir?       : {p.is_dir()}")
print(f"  Size (bytes)  : {p.stat().st_size}")

# Reading/writing with Path
p.write_text("Written via Path.write_text()\n")
print(f"\n  Read back     : {p.read_text().strip()}")

# Restore sample.txt
with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python file handling is easy.\n")
    f.write("This is line 3.\n")
    f.write("This line was appended.\n")

# Creating directories
demo_dir = Path("demo_folder")
demo_dir.mkdir(exist_ok=True)
(demo_dir / "nested").mkdir(exist_ok=True)
print(f"\n  Created dir   : {demo_dir}")
print(f"  Children      : {list(demo_dir.iterdir())}")

# Glob patterns
Path("demo_folder/file1.txt").write_text("file1")
Path("demo_folder/file2.txt").write_text("file2")
txt_files = list(Path("demo_folder").glob("*.txt"))
print(f"  *.txt in dir  : {[f.name for f in txt_files]}")


# ============================================================================
# 5. OS MODULE — FILE SYSTEM OPERATIONS
# ============================================================================

print("\n" + "=" * 70)
print("5. OS MODULE — FILE SYSTEM OPERATIONS")
print("=" * 70)

print(f"\n  Current dir   : {os.getcwd()}")
print(f"  Files here    : {[f for f in os.listdir('.') if os.path.isfile(f)][:6]}")

# Check / copy / rename / delete
print(f"\n  sample.txt exists : {os.path.exists('sample.txt')}")
shutil.copy("sample.txt", "sample_copy.txt")
print("  Copied to       : sample_copy.txt")

os.rename("sample_copy.txt", "sample_renamed.txt")
print("  Renamed to      : sample_renamed.txt")

os.remove("sample_renamed.txt")
print("  Deleted         : sample_renamed.txt")

# File metadata
stat = os.stat("sample.txt")
print(f"\n  Size    : {stat.st_size} bytes")
print(f"  Modified: {datetime.fromtimestamp(stat.st_mtime):%Y-%m-%d %H:%M:%S}")


# ============================================================================
# 6. ERROR HANDLING FOR FILES
# ============================================================================

print("\n" + "=" * 70)
print("6. ERROR HANDLING")
print("=" * 70)

def safe_read(filepath):
    """Safely read a file, returning None on any error."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"  ERROR: '{filepath}' not found")
    except PermissionError:
        print(f"  ERROR: No permission to read '{filepath}'")
    except IsADirectoryError:
        print(f"  ERROR: '{filepath}' is a directory, not a file")
    except OSError as e:
        print(f"  OS ERROR: {e}")
    return None


print()
result = safe_read("sample.txt")
print(f"  Read {len(result)} chars from sample.txt")

safe_read("nonexistent.txt")
safe_read("demo_folder")


# ============================================================================
# 7. CSV FILES
# ============================================================================

print("\n" + "=" * 70)
print("7. CSV — COMMA-SEPARATED VALUES")
print("=" * 70)

# --- Writing CSV ---
print("\n7a. Writing CSV with csv.writer:")

students = [
    ["Name",    "Age", "Grade", "City"],
    ["Alice",    20,   "A",     "New York"],
    ["Bob",      21,   "B+",    "Chicago"],
    ["Charlie",  19,   "A-",    "Houston"],
    ["Diana",    22,   "B",     "Phoenix"],
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)           # Write all at once

print("  Created: students.csv")


# --- Reading CSV ---
print("\n7b. Reading CSV with csv.reader:")

with open("students.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"  Header: {header}")
    for row in reader:
        print(f"  Row   : {row}")


# --- DictWriter ---
print("\n7c. Writing CSV with csv.DictWriter (dict per row):")

employees = [
    {"Name": "Alice",   "Department": "Engineering", "Salary": 90000},
    {"Name": "Bob",     "Department": "Marketing",   "Salary": 75000},
    {"Name": "Charlie", "Department": "HR",          "Salary": 65000},
]

with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Name", "Department", "Salary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)

print("  Created: employees.csv")


# --- DictReader ---
print("\n7d. Reading CSV with csv.DictReader (dict per row):")

with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']:<10} | {row['Department']:<15} | ${int(row['Salary']):,}")


# --- CSV with custom delimiter ---
print("\n7e. CSV with custom delimiter (pipe '|'):")

with open("pipe_delimited.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["Product", "Price", "Stock"])
    writer.writerow(["Laptop",  999.99,  50])
    writer.writerow(["Mouse",    29.99, 200])

with open("pipe_delimited.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print(f"  {row}")


# --- CSV with quoting (fields that contain commas) ---
print("\n7f. CSV with quoting (fields containing commas):")

with open("quoted.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Item", "Description", "Price"])
    writer.writerow(["Widget A", "Small, red, round widget", 4.99])
    writer.writerow(["Widget B", "Large, blue, square widget", 12.49])

with open("quoted.csv", "r", newline="", encoding="utf-8") as f:
    print(f.read())


# --- Practical CSV: filter & compute ---
print("7g. Practical: compute average salary from CSV:")

with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    salaries = [int(row["Salary"]) for row in reader]

avg = sum(salaries) / len(salaries)
print(f"  Average salary: ${avg:,.2f}")


# ============================================================================
# 8. JSON FILES
# ============================================================================

print("\n" + "=" * 70)
print("8. JSON — JAVASCRIPT OBJECT NOTATION")
print("=" * 70)


# --- Writing JSON ---
print("\n8a. Writing JSON with json.dump:")

user_profile = {
    "user_id": "U001",
    "name": "Alice Johnson",
    "age": 28,
    "email": "alice@example.com",
    "is_active": True,
    "balance": 1250.75,
    "tags": ["python", "developer", "open-source"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    },
    "login_history": ["2024-01-10", "2024-01-12", "2024-01-15"],
    "extra_field": None
}

with open("user_profile.json", "w", encoding="utf-8") as f:
    json.dump(user_profile, f, indent=4, ensure_ascii=False)

print("  Created: user_profile.json")


# --- Reading JSON ---
print("\n8b. Reading JSON with json.load:")

with open("user_profile.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"  Name    : {loaded['name']}")
print(f"  City    : {loaded['address']['city']}")
print(f"  Tags    : {loaded['tags']}")
print(f"  Balance : ${loaded['balance']:,.2f}")


# --- json.dumps / json.loads (strings, not files) ---
print("\n8c. json.dumps and json.loads (work with strings):")

data = {"x": 10, "y": [1, 2, 3], "active": True}

json_string = json.dumps(data, indent=2)
print(f"  dumps() → string:\n{json_string}")

recovered = json.loads(json_string)
print(f"  loads() → dict : {recovered}")


# --- JSON array of records ---
print("\n8d. JSON array of records:")

products = [
    {"id": 1, "name": "Laptop",  "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Mouse",   "price":  29.99, "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 349.99, "in_stock": False},
]

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2)

with open("products.json", "r", encoding="utf-8") as f:
    loaded_products = json.load(f)

print("  Products in stock:")
for p in loaded_products:
    if p["in_stock"]:
        print(f"    {p['name']:<10} ${p['price']:,.2f}")


# --- Custom JSON serialization ---
print("\n8e. Custom serialization for non-standard types:")

class DateTimeEncoder(json.JSONEncoder):
    """Extend JSONEncoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

event = {
    "event": "User Login",
    "timestamp": datetime.now(),
    "user_id": "U001"
}

json_str = json.dumps(event, cls=DateTimeEncoder, indent=2)
print(f"  Serialized datetime:\n{json_str}")


# --- Pretty-printing JSON ---
print("\n8f. Pretty-printing existing JSON:")

raw_json = '{"name":"Bob","scores":[95,87,92],"active":true}'
parsed   = json.loads(raw_json)
pretty   = json.dumps(parsed, indent=4, sort_keys=True)
print(f"  Pretty:\n{pretty}")


# --- JSON error handling ---
print("\n8g. JSON error handling:")

def safe_json_load(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"  ERROR: '{filepath}' not found")
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON — {e}")
    return None

# Valid file
data = safe_json_load("user_profile.json")
print(f"  Loaded user: {data['name']}")

# Bad JSON written to a temp file
with open("bad.json", "w") as f:
    f.write("{ invalid json !!!")
safe_json_load("bad.json")


# ============================================================================
# 9. PRACTICAL PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("9. PRACTICAL PATTERNS")
print("=" * 70)

# --- Pattern 1: JSON config file ---
print("\n9a. Config file pattern:")

DEFAULT_CONFIG = {
    "theme": "dark",
    "language": "en",
    "max_connections": 10,
    "debug": False
}

def load_config(path="config.json"):
    if not os.path.exists(path):
        save_config(DEFAULT_CONFIG, path)
        return DEFAULT_CONFIG.copy()
    with open(path, "r") as f:
        return json.load(f)

def save_config(config, path="config.json"):
    with open(path, "w") as f:
        json.dump(config, f, indent=4)

config = load_config()
config["theme"] = "light"           # User changes a setting
save_config(config)
print(f"  Config saved. Theme is now: {load_config()['theme']}")


# --- Pattern 2: CSV → JSON conversion ---
print("\n9b. Convert CSV → JSON:")

with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader  = csv.DictReader(f)
    records = [dict(row) for row in reader]

# Cast salary to int
for r in records:
    r["Salary"] = int(r["Salary"])

with open("employees.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

print("  Saved: employees.json")
with open("employees.json") as f:
    print(f"  Content:\n{f.read()}")


# --- Pattern 3: Append rows to CSV safely ---
print("9c. Append-to-CSV pattern:")

def append_to_csv(filepath, row_dict, fieldnames):
    file_exists = os.path.exists(filepath)
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)

fields = ["timestamp", "event", "user"]
append_to_csv("audit_log.csv", {"timestamp": "2024-01-15 09:00", "event": "login",  "user": "alice"}, fields)
append_to_csv("audit_log.csv", {"timestamp": "2024-01-15 09:05", "event": "upload", "user": "alice"}, fields)
append_to_csv("audit_log.csv", {"timestamp": "2024-01-15 09:10", "event": "logout", "user": "alice"}, fields)

with open("audit_log.csv", "r") as f:
    print(f"  Audit log:\n{f.read()}")


# --- Pattern 4: Safe atomic write ---
print("9d. Atomic write (write to temp, then rename):")

def atomic_write_json(data, filepath):
    """Write JSON safely — avoids partial files on crash."""
    tmp = filepath + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, filepath)           # Atomic on most OSes

atomic_write_json({"status": "ok", "version": 2}, "state.json")
print("  state.json written atomically")


# --- Pattern 5: Walk a directory tree ---
print("\n9e. Walk a directory tree:")

for root, dirs, files in os.walk("."):
    # Skip hidden dirs
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    depth   = root.count(os.sep)
    if depth > 1:
        continue
    indent = "  " * depth
    print(f"  {indent}{os.path.basename(root)}/")
    for fname in files:
        print(f"  {indent}  {fname}")


# ============================================================================
# 10. CLEANUP
# ============================================================================

print("\n" + "=" * 70)
print("10. CLEANUP DEMO FILES")
print("=" * 70)

demo_files = [
    "sample.txt", "items.txt", "binary_demo.bin",
    "students.csv", "employees.csv", "pipe_delimited.csv",
    "quoted.csv", "audit_log.csv",
    "user_profile.json", "products.json", "employees.json",
    "bad.json", "config.json", "state.json"
]

removed = []
for fname in demo_files:
    if os.path.exists(fname):
        os.remove(fname)
        removed.append(fname)

# Remove demo folder
if os.path.exists("demo_folder"):
    shutil.rmtree("demo_folder")
    removed.append("demo_folder/")

print(f"\n  Removed {len(removed)} demo files/folders.")

print("\n" + "=" * 70)
print("END OF FILE HANDLING GUIDE")
print("=" * 70)