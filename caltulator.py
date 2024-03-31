from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Калькулятор")
root.geometry("500x750")
root.maxsize(500,750)
root.minsize(500,750)
root.iconbitmap(default= "calculatorico.ico")

buttons_height = 75
buttons_width = 100

numbers = [24,56]

  

def plus():
    global operations
    operations= "+"
    print(operations)
    
def minus():
    global operations
    operations = "-"
    print(operations)
    
def mult():
    global operations
    operations = "x"
    print(operations)
    
def divis():
    global operations
    operations = "/"
    print(operations)
    
    


def pmud():
    if operations == "+":
        text.delete(textfromtext)
        conc = numbers[0], "+", numbers[1], "=", (numbers[0]+numbers[1])
        text(conc)
     
    if operations == "-":
        textfromtext.delete()
        conc = numbers[0],"-",numbers[1],"=",(numbers[0]-numbers[1])
        text(conc)
          
    if operations == "x":
        textfromtext.delete()
        conc = numbers[0], "x", numbers[1], "=", (numbers[0]*numbers[1])
        text(conc)
          
    if operations == "/":
        textfromtext.delete()
        conc = numbers[0],"/",numbers[1],'=',(numbers[0]/numbers[1])
        text(conc)
      
def procent():
 otvet = int(numbers[1])/100
 otvet = otvet * int(numbers[0])

 text(otvet)


#создаем текстовой бокс для вывода значений с толшиной границы 2 пикселя
framefromtext = ttk.Frame(root,borderwidth=2,relief=SOLID,height=225, width=450)
framefromtext.pack(side=TOP,pady=25)
framefromtext.pack_propagate(0)

#функция для вывода текста на экран
def text(result):
 global textfromtext
 textfromtext = Text(framefromtext)
 textfromtext.insert(40.0,result)
 textfromtext.pack(anchor=NW)



#кнопки
def buttons():
 framefrombuttons = ttk.Frame(root, borderwidth=2, relief=SOLID, height=485, width=450,padding=(10,5))
 
 button_PROCENT_frombuttons = ttk.Button(framefrombuttons, text="%", command=procent)
 button_PROCENT_frombuttons.pack()
 button_PROCENT_frombuttons.place(anchor=NW, height=buttons_height, width=buttons_width)
 
 button_1_frombuttons = ttk.Button(framefrombuttons,text=1)
 button_1_frombuttons.pack()
 button_1_frombuttons.place(anchor=NW, y=85,height=buttons_height, width=buttons_width)
 
 button_4_frombuttons = ttk.Button(framefrombuttons, text=4)
 button_4_frombuttons.pack()
 button_4_frombuttons.place(anchor=NW, y=170, height=buttons_height, width=buttons_width)
 
 button_7_frombuttons = ttk.Button(framefrombuttons, text=7)
 button_7_frombuttons.pack()
 button_7_frombuttons.place(anchor=NW, y=255, height=buttons_height, width=buttons_width)
 
 button_pm_frombuttons = ttk.Button(framefrombuttons, text="+/-")
 button_pm_frombuttons.pack()
 button_pm_frombuttons.place(anchor=NW, y=340, height=buttons_height, width=buttons_width)
 
 button_C_frombuttons = ttk.Button(framefrombuttons, text="C", )
 button_C_frombuttons.pack()
 button_C_frombuttons.place(anchor=NW,x=110, height=buttons_height, width=buttons_width)

 button_2_frombuttons = ttk.Button(framefrombuttons, text=2)
 button_2_frombuttons.pack()
 button_2_frombuttons.place(anchor=NW, x=110, y=85,height=buttons_height, width=buttons_width)

 button_5_frombuttons = ttk.Button(framefrombuttons, text=5)
 button_5_frombuttons.pack()
 button_5_frombuttons.place(anchor=NW, x=110, y=170,height=buttons_height, width=buttons_width)

 button_8_frombuttons = ttk.Button(framefrombuttons, text=8)
 button_8_frombuttons.pack()
 button_8_frombuttons.place(anchor=NW, x=110, y=255,height=buttons_height, width=buttons_width)

 button_0_frombuttons = ttk.Button(framefrombuttons, text="0")
 button_0_frombuttons.pack()
 button_0_frombuttons.place(anchor=NW, x=110, y=340, height=buttons_height, width=buttons_width)
 
 button_DEL_frombuttons = ttk.Button(framefrombuttons, text="⌫")
 button_DEL_frombuttons.pack()
 button_DEL_frombuttons.place(anchor=NW, x=220 , height=buttons_height, width=buttons_width)

 button_3_frombuttons = ttk.Button(framefrombuttons, text=3)
 button_3_frombuttons.pack()
 button_3_frombuttons.place(anchor=NW, x=220, y=85,height=buttons_height, width=buttons_width)

 button_6_frombuttons = ttk.Button(framefrombuttons, text=5)
 button_6_frombuttons.pack()
 button_6_frombuttons.place(anchor=NW, x=220, y=170,height=buttons_height, width=buttons_width)

 button_9_frombuttons = ttk.Button(framefrombuttons, text=8)
 button_9_frombuttons.pack()
 button_9_frombuttons.place(anchor=NW, x=220, y=255,height=buttons_height, width=buttons_width)

 button_comma_frombuttons = ttk.Button(framefrombuttons, text=",")
 button_comma_frombuttons.pack()
 button_comma_frombuttons.place(anchor=NW, x=220, y=340,height=buttons_height, width=buttons_width)
 
 button_equals_frombuttons = ttk.Button(framefrombuttons, text="=",command=pmud)
 button_equals_frombuttons.pack()
 button_equals_frombuttons.place(anchor=NW, x=330, height=buttons_height, width=buttons_width)

 button_plus_frombuttons = ttk.Button(framefrombuttons, text="+",command= plus )
 button_plus_frombuttons.pack()
 button_plus_frombuttons.place(anchor=NW, x=330, y=85,height=buttons_height, width=buttons_width)

 button_minus_frombuttons = ttk.Button(framefrombuttons, text="-",command  =minus)
 button_minus_frombuttons.pack()
 button_minus_frombuttons.place(anchor=NW, x=330, y=170,height=buttons_height, width=buttons_width)

 button_multiplication_frombuttons = ttk.Button(framefrombuttons, text="X",command = mult)
 button_multiplication_frombuttons.pack()
 button_multiplication_frombuttons.place(anchor=NW, x=330, y=255,height=buttons_height, width=buttons_width)

 button_division_frombuttons = ttk.Button(framefrombuttons, text="÷",command = divis)
 button_division_frombuttons.pack()
 button_division_frombuttons.place(anchor=NW, x=330, y=340, height=buttons_height, width=buttons_width)
 
 framefrombuttons.pack(side=BOTTOM, pady=20)
 framefrombuttons.pack_propagate(0)
 

buttons()
root.mainloop()

