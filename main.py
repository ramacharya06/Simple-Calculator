import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR= "#25265E"
WHITE  ="#FFFFFF"
BLACK ="#000000"
SMALL_FONT_STYLE = ("Arial",16)
LARGE_FONT_STYLE = ("Arial",40,"bold")
DIGITS_FONT_STYLE = ("Arial",36,"bold")
OFF_WHITE ="#F8FAFF"

class Calculator:
    def __init__(self):
        self.window =tk.Tk()        
        self.window.geometry("344x640")        
        self.window.resizable(False,False)
        self.window.title("Ram's Calc")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        self.digit = {
            "(":(0,1), ")":(0,2),
            7: (1,1), 8: (1,2), 9: (1,3), 
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,1)
        }
        self.operations = {"/":"\u00F7", "*":"x","-":"-","+":"+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_buttons()
        self.create_equals_buttons()

        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label
    
    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit,grid_value in self.digit.items():
            buttons = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth=1,command = lambda x=digit : self.add_to_expression(x))
            buttons.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def append_operator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = " "
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            buttons = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth=1,command=lambda x=operator: self.append_operator(x))
            buttons.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def clear(self):
        self.current_expression=""
        self.total_expression =""
        self.update_total_label()
        self.update_label()

    def create_clear_buttons(self):
        buttons = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth=1,command=self.clear)
        buttons.grid(row=0,column=3,sticky=tk.NSEW)       

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()

    def create_equals_buttons(self):
        buttons = tk.Button(self.buttons_frame, text="=", bg=BLACK, fg=WHITE,font=DIGITS_FONT_STYLE,borderwidth=1, command= self.evaluate)
        buttons.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW) 

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
    
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run() 
    
