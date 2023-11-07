import tkinter as tk


def onEntryClick(event):
    """Function to be called when the entry widget is clicked."""
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)  # Delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')


def onFocusout(event):
    """Function to be called when the entry widget loses focus."""
    if entry.get() == '':
        entry.insert(0, placeholder_text)
        entry.config(fg='grey')


root = tk.Tk()

placeholder_text = 'Enter text here'

entry = tk.Entry(root, fg='grey')
entry.insert(0, placeholder_text)
entry.bind('<FocusIn>', onEntryClick)
entry.bind('<FocusOut>', onFocusout)
entry.pack()

entry2 = tk.Entry(root)
entry2.pack()

root.mainloop()
