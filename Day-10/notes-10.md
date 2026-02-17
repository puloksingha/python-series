# Python File Handling (Day 10)

Comprehensive notes on file operations, file modes, pathlib, CSV, JSON, error handling, and practical patterns.

---

## 1. Basic File Operations

### Writing to a file
- Use `open(filename, "w")` to create/overwrite a file.
- Use `write()` to add text.

```python
with open("sample.txt", "w") as f:
	f.write("Hello, World!\n")
	f.write("Python file handling is easy.\n")
```

### Reading a file
- `read()` reads full content as a single string.
- `readline()` reads one line at a time.
- `readlines()` reads all lines into a list.

```python
with open("sample.txt", "r") as f:
	content = f.read()

with open("sample.txt", "r") as f:
	first_line = f.readline()

with open("sample.txt", "r") as f:
	all_lines = f.readlines()
```

### Reading line-by-line efficiently

```python
with open("sample.txt", "r") as f:
	for i, line in enumerate(f, start=1):
		print(i, line.rstrip())
```

### Appending to existing file
- Use `"a"` mode to add content at the end.

```python
from datetime import datetime

with open("sample.txt", "a") as f:
	f.write("This line was appended.\n")
	f.write(f"Timestamp: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
```

### Writing multiple lines

```python
lines_to_write = ["First item\n", "Second item\n", "Third item\n"]
with open("items.txt", "w") as f:
	f.writelines(lines_to_write)
```

---

## 2. File Modes Cheat Sheet

| Mode | Meaning |
|------|---------|
| `r` | Read (default), error if not found |
| `w` | Write, creates file, overwrites existing content |
| `a` | Append, creates file if missing |
| `x` | Create only, error if file exists |
| `r+` | Read + write, file must exist |
| `w+` | Read + write, overwrite existing |
| `a+` | Read + append |
| `rb` / `wb` / `ab` | Binary read/write/append |

### Binary mode example

```python
data = bytes(range(256))
with open("binary_demo.bin", "wb") as f:
	f.write(data)

with open("binary_demo.bin", "rb") as f:
	read_back = f.read()
```

---

## 3. File Position and Seeking

- `tell()` gives current file pointer position.
- `seek(offset, whence)` moves pointer.
  - `whence=0`: beginning
  - `whence=1`: current position
  - `whence=2`: end of file

```python
with open("sample.txt", "r") as f:
	print(f.tell())
	chunk = f.read(13)
	print(f.tell())
	f.seek(0)
	f.seek(0, 2)
```

---

## 4. Pathlib (Modern Path Handling)

`pathlib.Path` gives a cleaner, object-oriented way to work with paths.

```python
from pathlib import Path

p = Path("sample.txt")
print(p.resolve())
print(p.name, p.stem, p.suffix)
print(p.exists(), p.is_file(), p.is_dir())
print(p.stat().st_size)
```

### Read/Write with Path

```python
p.write_text("Written via Path.write_text()\n")
text = p.read_text()
```

### Directory operations and glob

```python
demo_dir = Path("demo_folder")
demo_dir.mkdir(exist_ok=True)
(demo_dir / "nested").mkdir(exist_ok=True)

Path("demo_folder/file1.txt").write_text("file1")
Path("demo_folder/file2.txt").write_text("file2")
txt_files = list(Path("demo_folder").glob("*.txt"))
```

---

## 5. OS + shutil File System Operations

Useful functions demonstrated:
- `os.getcwd()` current working directory
- `os.listdir()` list entries
- `os.path.exists()` existence check
- `shutil.copy()` copy file
- `os.rename()` rename file
- `os.remove()` delete file
- `os.stat()` metadata (size, modified time)

```python
import os
import shutil

shutil.copy("sample.txt", "sample_copy.txt")
os.rename("sample_copy.txt", "sample_renamed.txt")
os.remove("sample_renamed.txt")
```

---

## 6. Error Handling for File Operations

A safe file reader should handle common exceptions gracefully.

```python
def safe_read(filepath):
	try:
		with open(filepath, "r") as f:
			return f.read()
	except FileNotFoundError:
		print(f"ERROR: '{filepath}' not found")
	except PermissionError:
		print(f"ERROR: No permission to read '{filepath}'")
	except IsADirectoryError:
		print(f"ERROR: '{filepath}' is a directory, not a file")
	except OSError as e:
		print(f"OS ERROR: {e}")
	return None
```

---

## 7. CSV Files

### Writing CSV with `csv.writer`

```python
import csv

students = [
	["Name", "Age", "Grade", "City"],
	["Alice", 20, "A", "New York"],
	["Bob", 21, "B+", "Chicago"],
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)
	writer.writerows(students)
```

### Reading CSV with `csv.reader`

```python
with open("students.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	for row in reader:
		print(row)
```

