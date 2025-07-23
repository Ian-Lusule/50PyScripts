```python
# simple_notepad.py
"""A simple notepad application using Tkinter."""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class Notepad:
    def __init__(self, master):
        """Initializes the Notepad application."""
        self.master = master
        master.title("Simple Notepad")

        self.text_area = tk.Text(master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill="both")

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        editmenu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        editmenu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menubar.add_cascade(label="Edit", menu=editmenu)

        master.config(menu=menubar)
        self.filename = None


    def new_file(self):
        """Creates a new file, clearing the text area."""
        self.text_area.delete("1.0", tk.END)
        self.filename = None

    def open_file(self):
        """Opens an existing file."""
        try:
            self.filename = filedialog.askopenfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if self.filename:
                with open(self.filename, "r") as f:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, f.read())
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        """Saves the current file. If no filename, prompts for save as."""
        if self.filename:
            self.save_as_file(self.filename)  # Reuse save_as for existing files
        else:
            self.save_as_file()

    def save_as_file(self, filename=None):
        """Saves the current file as a new file or to the specified filename."""
        if filename is None:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
        if filename:
            try:
                with open(filename, "w") as f:
                    f.write(self.text_area.get("1.0", tk.END))
                self.filename = filename
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()

```