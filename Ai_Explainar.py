import tkinter as tk
window=tk.Tk()
window.title("🤖 AI Code Explainer ")
window.geometry("500x600")
window.config(bg="lavender")
show=tk.Label(window,text="🤖 AI Code Explainer",font=("Arial",18,"bold")).pack(pady=5)
tk.Label(window,text="Paste Python Code",font=("Arial",12,"bold")).pack(pady=5)
text_entry=tk.Text(height=12,width=70,wrap="word",font=("Consolas",11))
text_entry.pack(pady=5)
def explain_code():
    pass
def save():
    pass
def load():
    pass
def clear():
    pass

explain_button=tk.Button(window,text="Explain Code",font=("Arial",12,"bold"))
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
window.mainloop()
