# File Integrity Checker
# Developed with user-friendly design and practicality in mind

import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json

class FileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")
        self.file_hashes = {}
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, sticky="nsew")

        # Buttons for various actions
        ttk.Button(frame, text="Add Files", command=self.add_files).grid(row=0, column=0, sticky="ew", pady=5)
        ttk.Button(frame, text="Check Integrity", command=self.check_files).grid(row=1, column=0, sticky="ew", pady=5)
        ttk.Button(frame, text="Save Hash Data", command=self.save_hashes).grid(row=2, column=0, sticky="ew", pady=5)
        ttk.Button(frame, text="Load Hash Data", command=self.load_hashes).grid(row=3, column=0, sticky="ew", pady=5)

        # Output display
        self.output_box = tk.Text(frame, height=12, width=60)
        self.output_box.grid(row=4, column=0, pady=10)

    def calculate_file_hash(self, file_path):
        # Calculates the SHA-256 hash of the given file
        hash_object = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_object.update(chunk)
        return hash_object.hexdigest()

    def add_files(self):
        # Let the user pick files to monitor
        selected_files = filedialog.askopenfilenames()
        for file_path in selected_files:
            file_hash = self.calculate_file_hash(file_path)
            self.file_hashes[file_path] = file_hash
            self.output_box.insert(tk.END, f"Added: {file_path}\n")

    def check_files(self):
        # Compare current hashes with stored ones
        report = []
        for path, stored_hash in self.file_hashes.items():
            if not os.path.exists(path):
                report.append(f"[MISSING] {path}")
                continue

            current_hash = self.calculate_file_hash(path)
            if current_hash != stored_hash:
                report.append(f"[CHANGED] {path}")
            else:
                report.append(f"[OK] {path}")

        self.output_box.insert(tk.END, "\n".join(report) + "\n")

    def save_hashes(self):
        # Save the hashes to a JSON file
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.file_hashes, file, indent=4)
            messagebox.showinfo("Done", "Hashes saved successfully.")

    def load_hashes(self):
        # Load the hashes from a JSON file
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                self.file_hashes = json.load(file)
            messagebox.showinfo("Loaded", "Hashes loaded successfully.")

if __name__ == '__main__':
    root = tk.Tk()
    app = FileIntegrityChecker(root)
    root.mainloop()
