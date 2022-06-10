from tkinter import *
import cmath

Main_window = Tk()
Main_window.configure(bg="#202020")
#Main_window.iconbitmap(r"C:\Users\admin\Desktop")


lis_values, lis_operations = [], []
final_value = 0
Error_case = 0
Func_case =  0
Stat_window = None

tuple_font1=("Lucida Bright",10,"bold")
tuple_font=("Lucida Bright",12,"bold")

def Operation_func(operation = None):
    global  Error_case
    try:
        imag = imag_part.get()
        real = real_part.get()
        if not real:
            real = 0
        else:
            real = float(real)
        if not imag:
            imag = 0
        else:
            imag = float(imag)

    except ValueError:
        label_result.config(text="Invalid input")
        real_part.delete(0, END)
        imag_part.delete(0, END)
        Error_case = 1

    else:
        z = complex(real, imag)
        real_part.delete(0, END)
        imag_part.delete(0, END)
        lis_values.append(z)

        if operation:
            lis_operations.append(operation)
            pass

def Evaluate():
    global final_value
    global  Error_case
    final_value = 0
    Operation_func()
    if Error_case == 0:
        while True:
            if len(lis_operations) == 0:
                break

            elif lis_operations[0] == "+":
                lis_values[0] = lis_values[0] + lis_values[1]
                del lis_values[1]

            elif lis_operations[0] == "-":
                lis_values[0] = lis_values[0] - lis_values[1]
                del lis_values[1]

            elif lis_operations[0] == "/":
                try:
                    lis_values[0] = lis_values[0] / lis_values[1]
                except ZeroDivisionError:
                    label_result.config(text="Division by zero is not possible")
                    Error_case = 1
                    break
                else:
                    del lis_values[1]

            elif lis_operations[0] == "*":
                lis_values[0] = lis_values[0] * lis_values[1]
                del lis_values[1]

            lis_operations.pop(0)
        if Error_case == 0:
            final_value = lis_values[0]
            if (final_value.imag == 0):
                final_value = final_value.real
            label_result.config(text=final_value)


def Clear():
    global final_value
    global Func_case
    global  Error_case
    if (Func_case == 1 ):
        label_result.config(text=final_value)
        Func_case = 0

    else:
        global lis_values, lis_operations
        lis_values, lis_operations = [], []
        final_value = 0
        label_result.config(text=final_value)
        Error_case = 0


def Argument():
    global Func_case
    phase = round(cmath.phase(final_value), 3) 
    if final_value:
        label_result.config(text=("arg(" + str(final_value) + ") = " + str(phase)+ "rad"))
        Func_case = 1

    else:
        return

def Modulus():
    global Func_case
    mod = round(abs(final_value), 3)
    if final_value:
        label_result.config(text=("|" + str(final_value) + "| = " + str(mod)))
        Func_case = 1

    else:
        return
def Conj():
    global final_value
    global lis_values
    if final_value:
        final_value = final_value.conjugate()
        lis_values = [final_value]
        label_result.config(text=final_value)

    else:
        pass

def Solve_by_stat():
    global Stat_window
    if not Stat_window:
        global stat_val
        stat_val = 0
        Stat_window = Toplevel()
        Stat_window.title("Solve using expression")
        
    else:
        Stat_window.deiconify()

    def Solve():
        exp = Stat_Entry.get()
        global stat_val
        if exp:
            stat_val = eval(exp)
            label_result_stat.config(text=stat_val)
            Stat_Entry.delete(0, END)
        else:
            pass

    def Pass_to_main():
        global final_value
        global lis_values
        if stat_val:
            final_value = stat_val
        label_result.config(text=final_value)
        lis_values = [final_value]
        Stat_window.iconify()

    def Clear_stat():
        global stat_val
        stat_val = 0
        label_result_stat.config(text=stat_val)
        Stat_Entry.delete(0, END)

    def close():
        global Stat_window
        Stat_window.destroy()
        Stat_window = None        
      

    Stat_Entry = Entry(Stat_window, width=40, bd =5)
    Stat_Entry.grid(row=0, column=0, columnspan=3,pady=5)

    button_solve = Button(Stat_window, width=5, text="Solve",command=Solve)
    button_solve.grid(row=1, column=0, pady=5)

    button_clear_stat = Button(Stat_window, text="Clear", command=Clear_stat, width=5)
    button_clear_stat.grid(row=1, column=1, pady=5)

    pass_button = Button(Stat_window, width=20, text="Pass value to main window", command=Pass_to_main)
    pass_button.grid(row=1,column=2, pady=5)

    label_result_stat = Label(Stat_window, width=30, height=1, text=stat_val, bg="#C9C7C7")
    label_result_stat.grid(row=2, column=0, columnspan=3, pady=5)
    
    Stat_window.protocol("WM_DELETE_WINDOW", close)

