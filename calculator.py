import tkinter
import math

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

def calculator(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        return number1 / number2
    elif sign == "%":
        return number1 % number2
    elif sign == "Нод":
        return gcd(number1, number2)
    elif sign == "Нок":
        return lcm(number1, number2)


number1 = 0
number2 = 0
number3 = None
root = tkinter.Tk()
root.geometry("390x720")
root["bg"] = "#0B0B0A"
root.resizable(False, False)
root.title("Калькулятор")

label = tkinter.Label(text="0", fg="white", bg="#0B0B0A", font="Times 30")
label.place(x=18, y=60)

def one():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 1
        label["text"] = "1"
    else:
        number2 = 1
        number1 = calculator(number1, number2, number3)
        label["text"] = "1"
        number2 = 0
        number3 = None

def plus():
    global label, number3
    label["text"] = "+"
    number3 = "+"

def ost():
    global label, number3
    label["text"] = "%"
    number3 = "%"


def two():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 2
        label["text"] = "2"
    else:
        number2 = 2
        number1 = calculator(number1, number2, number3)
        label["text"] = "2"
        number2 = 0
        number3 = None

def three():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 3
        label["text"] = "3"
    else:
        number2 = 3
        number1 = calculator(number1, number2, number3)
        label["text"] = "3"
        number2 = 0
        number3 = None

def four():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 4
        label["text"] = "4"
    else:
        number2 += 4
        number1 = calculator(number1, number2, number3)
        label["text"] = "4"
        number3 = None


def five():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 5
        label["text"] = "5"
    else:
        number2 = 5
        number1 = calculator(number1, number2, number3)
        label["text"] = "5"
        numer2 = 0
        number3 = None

def six():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 6
        label["text"] = "6"
    else:
        number2 = 6
        number1 = calculator(number1, number2, number3)
        number2 = 0
        label["text"] = "6"
        number3 = None

def seven():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 7
        label["text"] = "7"
    else:
        number2 = 7
        number1 = calculator(number1, number2, number3)
        label["text"] = "7"
        number2 = 0
        number3 = None

def eight():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 8
        label["text"] = "8"
    else:
        number2 = 8
        number1 = calculator(number1, number2, number3)
        label["text"] = "8"
        number2 = 0
        number3 = None


def nine():
    global number1, label, number2, number4, number3
    if number3 == None:
        number1 += 9
        label["text"] = "9"
    else:
        number2 = 9
        number1 = calculator(number1, number2, number3)
        label["text"] = "9"
        number2 = 0
        number3 = None

def zero():
    global number1, label, number2, number3
    if number3 == None:
        number1 += 0
        label["text"] = "0"
    else:
        number2 = 0
        number1 = calculator(number1, number2, number3)
        label["text"] = "0"
        number2 = 0
        number3 = None


def mult():
    global label, number3
    label["text"] = "*"
    number3 = "*"

def minus():
    global label, number3
    label["text"] = "-"
    number3 = "-"

def delit():
    global label, number3
    label["text"] = "/"
    number3 = "/"

def nod():
    global label, number3
    label["text"] = "Нод"
    number3 = "Нод"

def clear():
    global label, number1, number2, number3
    label["text"] = 0
    number1 = 0
    number2 = 0
    number3 = None

def factorial():
    global number1, label
    number1 = math.factorial(number1)
    label["text"] = "!"

def result():
    global label
    label["text"] = number1

def prost():
    global number1, label
    if number1 % 2 == 0:
        return number1 == 2
    d = 3
    while d * d <= number1 and number1 % d != 0:
        d += 2
    if d * d > number1:
        number1 = 1
    else:
        number1 = 0
    label["text"] = "Простое"

def nok():
    global label, number3
    label["text"] = "Нок"
    number3 = "Нок"


button1 = tkinter.Button(root, text="0", width=24, height=5, bg="#54504E", command=zero).place(x = 18, y = 510)
button2 = tkinter.Button(root, text=",", width=10, height=5, bg="#54504E").place(x = 205, y = 510)
button3 = tkinter.Button(root, text="=", width=10, height=5, bg="#ED5808", command=result).place(x = 295, y = 510)

button4 = tkinter.Button(root, text="1", width=10, height=5, bg="#54504E", command=one).place(x = 18, y = 415)
button5 = tkinter.Button(root, text="2", width=10, height=5, bg="#54504E", command=two).place(x = 115, y = 415)
button6 = tkinter.Button(root, text="3", width=10, height=5, bg="#54504E", command=three).place(x = 205, y = 415)
button7 = tkinter.Button(root, text="+", width=10, height=5, bg="#ED5808", command=plus).place(x = 295, y = 415)

button8 = tkinter.Button(root, text="4", width=10, height=5, bg="#54504E", command=four).place(x = 18, y = 320)
button9 = tkinter.Button(root, text="5", width=10, height=5, bg="#54504E", command=five).place(x = 115, y = 320)
button10 = tkinter.Button(root, text="6", width=10, height=5, bg="#54504E", command=six).place(x = 205, y = 320)
button11 = tkinter.Button(root, text="-", width=10, height=5, bg="#ED5808", command=minus).place(x = 295, y = 320)

button12 = tkinter.Button(root, text="7", width=10, height=5, bg="#54504E", command=seven).place(x = 18, y = 225)
button13 = tkinter.Button(root, text="8", width=10, height=5, bg="#54504E", command=eight).place(x = 115, y = 225)
button14 = tkinter.Button(root, text="9", width=10, height=5, bg="#54504E", command=nine).place(x = 205, y = 225)
button15 = tkinter.Button(root, text="X", width=10, height=5, bg="#ED5808", command=mult).place(x = 295, y = 225)

button16 = tkinter.Button(root, text="AC", width=10, height=5, bg="#AAAAAA", command=clear).place(x = 18, y = 130)
button17 = tkinter.Button(root, text="+/-", width=10, height=5, bg="#AAAAAA").place(x = 115, y = 130)
button18 = tkinter.Button(root, text="%", width=10, height=5, bg="#AAAAAA", command=ost).place(x = 205, y = 130)
button19 = tkinter.Button(root, text="/", width=10, height=5, bg="#ED5808", command=delit).place(x = 295, y = 130)



button20 = tkinter.Button(root, text="Нок", width=10, height=5, bg="#ED5808", command=nok).place(x = 18, y = 605)
button21 = tkinter.Button(root, text="Нод", width=10, height=5, bg="#ED5808", command=nod).place(x = 115, y = 605)
button22 = tkinter.Button(root, text="Простое", width=10, height=5, bg="#ED5808", command=prost).place(x = 205, y = 605)
button23 = tkinter.Button(root, text="!", width=10, height=5, bg="#ED5808", command=factorial).place(x = 295, y =605)


root.mainloop()