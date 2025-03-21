# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #     print(sum)
# #
# #
# # add(1, 2, 4, 56, 1, 2, 69, 42)
# #
# #
# # def calculate(n, **kwargs):
# #     # for key,value in kwargs.items():
# #     #     print(key)
# #     #     print(value)
# #     n += kwargs["add"]
# #     n *= kwargs["multiply"]
# #     print(n)
# #
# #
# # calculate(2, add=3, multiply=5)
#
#
# class Car:
# #     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
#
# car = Car(make="Nissan", model="GT-R", seats=2)
#
# print(car.make)
# print(car.model)
from tkinter import *

window = Tk()


window.title("My First GUI program")
window.minsize(width=500,height=300)

label = Label(text="This is a Label", font=("Arial", 24,"bold"))
label.pack()

label["text"] = "THAT IS SICK"
label["font"] = ("Times New Romans", 80)
label.config(text="New Text", font=("Arial", 24, "italic"))



def button_clicked():
    label.config(text=input.get())


button = Button(text="Click me",command=button_clicked)
button.pack()

#Entry basically input

input = Entry(width=20, name="hello")
input.pack()

checked_state = IntVar()
check_button = Checkbutton(text="is on", variable=checked_state)
check_button.pack()

text = Text(width=15,height=5)
text.pack()
print(text)



window.mainloop()
