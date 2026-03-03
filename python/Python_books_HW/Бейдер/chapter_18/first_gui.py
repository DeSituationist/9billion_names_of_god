import tkinter as tk
windows = tk.Tk()
greeting = tk.Label(text = 'Hello, Tkinter',
    foreground='white',
    background='black',
    width=10,
    height=10
)
greeting.pack()
button = tk.Button(
    text='Click me',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)
button.pack()
label = tk.Label(text='Name')
entry = tk.Entry()
entry.insert(0, 'Write here')
label.pack()
entry.pack()
name = entry.get()
print(name)
windows.mainloop()