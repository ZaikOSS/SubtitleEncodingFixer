import tkinter as tk
from tkinter import filedialog, messagebox
import os

def fix_subtitle_encoding(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='windows-1256') as infile:
            content = infile.read()
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        messagebox.showinfo("Success", f"Subtitle encoding fixed successfully!\nSaved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select Subtitle File",
        filetypes=[("Subtitle Files", "*.srt *.txt *.sub *.ass *.ssa *.vtt"), ("All Files", "*.*")]
    )
    if file_path:
        input_path_var.set(file_path)  # Display the selected file path in the GUI

def process_file():
    input_file = input_path_var.get()
    if not input_file:
        messagebox.showwarning("Warning", "Please select a subtitle file.")
        return

    # Generate the output file name by appending "_fixed"
    output_file = os.path.splitext(input_file)[0] + "_fixed.srt"
    fix_subtitle_encoding(input_file, output_file)

# Create the GUI window
app = tk.Tk()
app.title("Subtitle Encoding Fixer")
app.geometry("500x200")

# Input file selection
tk.Label(app, text="Select Subtitle File:").pack(pady=10)
input_path_var = tk.StringVar()  # Variable to store the selected file path
tk.Entry(app, textvariable=input_path_var, width=50, state="readonly").pack(pady=5)
tk.Button(app, text="Browse", command=select_file).pack(pady=5)

# Process button
tk.Button(app, text="Fix Encoding", command=process_file, bg="green", fg="white").pack(pady=20)

# Start the main loop
app.mainloop()
