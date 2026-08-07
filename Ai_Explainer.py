import tkinter as tk
from tkinter import messagebox
import os
from groq import Groq
client = Groq(
  api_key=os.getenv("GROQ_API_KEY")
 )
window=tk.Tk()
window.title("🤖 AI Code Explainer ")
window.geometry("500x600")
window.config(bg="lavender")

BG_COLOR = "#1e1e2e"
TEXT_COLOR = "white"

window.config(bg=BG_COLOR)
EXPLANATION_FILE="explain.txt"
show=tk.Label(window,text="🤖 AI Code Explainer",font=("Arial",18,"bold")).pack(pady=5)
status_label = tk.Label(
    window,
    text="Status: Ready",
    font=("Arial",10),
    bg="white",
    fg="gray"
)

status_label.pack(pady=5)
tk.Label(window,text="Paste Python Code",font=("Arial",12,"bold")).pack(pady=5)
code_frame = tk.Frame(window, bg="lavender")
code_frame.pack(pady=10)

text_entry = tk.Text(
    code_frame,
    height=12,
    width=55,
    wrap="word",
    font=("Consolas",11)
)
code_scroll=tk.Scrollbar(code_frame,
command=text_entry.yview
)
text_entry.configure(
    yscrollcommand=code_scroll.set
)

text_entry.pack(side=tk.LEFT)

code_scroll.pack(side=tk.RIGHT, fill=tk.Y)
def save():
    explain=explanation_view.get("1.0",tk.END)
    with open(EXPLANATION_FILE,"w")as file:
        file.write(explain)
    messagebox.showinfo("Success","Text saved successfuly")
def load():
    try:
        with open(EXPLANATION_FILE,"r")as file:
            explain=file.read()
            explanation_view.delete("1.0", tk.END)
            explanation_view.insert( tk.END,explain)
        messagebox.showinfo("Success","Text loaded successfuly")
    except FileNotFoundError:
        messagebox.showerror("Error",
                "No saved text found"
             )
def explain_code():
    code = text_entry.get("1.0", tk.END).strip()
    if code == "":
        explanation_view.delete("1.0", tk.END)
        explanation_view.insert(tk.END, "Please enter Python code")
        return 
    status_label.config(
    text="Status: 🤖 AI is thinking..."
)
    window.update()

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert Python teacher.\n\n"
                "Explain the given Python code in very simple English.\n\n"
                "Rules:\n"
                "- Explain line by line.\n"
                "- Mention what each line does.\n"
                "- If there is output, show the output.\n"
                "- Use beginner-friendly language.\n"
                "- Return only the explanation."
            )
        },
        {
            "role": "user",
            "content": code
        }
    ]
    try:
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
            )
        explain=response.choices[0].message.content
        explanation_view.delete("1.0",tk.END)
        explanation_view.insert(tk.END,explain)
        status_label.config(
    text="Status: ✅ Completed"
)
    except Exception as e:
        explanation_view.delete("1.0", tk.END)
        explanation_view.insert(tk.END, f"Error:\n\n{e}")
        status_label.config(
    text="Status: ❌ Error"
)
def clear():
    text_entry.delete("1.0",tk.END)
    explanation_view.delete("1.0",tk.END)


explain_label=tk.Label(window,text="Explanation",font=("Arial",18,"bold"))
explain_label.pack(pady=5)
explain_frame = tk.Frame(window,bg="lavender")
explain_frame.pack(pady=10)


explanation_view = tk.Text(
    explain_frame,
    height=12,
    width=55,
    wrap="word"
)


explain_scroll = tk.Scrollbar(
    explain_frame,
    command=explanation_view.yview
)


explanation_view.configure(
    yscrollcommand=explain_scroll.set
)


explanation_view.pack(side=tk.LEFT)

explain_scroll.pack(
    side=tk.RIGHT,
    fill=tk.Y
)
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

explain_button = tk.Button(
    button_frame,
    text="🤖 Explain",
    width=12,
    font=("Arial",10,"bold"),
    bg="#28a745",
    fg="white",
    relief="flat",
    command=explain_code
)
explain_button.grid(row=0,column=0,padx=5)

save_button = tk.Button(
    button_frame,
    text="💾 Save",
    width=10,
    font=("Arial",10,"bold"),
    bg="#007bff",
    fg="white",
    relief="flat",
    command=save
)
save_button.grid(row=0,column=1,padx=5)

load_button = tk.Button(
    button_frame,
    text="📂 Load",
    width=10,
    font=("Arial",10,"bold"),
    bg="#ff9800",
    fg="white",
    relief="flat",
    command=load
)
load_button.grid(row=0,column=2,padx=5)

clear_button = tk.Button(
    button_frame,
    text="🗑 Clear",
    width=10,
    font=("Arial",10,"bold"),
    bg="#dc3545",
    fg="white",
    relief="flat",
    command=clear
)
clear_button.grid(row=0,column=3,padx=5)

load()
window.mainloop()
