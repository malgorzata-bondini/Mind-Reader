import tkinter as tk
from tkinter import ttk, messagebox
is_processing = False

def another_round():
    global is_processing
    is_processing = False
    output_label.grid_remove()
    success_label.grid_remove()
    another_button.grid_remove()
    end_button.grid_remove()
    progress_bar['value'] = 0
    status_label.config(text="Awaiting your input...")
    status_label.grid_remove()
    input_entry.delete(0, tk.END)
    input_label.grid()
    input_entry.grid()
    read_button.grid()

def end_application():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

def read_my_mind():
    global is_processing
    if is_processing:
        return

    number = input_entry.get()
    if not number.isdigit() or not (1 <= int(number) <= 20):
        output_label.config(
            text="Please enter a number between 1 and 20!",
            fg="#6A8EAE",
            font=("Arial", 14, "bold")
        )
        output_label.grid()
        return

    is_processing = True
    input_label.grid_remove()
    input_entry.grid_remove()
    read_button.grid_remove()

    # Progress bar
    status_label.config(text="Starting...")
    status_label.grid()
    progress_bar.grid()

    output_label.config(text="")
    output_label.grid_remove()
    success_label.grid_remove()

    steps = [
        "Calculating probabilities...",
        "Decoding thoughts...",
        "Analyzing brainwaves...",
        "Scanning memories...",
        "Interpreting signals...",
        "Finalizing prediction..."
    ]

    total_steps = len(steps)
    substeps_per_step = 20
    total_substeps = total_steps * substeps_per_step
    progress_increment = 100 / total_substeps

    current_step = {'index': 0, 'subindex': 0}

    def update_progress():
        global is_processing
        if current_step['index'] < total_steps:
            if current_step['subindex'] < substeps_per_step:
                new_value = progress_bar['value'] + progress_increment
                if new_value > 100:
                    new_value = 100
                progress_bar['value'] = new_value
                current_step['subindex'] += 1
                root.after(50, update_progress)
            else:
                status_label.config(text=steps[current_step['index']])
                current_step['index'] += 1
                current_step['subindex'] = 0
                if current_step['index'] == total_steps:
                    root.after(3000, update_progress)
                else:
                    root.after(1000, update_progress)
        else:
            progress_bar['value'] = 100
            status_label.config(text="Success!")
            success_label.config(
                text="Success!",
                fg="green",
                font=("Arial", 18, "bold")
            )
            success_label.grid()
            output_label.config(
                text=f"You're thinking of the number {number}!",
                fg="#6A8EAE",
                font=("Arial", 14, "bold")
            )
            output_label.grid()
            another_button.grid()
            end_button.grid()
            progress_bar.grid_remove()
            status_label.grid_remove()
            is_processing = False

    update_progress()

def on_enter(event):
    read_my_mind()
def on_closing():
    end_application()

root = tk.Tk()
root.title("Mind Reader 💀")
root.geometry("500x400")
root.configure(bg="white")
root.resizable(False, False)
root.bind('<Return>', on_enter)
root.bind('<Escape>', lambda event: end_application())
root.protocol("WM_DELETE_WINDOW", on_closing)
style = ttk.Style()
style.theme_use('clam')

style.configure(
    "TButton",
    font=("Arial", 14, "bold"),
    padding=10,
    relief="raised",
    borderwidth=3,
    background="#5a99c8",
    foreground="#ffffff"
)
style.map("TButton",
          background=[("active", "#4a8aa3")],
          foreground=[("active", "#ffffff")])
style.configure("TLabel", font=("Arial", 14, "bold"), background="white", foreground="#6A8EAE")
style.configure("TEntry", font=("Arial", 14), padding=5)

# Progress bar
style.configure("green.Horizontal.TProgressbar", troughcolor="#e0e0e0", 
                background="#4caf50", thickness=30)
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

# Header
header_frame = tk.Frame(main_frame, bg="#1976d2", bd=2, relief="groove")
header_frame.pack(pady=(15, 30))
header_subframe = tk.Frame(header_frame, bg="#1976d2")
header_subframe.pack(padx=10, pady=10)

# Skull emoji
skull_label = tk.Label(
    header_subframe, 
    text="💀", 
    font=("Arial", 30),
    bg="#1976d2",
    fg="#ffffff"
)
skull_label.pack(side="left", padx=(5, 10), pady=(0, 10))

header_label = tk.Label(
    header_subframe, 
    text="Mind Reader", 
    font=("Arial", 34, "bold"),
    bg="#1976d2", 
    fg="#ffffff"
)
header_label.pack(side="left")
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack()

input_label = ttk.Label(content_frame, text="Think of a number between 1 and 20:")
input_label.grid(row=0, column=0, pady=(5, 3), padx=10)
input_entry = ttk.Entry(content_frame, width=10, justify='center')
input_entry.grid(row=1, column=0, pady=3, padx=10)

read_button = ttk.Button(content_frame, text="Read My Mind", command=read_my_mind)
read_button.grid(row=2, column=0, pady=8, padx=10)

status_label = tk.Label(
    content_frame, 
    text="Awaiting your input...",
    font=("Arial", 14),
    fg="#555555",
    bg="white"
)
status_label.grid(row=3, column=0, pady=8, padx=10)
status_label.grid_remove()

progress_bar = ttk.Progressbar(
    content_frame, 
    style="green.Horizontal.TProgressbar",
    orient="horizontal", 
    length=250,
    mode="determinate"
)
progress_bar.grid(row=4, column=0, pady=8, padx=10)
progress_bar.grid_remove()

success_label = tk.Label(
    content_frame, 
    text="", 
    font=("Arial", 20, "bold"),
    fg="green",
    bg="white"
)
success_label.grid(row=5, column=0, pady=4, padx=10)
success_label.grid_remove()

output_label = tk.Label(
    content_frame, 
    text="", 
    font=("Arial", 14, "bold"),
    fg="#6A8EAE",
    bg="white"
)
output_label.grid(row=6, column=0, pady=8, padx=10)
output_label.grid_remove()

another_button = ttk.Button(content_frame, text="✅ Another Round", command=another_round)
another_button.grid(row=7, column=0, pady=8, padx=10)
another_button.grid_remove()

end_button = ttk.Button(content_frame, text="❌ End", command=end_application)
end_button.grid(row=8, column=0, pady=8, padx=10)
end_button.grid_remove()

# Center
for i in range(9):
    content_frame.grid_rowconfigure(i, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
