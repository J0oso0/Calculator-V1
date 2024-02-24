# Calculator inspired by Poco x3 pro Calculator App
from tkinter import *
import tkinter
import math

c = Tk()

c.configure(bg = "#000")

calculation = ""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Output
def addToField(symbol):
    global calculation
    if symbol == "%":
        calculation += "/100"
        evaluationField()
    elif symbol == "!":
        num = int(calculation)
        factorial = math.factorial(num)
        calculation = str(factorial)
        evaluationField()
    elif symbol == "^(-1)":
        calculation += "**(-1)"
        evaluationField()
    elif symbol == "√x":
        calculation += "math.sqrt("
        evaluationField()
    else:
        calculation += str(symbol)
        result.delete(1.0, "end")
        result.insert(1.0, calculation)

# Calculate
def evaluationField():
    global calculation    
    try:
         calculation = str(eval(calculation))
         result.delete(1.0, "end")
         result.insert(1.0, calculation)
    except:
        clearField()
        result.insert(1.0, "Error")

# Clearing The field    
def clearField():
    global calculation
    calculation = ""
    result.delete(1.0, "end")

# Deleting Single Character
def deleteCharacter():
    global calculation
    calculation = calculation[:-1]
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

# Expand Button
def switchButton():
    # button 9 replaced
    but9.config(text = "e", command = lambda: addToField("2.71828183"), width = 1, height = 1)
    
    # Button Switch Back
    global but11, but12, but13, but14, but15, but16, but17, but18, but19, but20, but21, but22, but23, but24, but25
    but11 = Button(c, text = "↪", command = switchBack, width = 1, height = 1, fg = '#c52', bg = '#000')
    but11.place(x = 150, y = 900)
    
    # Button Pi (π)
    but12 = Button(c, text = "π", command = lambda: addToField("3.14159"), width = 1, height = 1, fg = '#333', bg = "#000")
    but12.place(x = 150, y = 800)

    # Button one divide multiply (1/x)
    but13 = Button(c, text = "1/x", command = lambda: addToField("^(-1)"), width = 1, height = 1, fg = '#333', bg = '#000')
    but13.place(x = 150, y = 700)
    
    # Button Factorial (x!)
    but14 = Button(c, text = "x!", command = lambda: addToField("!"), width = 1, height = 1, fg = '#333', bg = '#000')
    but14.place(x = 150, y = 600) 

    # Button Square Root (√x)
    but15 = Button(c, text = "√x", command = lambda: addToField("√"), width = 1, height = 1, fg = '#333', bg = '#000')
    but15.place(x = 150, y = 500)

    # Button Squared (xʸ)
    but16 = Button(c, text = "xʸ", command = lambda: addToField("^"), width = 1, height = 1, fg = '#333', bg = '#000')
    but16.place(x = 150, y = 400)

    # Button 2nd
    but17 = Button(c, text = "2nd", width = 1, height = 1, fg = '#333', bg = '#000')
    but17.place(x = 150, y = 300)
    
    # Button logrithm (lg)
    but18 = Button(c, text = "lg", command = lambda: addToField("lg("), width = 1, height = 1, fg = '#333', bg = '#000')
    but18.place(x = 280, y = 400)
    
    # Button Natural Logrithm (ln)
    but19 = Button(c, text = "ln", command = lambda: addToField("ln("), width = 1, height = 1, fg = '#333', bg = '#000')
    but19.place(x = 410, y = 400)
    
    # Button Parenthesis (
    but20 = Button(c, text = "(", command = lambda: addToField("("), width = 1, height = 1, fg = '#333', bg = '#000')
    but20.place(x = 540, y = 400)
    
    # Button Parenthesis )
    but21 = Button(c, text = ")", command = lambda: addToField(")"), width = 1, height = 1, fg = '#333', bg = '#000')
    but21.place(x = 670, y = 400)

    # Button Tangent (tan)
    but22 = Button(c, text = "tan", command = lambda: addToField("tan("), width = 1, height = 1, fg = '#333', bg = '#000')
    but22.place(x = 670, y = 300)

    # Button Cosine (cos)
    but23 = Button(c, text = "cos", command = lambda: addToField("cos("), width = 1, height = 1, fg = '#333', bg = '#000')
    but23.place(x = 540, y = 300)

    # Button Trigonometric (sin)
    but24 = Button(c, text = "sin", command = lambda: addToField("sin("), width = 1, height = 1, fg = '#333', bg = '#000')
    but24.place(x = 410, y = 300)

    # Button Degree (deg)
    but25 = Button(c, text = "deg", width = 1, height = 1, fg = '#333', bg = '#000')
    but25.place(x = 280, y = 300)

    result.config(width = 20, padx = 10.5, height = 0.1,     font = ("Arial", 10), bg = '#000', fg = '#fff')
    result.place(x = 150, y = 228)

    # All Button Displayed Expand
    but1.place(x = 280, y = 500)
    but2.place(x = 410, y = 500)
    but3.place(x = 540, y = 500)
    but4.place(x = 670, y = 500)
    but5.place(x = 670, y = 600)
    but6.place(x = 670, y = 700)
    but7.place(x = 670, y = 800)
    but8.place(x = 670, y = 900)
    but9.place(x = 280, y = 900)
    but10.place(x = 540, y = 900)
    num0.place(x = 410, y = 900)
    num1.place(x = 280, y = 800)
    num2.place(x = 410, y = 800)
    num3.place(x = 540, y = 800)
    num4.place(x = 280, y = 700)
    num5.place(x = 410, y = 700)
    num6.place(x = 540, y = 700)
    num7.place(x = 280, y = 600)
    num8.place(x = 410, y = 600)
    num9.place(x = 540, y = 600)

