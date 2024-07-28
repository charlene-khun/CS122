import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        self.display = tk.Entry(root, width=20, font=('Arial', 18))
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('%', 5, 0), ('.', 5, 1)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

        self.root.bind('<Return>', self.calculate)
        self.root.bind('<KP_Enter>', self.calculate)
        self.root.bind('<Key>', self.on_key_press)
        
        self.last_button = None
        self.last_char = None

    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, font=('Arial', 14), width=5, height=2,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char == '+' and self.last_button == '+':
            pass  # Ignore consecutive '+'
        elif char == '-' and self.last_button == '-':
            pass  # Ignore consecutive '-'
        elif char == '*' and self.last_button == '*':
            pass  # Ignore consecutive '*'
        elif char == '/' and self.last_button == '/':
            pass # Ignore consecutive '/'
        elif char == '.' and self.last_button == '.':
            pass  # Ignore consecutive decimal points
        else:
            self.display.insert(tk.END, char)
        self.last_button = char

    def calculate(self, event=None):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
    
    def on_key_press(self, event):
        char = event.char
        if char == '=':
            display_text = self.display.get()
            if char in display_text:
                index = display_text.rindex(char)
                self.display.delete(index, tk.END)
            return 'break'  # Ignore the equals key
        if char in ('+', '-', '*', '/', '.') and self.last_char == char:
            display_text = self.display.get()
            if char in display_text:
                index = display_text.rindex(char)
                self.display.delete(index, tk.END)
            return 'break'  # Ignore consecutive operators
        self.last_char = char
    
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


