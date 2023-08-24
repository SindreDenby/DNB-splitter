import json
import tkinter as tk
import os
import user_data
from tkinter.simpledialog import askstring

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
        

        self.root = tk.Tk()
        
        self.root.title("DNB Financial Analysis System Configuration Tool")

        self.mainFrame = tk.Frame(self.root, padx=30, pady=30)
        self.mainFrame.grid()

        newTypeBtn = tk.Button(self.mainFrame,
            command=self.add_type,
            text="+",
            width=8
        )
        newTypeBtn.grid(column=0, row=0, sticky='w')
        
        self.listTitles = []
        self.listBoxes = []
        self.listMoveBtns = []
        self.build_listboxes()

        self.root.mainloop()

    def move_stores(self):
        pass

    def add_type(self):
        inp = askstring("New type", "Insert new name:")
        user_data.new_type(inp)
        self.build_listboxes()

    def update_listbox_items(self):
        self.store_types = user_data.read_data()
        for i, typeName in enumerate(self.store_types):
            insert_into_listbox(self.listBoxes[i], self.store_types[typeName])


    def build_listboxes(self):
        for col in zip(self.listTitles, self.listBoxes, self.listMoveBtns):
            for item in col:
                item.destroy()

        self.listTitles = []
        self.listBoxes = []
        self.listMoveBtns = []

        self.store_types = user_data.read_data()
        curCol = 0
        for store_type in self.store_types:
            self.listTitles.append(tk.Label(self.mainFrame,
                text= store_type
            ))
            self.listTitles[-1].grid(row=1, column=curCol)

            self.listBoxes.append(create_listBox(self.mainFrame, 2, curCol))

            self.listMoveBtns.append(tk.Button(self.mainFrame, 
                # command=
                text="Flytt hit"
            ))

            self.listMoveBtns[-1].grid(row=3, column=curCol)

            curCol +=1

        self.update_listbox_items()
        self.root.update()
        
        



def main():
    config_ui()

if __name__ == '__main__':
    main()