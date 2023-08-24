import json
import tkinter as tk
import os
import user_data

def insert_into_listbox(listbox: tk.Listbox, list):
    listbox.delete(0, tk.END)

    for i in list:
        listbox.insert(tk.END, i)

def create_listBox(box, row, col):
    listboxFrame = tk.Frame(box)
    listboxFrame.grid(row=row, column=col)

    listbox = tk.Listbox(listboxFrame, width=30, height=30, selectmode='extended')

    listbox.pack(side = tk.LEFT, fill = tk.BOTH)

    scrollbar = tk.Scrollbar(listboxFrame)

    scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        
    listbox.config(yscrollcommand = scrollbar.set)

    scrollbar.config(command = listbox.yview)

    return listbox

class config_ui:
    def __init__(self):
        self.store_types = user_data.read_data()

        root = tk.Tk()
        
        root.title("DNB Financial Analysis System Configuration Tool")

        mainFrame = tk.Frame(root, padx=30, pady=30)
        mainFrame.grid()

        curCol = 0

        self.listBoxes = []
        for store_type in self.store_types:
            tk.Label(mainFrame,
                text= store_type
            ).grid(row=1, column=curCol)

            self.listBoxes.append(create_listBox(mainFrame, 2, curCol))

            tk.Button(mainFrame, 
                # command=
                text="Flytt hit"
            ).grid(row=3, column=curCol)
        root.mainloop()


def main():
    config_ui()

if __name__ == '__main__':
    main()