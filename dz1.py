import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i*4 + j], width=10, height=4, font=("Arial", 12))
        btn.grid(row=i+1, column=j)
        btn.bind("<Button-1>", on_click)

root.mainloop()

