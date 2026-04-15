import tkinter as tk

def create_output_section(root):
    label = tk.Label(root, text="Feedback:", font=("Arial", 14, "bold"))
    label.pack(pady=5)

    output_box = tk.Text(root, height=15, width=80, wrap="word")
    output_box.pack(pady=5)

    return output_box


def display_output(output_box, text):
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)


def show_loading(output_box):
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Processing your CV... Please wait.")


def show_error(output_box, message="Something went wrong"):
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"Error: {message}")
