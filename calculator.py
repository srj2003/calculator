import tkinter as tk
from tkinter import font as tkfont

class DarkRoundedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Dark Rounded Calculator")
        master.geometry("350x500")
        master.configure(bg='#000000')
        master.resizable(False, False)

        self.display_font = tkfont.Font(family="Sans Serif", size=24)
        self.button_font = tkfont.Font(family="Sans Serif", size=18, weight="bold")

        self.main_frame = tk.Frame(master, bg='#000000')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self.main_frame, 
            textvariable=self.display_var, 
            font=self.display_font, 
            justify='right', 
            bd=0, 
            bg='#2f2f2f', 
            fg='#ffffff',
            relief=tk.FLAT,
            insertbackground='#3498db'
        )
        self.display.pack(fill='x', pady=(0, 20), ipady=10)
        
     
        self.button_frame = tk.Frame(self.main_frame, bg='#000000')
        self.button_frame.pack(expand=True, fill='both')

        
        button_configs = [
            ('C', '#e74c3c', self.clear),
            ('(', '#3498db', lambda: self.add_to_display('(')),
            (')', '#3498db', lambda: self.add_to_display(')')),
            ('+', '#3498db', lambda: self.add_to_display('+')),
            ('7', '#2f2f2f', lambda: self.add_to_display('7')),
            ('8', '#2f2f2f', lambda: self.add_to_display('8')),
            ('9', '#2f2f2f', lambda: self.add_to_display('9')),
            ('-', '#3498db', lambda: self.add_to_display('-')),
            ('4', '#2f2f2f', lambda: self.add_to_display('4')),
            ('5', '#2f2f2f', lambda: self.add_to_display('5')),
            ('6', '#2f2f2f', lambda: self.add_to_display('6')),
            ('x', '#3498db', lambda: self.add_to_display('x')),
            ('1', '#2f2f2f', lambda: self.add_to_display('1')),
            ('2', '#2f2f2f', lambda: self.add_to_display('2')),
            ('3', '#2f2f2f', lambda: self.add_to_display('3')),
            ('/', '#3498db', lambda: self.add_to_display('/')),
            ('0', '#2f2f2f', lambda: self.add_to_display('0')),
            ('.', '#2f2f2f', lambda: self.add_to_display('.')),
            ('=', '#2ecc71', self.calculate),
            ('%', '#3498db', lambda: self.add_to_display('%')),
            
        ]
        self.display.bind('<Return>', lambda event: self.calculate())

        row, col = 0, 0
        for (text, color, command) in button_configs:
            btn = tk.Button(
                self.button_frame, 
                text=text, 
                command=command,
                font=self.button_font,
                bg=color, 
                fg='white',
                activebackground=color,
                relief=tk.FLAT,
                borderwidth=0,
                padx=15,
                pady=15,
                bd=0
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(6):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

        
        

    def add_to_display(self, value):
        current = self.display_var.get()
        self.display_var.set(current + value)

    def clear(self):
        self.display_var.set('')

    def calculate(self):
        try:
            
            expression = self.display_var.get().replace('x', '*')
            result = eval(expression)
            self.display_var.set(str(result))
        except Exception:
            self.display_var.set('Error')

def main():
    root = tk.Tk()
    DarkRoundedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()