### Dict-based CSV (`DictWriter` / `DictReader`)

```python
employees = [
	{"Name": "Alice", "Department": "Engineering", "Salary": 90000},
	{"Name": "Bob", "Department": "Marketing", "Salary": 75000},
]

with open("employees.csv", "w", newline="", encoding="utf-8") as f:
	fieldnames = ["Name", "Department", "Salary"]
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(employees)
```

### Custom delimiter and quoting

```python
with open("pipe_delimited.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f, delimiter="|")
	writer.writerow(["Product", "Price", "Stock"])

with open("quoted.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f, quoting=csv.QUOTE_ALL)
	writer.writerow(["Item", "Description", "Price"])
```

### Practical CSV computation

```python
with open("employees.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.DictReader(f)
	salaries = [int(row["Salary"]) for row in reader]

avg = sum(salaries) / len(salaries)
```

---

## 8. JSON Files

### Write JSON (`json.dump`) and read JSON (`json.load`)

```python
import json

user_profile = {
	"user_id": "U001",
	"name": "Alice Johnson",
	"age": 28,
	"is_active": True,
	"balance": 1250.75,
	"tags": ["python", "developer"],
	"address": {"city": "New York"},
	"extra_field": None,
}

with open("user_profile.json", "w", encoding="utf-8") as f:
	json.dump(user_profile, f, indent=4, ensure_ascii=False)

with open("user_profile.json", "r", encoding="utf-8") as f:
	loaded = json.load(f)
```

### JSON strings (`dumps` / `loads`)

```python
data = {"x": 10, "y": [1, 2, 3], "active": True}
json_string = json.dumps(data, indent=2)
recovered = json.loads(json_string)
```

### JSON list of records

```python
products = [
	{"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
	{"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
]

with open("products.json", "w", encoding="utf-8") as f:
	json.dump(products, f, indent=2)
```

### Custom serialization (datetime)

```python
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.isoformat()
		return super().default(obj)

event = {"event": "User Login", "timestamp": datetime.now()}
json_str = json.dumps(event, cls=DateTimeEncoder, indent=2)
```

### JSON error handling

```python
def safe_json_load(filepath):
	try:
		with open(filepath, "r", encoding="utf-8") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f"ERROR: '{filepath}' not found")
	except json.JSONDecodeError as e:
		print(f"ERROR: Invalid JSON — {e}")
	return None
```

---

## 9. Practical Patterns from the Script

### 9a. JSON config file pattern
- Keep defaults in `DEFAULT_CONFIG`.
- Auto-create config if it does not exist.
- Provide `load_config()` and `save_config()` helpers.

```python
DEFAULT_CONFIG = {
	"theme": "dark",
	"language": "en",
	"max_connections": 10,
	"debug": False,
}
```

### 9b. CSV → JSON conversion

```python
with open("employees.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.DictReader(f)
	records = [dict(row) for row in reader]

for r in records:
	r["Salary"] = int(r["Salary"])

with open("employees.json", "w", encoding="utf-8") as f:
	json.dump(records, f, indent=2)
```

### 9c. Append-to-CSV safely
- Write header only when file does not exist.

```python
def append_to_csv(filepath, row_dict, fieldnames):
	file_exists = os.path.exists(filepath)
	with open(filepath, "a", newline="", encoding="utf-8") as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		if not file_exists:
			writer.writeheader()
		writer.writerow(row_dict)
```

### 9d. Atomic JSON write
- Write to temporary file first.
- Replace target using `os.replace()` to reduce corruption risk.

```python
def atomic_write_json(data, filepath):
	tmp = filepath + ".tmp"
	with open(tmp, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2)
	os.replace(tmp, filepath)
```

### 9e. Directory tree walk

```python
for root, dirs, files in os.walk("."):
	dirs[:] = [d for d in dirs if not d.startswith(".")]
	depth = root.count(os.sep)
	if depth > 1:
		continue
```

---

## 10. Cleanup Pattern

The script keeps a list of demo files/folders and removes them at the end:
- Prevents clutter
- Makes reruns clean and repeatable

```python
demo_files = [
	"sample.txt", "items.txt", "binary_demo.bin",
	"students.csv", "employees.csv", "pipe_delimited.csv",
	"quoted.csv", "audit_log.csv",
	"user_profile.json", "products.json", "employees.json",
	"bad.json", "config.json", "state.json",
]
```

---

## Key Takeaways

- Prefer context managers (`with open(...)`) for safe automatic file closing.
- Choose file mode carefully (`w` overwrites, `a` appends, binary modes for bytes).
- Use `pathlib.Path` for cleaner and more readable path logic.
- Use `csv` and `json` modules instead of manual string parsing.
- Add robust exception handling for production-safe file operations.
- Use practical patterns: config files, CSV↔JSON conversion, atomic writes, and cleanup.
