from tkinter import *


def miles_to_kilo():
    mile = int(miles_entry.get())
    mile *= 1.609
    kilo_label_entry.config(text=round(mile,4))


miles_y_cor = 75
window = Tk()
window.title("Miles to Kilometer ")
window.minsize(width=300,height=100)

kilo = 0
mile_label = Label(text="Miles")
mile_label.grid(column=3,row=2)

miles_entry = Entry(width=10)
miles_entry.grid(column=2,row=2)

kilo_label_entry = Label(text=kilo)
kilo_label_entry.grid(column=2, row=3)

kilo_label = Label(text="Km")
kilo_label.grid(column=3,row=3)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=3)

button = Button(text="calculate", command=miles_to_kilo)
button.grid(column=2, row=4)



window.mainloop()