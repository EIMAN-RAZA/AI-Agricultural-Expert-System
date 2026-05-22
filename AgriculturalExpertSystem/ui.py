# ui.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from inference_engine import infer

def create_ui():
    def on_submit():
        symptom_key = entry.get().strip().lower().replace(" ", "_")
        result = infer(symptom_key)

        output_box.configure(state='normal')  # Make text box editable
        output_box.delete("1.0", tk.END)  # Clear previous output

        if result["Diagnosis"] != "Unknown":
            output = (
                f"🌾 DIAGNOSIS:\n"
                f"{result['Diagnosis']}\n\n"
                f"🧠 EXPLANATION:\n"
                f"{result['Explanation']}\n\n"
                f"💊 TREATMENT:\n"
                f"{result['Treatment']}\n"
            )
        else:
            output = (
                "⚠ Symptom not found in the system.\n"
                "Please consult an agriculture expert.\n"
            )

        output_box.insert(tk.END, output)
        output_box.configure(state='disabled')  # Make text box read-only

    # 🌿 Main Window
    window = tk.Tk()
    window.title("🌾 Agricultural Expert System")
    window.geometry("600x500")
    window.configure(bg="#f0f8ff")

    # Title Label
    title_label = ttk.Label(window, text="Agricultural Expert System",
                            font=("Helvetica", 18, "bold"), foreground="#2f4f4f")
    title_label.pack(pady=20)

    # Instruction Label
    ttk.Label(window, text="Enter Symptom (e.g., yellow spots, holes in leaves):",
              font=("Helvetica", 12)).pack()

    # Input Field
    entry = ttk.Entry(window, width=50, font=("Helvetica", 12))
    entry.pack(pady=10)

    # Diagnose Button
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=6)
    diagnose_button = ttk.Button(window, text="🔍 Diagnose", command=on_submit)
    diagnose_button.pack(pady=10)

    # Output Box
    output_box = tk.Text(window, height=15, width=70, font=("Courier New", 12),
                         wrap=tk.WORD, bg="#fdfdfd", borderwidth=2, relief=tk.GROOVE)
    output_box.pack(padx=10, pady=20)
    output_box.configure(state='disabled')  # Initially not editable

    window.mainloop()