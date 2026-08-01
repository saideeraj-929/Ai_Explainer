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
EXPLANATION_FILE="explain.txt"
show=tk.Label(window,text="🤖 AI Code Explainer",font=("Arial",18,"bold")).pack(pady=5)
tk.Label(window,text="Paste Python Code",font=("Arial",12,"bold")).pack(pady=5)
text_entry=tk.Text(height=12,width=70,wrap="word",font=("Consolas",11))
text_entry.pack(pady=5)
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
    except Exception as e:
        explanation_view.delete("1.0", tk.END)
        explanation_view.insert(tk.END, f"Error:\n\n{e}")
def clear():
    text_entry.delete("1.0",tk.END)
    explanation_view.delete("1.0",tk.END)


explain_button=tk.Button(window,text="Explain Code",font=("Arial",12,"bold"),command=explain_code)
explain_button.pack(pady=5)
explain_label=tk.Label(window,text="Explanation",font=("Arial",18,"bold"))
explain_label.pack(pady=5)
explanation_view=tk.Text(height=12,width=70,wrap="word")
explanation_view.pack()
save_button=tk.Button(window,text="Save",font=("Arial",10,"bold"),command=save)
save_button.pack(pady=5,padx=5)
load_button=tk.Button(window,text="Load",font=("Arial",10,"bold"),command=load)
load_button.pack(pady=5,padx=5)
clear_button=tk.Button(window,text="Clear",font=("Arial",10,"bold"),command=clear)
clear_button.pack(pady=5,padx=5)
load()
window.mainloop()
