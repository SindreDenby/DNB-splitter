from dataclasses import dataclass
import tkinter as tk
from tkinter import filedialog, ttk
import user_data
import xlsx_splitter
import tooltip
import config
import dnb_icon

@dataclass
class hub_UI:
    file_location: str = ""
    save_location: str = ""

    def __post_init__(self):
        root = tk.Tk()
        
        root.title("DNB Financial Analysis System")
        # dnb_icon.set_base64_icon(dnb_icon.icon ,root)
        mainFrame = tk.Frame(root, padx=30, pady=30)
        mainFrame.grid()

        setFileFrame = tk.Frame(mainFrame)
        setFileFrame.grid(row=0, column=0, columnspan= 2)
        setFileFrame.grid()


        ttk.Label(setFileFrame, text=".xlsx fil:").grid(row=0, column=0)

        self.fileInput = ttk.Entry(setFileFrame, justify=tk.RIGHT, width=40)
        self.fileInput.grid(row=0, column=1)

        ttk.Button(setFileFrame,
            text="...",
            command=self.set_file_location,
            width=6
        ).grid(row=0, column=2)

        ttk.Label(setFileFrame, text="Lagres som:").grid(row=1, column=0)

        self.saveDirInput = ttk.Entry(setFileFrame, justify=tk.RIGHT, width=40)
        self.saveDirInput.grid(row=1, column=1)

        ttk.Button(setFileFrame,
            text="...",
            command=self.set_save_location,
            width=6
        ).grid(row=1, column=2)

        curRow = 2
        btns = []
        for procedure in xlsx_splitter.procedures :
            btns.append(
                ttk.Button(mainFrame,
                    text=procedure.btn,
                    command= lambda: procedure.func(self.file_location, self.save_location),
                    width=17
                )
            )
            btns[len(btns) - 1].grid(row=curRow, column=0)
            tooltip.create(btns[len(btns) - 1], procedure.desc)
            curRow += 1

        ttk.Button(mainFrame,
            text="Velg salgs typer",
            command=config.main,
            width=30,
            # bg="#4287f5"
        ).grid(row=100, column=0, columnspan=2)

        root.mainloop()

    def set_file_location(self):
        self.file_location = filedialog.askopenfilename(
            defaultextension=".xlsx",
            filetypes=(('Microsoft Excel File', '*.xlsx'), ("All Files", "*.*"))
        )

        if self.file_location != "":
            self.fileInput.delete(0, tk.END)
            self.fileInput.insert(0, self.file_location)

    def set_save_location(self):
        self.save_location = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=(('Microsoft Excel file', '*.xlsx'), ("All Files", "*.*"))
        )
        
        if self.save_location != "":
            self.saveDirInput.delete(0, tk.END)
            self.saveDirInput.insert(0, self.save_location)


def main():
    user_data.data_setup()
    UI = hub_UI()
    

if __name__ == '__main__':
    main()