# Back to Normal
def switchBack():

    but9.config(text = "↻", command = switchButton, width = 1, height = 1)

    result.config(width = 15, padx = 24, height = 0.1, font = ("Arial", 10), bg = '#000', fg = '#fff')

    # Back to Normal
    but1.place(x = 280, y = 200)
    but2.place(x = 410, y = 200)
    but3.place(x = 540, y = 200)
    but4.place(x = 670, y = 200)
    but5.place(x = 670, y = 300)
    but6.place(x = 670, y = 400)
    but7.place(x = 670, y = 500)
    but8.place(x = 670, y = 600)
    but9.place(x = 280, y = 600)
    but10.place(x = 540, y = 600)
    num0.place(x = 410, y = 600)
    num1.place(x = 280, y = 500)
    num2.place(x = 410, y = 500)
    num3.place(x = 540, y = 500)
    num4.place(x = 280, y = 400)
    num5.place(x = 410, y = 400)
    num6.place(x = 540, y = 400)
    num7.place(x = 280, y = 300)
    num8.place(x = 410, y = 300)
    num9.place(x = 540, y = 300)
    result.place(x = 280, y = 128)

    but11.place_forget()
    but12.place_forget()
    but13.place_forget()
    but14.place_forget()
    but15.place_forget()
    but16.place_forget()
    but17.place_forget()
    but18.place_forget()
    but19.place_forget()
    but20.place_forget()
    but21.place_forget()
    but22.place_forget()
    but23.place_forget()
    but24.place_forget()
    but25.place_forget()

# Label Title Display
Title = Label(c, text = "Calculator", bg = '#000', fg = '#c51')
Title.place(x = 450, y = 0)

# Button All Clear (AC)
but1 = Button(c, text = "AC", command = clearField, width = 1, height = 1, fg = '#c52', bg = '#000')
but1.pack()
but1.place(x = 280, y = 200)

# Button Delete (Del)
but2 = Button(c, text = "⌫", command = deleteCharacter, width = 1, height = 1, fg = '#c52', bg = '#000')
but2.pack()
but2.place(x = 410, y = 200)