Main_window.title('Complex number calculator')

label2 = Label(Main_window, text="Real part", width=15, height=2, font=tuple_font, bg="#202020", foreground="#75E9FC")
label2.grid(row=0, columnspan=1, column=0)

real_part = Entry(Main_window, width=20, bd=5)
real_part.grid(row=1, columnspan=1, column=0)

label1 = Label(Main_window, text="Imaginary part", width=15, height=2, font=tuple_font, bg="#202020", foreground="#75E9FC")
label1.grid(row=0, columnspan=1, column=1)

imag_part = Entry(Main_window, width=20, bd=5)
imag_part.grid(row=1, columnspan=1, column=1)

img_add = PhotoImage(file="C:/Users/Admin/Desktop/proimg/plus_8.png")

button_add = Button(Main_window, image=img_add, command=lambda : Operation_func("+"), fg="red", bg="#202020", width=50, height=50, borderwidth=0)
button_add.grid(row=0, column=2)

img_subtract = PhotoImage(file="C:/Users/Admin/Desktop/proimg/minus_3.png")

button_subtract = Button(Main_window, image=img_subtract, command=lambda : Operation_func("-"), fg="red", bg="#202020", width=50, height=50, borderwidth=0)
button_subtract.grid(row=0, column=3, pady=5,padx=10)

img_multiply = PhotoImage(file="C:/Users/Admin/Desktop/proimg/multiply_3.png")
                     
button_multiply = Button(Main_window, image=img_multiply, command=lambda : Operation_func("*"), fg="red", bg="#202020", width=50, height=50, borderwidth=0)     
button_multiply.grid(row=1, column=2, pady=5)

img_divide = PhotoImage(file="C:/Users/Admin/Desktop/proimg/divide_3.png")

button_divide = Button(Main_window, image=img_divide, command=lambda : Operation_func("/"), fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_divide.grid(row=1, column=3, pady=5)

img_clear= PhotoImage(file="C:/Users/Admin/Desktop/proimg/clear_3.png")

button_clear = Button(Main_window, text="Clear", command=Clear,  image=img_clear, fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_clear.grid(row=2, column=2, pady=5)

img_evaluate = PhotoImage(file="C:/Users/Admin/Desktop/proimg/eval_1.png")

button_evaluate = Button(Main_window, text="=", command=Evaluate, image=img_evaluate, fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_evaluate.grid(row=2, column=3, pady=5)

img_arg= PhotoImage(file="C:/Users/Admin/Desktop/proimg/arg_1.png")

button_arg = Button(Main_window, text="arg()", command=Argument,image=img_arg, fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_arg.grid(row=0, column=4, pady=5)

img_mod= PhotoImage(file="C:/Users/Admin/Desktop/proimg/mod_1.png")

button_mod = Button(Main_window, text="mod()", command=Modulus, image=img_mod, fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_mod.grid(row=1, column=4, pady=5)

img_conj = PhotoImage(file="C:/Users/Admin/Desktop/proimg/conj_2.png")

button_conj = Button(Main_window, text="conj()", command=Conj, image=img_conj, fg="red", bg="#202020", width=50,height=50, borderwidth=0)
button_conj.grid(row=2, column=4, pady=5,)

label_result = Label(Main_window, text="0", height=2, bg="#936BFF",fg="white", width=35, font=tuple_font1)
label_result.grid(row=2,column=0, columnspan=2,pady=10, padx=10)

button_solvebystat = Button(Main_window, text="Solve by expression", command=Solve_by_stat, width=20)
button_solvebystat.grid(row = 3, column=0, pady=5, columnspan=2,padx=10)

Main_window.mainloop()
                   
