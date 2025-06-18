# 📄 File Integrity Checker

A simple and practical Python GUI tool to **monitor file integrity**.  
It uses SHA-256 hashing to detect changes in files and ensure they haven’t been tampered with.

---

## 🚀 Features

- Add and track multiple files
- Calculate and compare file hashes
- Detect modified or missing files
- Save and load hash records (`.json`)
- User-friendly interface built with Tkinter

---

## 🛠️ Requirements

- Python 3.7 or higher
- `tkinter` (included with most Python distributions)
- Uses built-in libraries: `hashlib`, `json`, `os`

---

## 🧪 How It Works

1. Select files you want to monitor.
2. The tool calculates SHA-256 hashes for those files.
3. When you recheck, it compares current file hashes with stored ones.
4. It notifies you if any file has been modified or is missing.

---

## 📦 Usage

### Run the app

```bash
python file_integrity_checker.py