# Button Percentage (%)
but3 = Button(c, text = "%", command = lambda: addToField("%"), width = 1, height = 1, fg = '#c52', bg = '#000')
but3.pack()
but3.place(x = 540, y = 200)

# Button Divide (÷)
but4 = Button(c, text = "÷", command = lambda: addToField("/"), width = 1, height = 1, fg = '#c52', bg = '#000')
but4.pack()
but4.place(x = 670, y = 200)

# Button Multiplication (×)
but5 = Button(c, text = "×", command = lambda: addToField("*"), width = 1, height = 1, fg = '#c52', bg = '#000')
but5.pack()
but5.place(x = 670, y = 300)

# Button Subtraction (–)
but6 = Button(c, text = "–", command = lambda: addToField("-"), width = 1, height = 1, fg = '#c51', bg = '#000')
but6.pack()
but6.place(x = 670, y = 400)

#Button Subtraction (+)
but7 = Button(c, text = "+", command = lambda: addToField("+"), width = 1, height = 1, fg = '#c51', bg = '#000')
but7.pack()
but7.place(x = 670, y = 500)

# Button Equal (=)
but8 = Button(c, text = "=", command = evaluationField, width = 1, height = 1, fg = '#c51', bg = '#000')
but8.pack()
but8.place(x = 670, y = 600)

# Button switch (↻)
but9 = Button(c, text = "↻", command = switchButton, width = 1, height = 1, fg = '#c51', bg = '#000')
but9.pack()
but9.place(x = 280, y = 600)

#Button Point (.)
but10 = Button(c, text = ".",  command = lambda: addToField("."), width = 1, height = 1, fg = '#fff', bg = '#000')
but10.pack()
but10.place(x = 540, y = 600)

# Button Number 0
num0 = Button(c, text = "0", command = lambda: addToField(0), width = 1, height = 1, fg = '#fff', bg = '#000')
num0.pack()
num0.place(x = 410, y = 600)

# Button Number 1
num1 = Button(c, text = "1", command = lambda: addToField(1), width = 1, height = 1, fg = '#fff', bg = '#000')
num1.pack()
num1.place(x = 280, y = 500)

# Button Number 2
num2 = Button(c, text = "2", command = lambda: addToField(2), width = 1, height = 1, fg = '#fff', bg = '#000')
num2.pack()
num2.place(x = 410, y = 500)

# Button Number 3
num3 = Button(c, text = "3", command = lambda: addToField(3), width = 1, height = 1, fg = '#fff', bg = '#000')
num3.pack()
num3.place(x = 540, y = 500)

# Button Number 4
num4 = Button(c , text = "4", command = lambda: addToField(4), width = 1, height = 1, fg = '#fff', bg = '#000')
num4.pack()
num4.place(x = 280, y = 400)

# Button Number 5
num5 = Button(c, text = "5", command = lambda: addToField(5), width = 1, height = 1, fg = '#fff', bg = '#000')
num5.pack()
num5.place(x = 410, y = 400)

# Button Number 6
num6 = Button(c, text = "6", command = lambda: addToField(6), width = 1, height = 1, fg = '#fff', bg = '#000')
num6.pack()
num6.place(x = 540, y = 400)

# Button Number 7
num7 = Button(c, text = "7", command = lambda: addToField(7), width = 1, height = 1, fg = '#fff', bg = '#000')
num7.pack()
num7.place(x = 280, y = 300)

# Button Number 8
num8 = Button(c, text = "8", command = lambda: addToField(8), width = 1, height = 1, fg = '#fff', bg = '#000')
num8.pack()
num8.place(x = 410, y = 300)

# Button Number 9
num9 = Button(c, text = "9", command = lambda: addToField(9), width = 1, height = 1, fg = '#fff', bg = '#000')
num9.pack()
num9.place(x = 540, y = 300)

# Input Displayed
result = Text(c, width = 15, padx = 24, height = 0.1, font = ("Arial", 10), bg = '#000', fg = '#fff')
result.place(x = 280, y = 128)

# loop
c.mainloop()