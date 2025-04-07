BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

rand_num = random.randint(0, len(to_learn)-1)
french_word = to_learn[rand_num]["French"]
def right_button():
    global rand_num
    try:
        to_learn.remove(to_learn[rand_num])
    except IndexError:
        canvas.itemconfig(top_text,text="YOU HAVE FINISHED,")
        canvas.itemconfig(bottom_text,text="CONGRATS!!!!")
    words_learned = pandas.DataFrame(to_learn)
    words_learned.to_csv("data/words_to_learn.csv")
    generate_new_word()

def generate_new_word():
    global rand_num, showing_back
    rand_num = random.randint(0, len(to_learn)-1)
    window.after_cancel(showing_back)
    canvas.itemconfig(canvas_image, image=front_image)

    french_word = to_learn[rand_num]["French"]

    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(bottom_text, text=french_word, fill="black")
    showing_back = window.after(3000, show_back)


def show_back():
    global rand_num
    english_word = to_learn[rand_num]["English"]

    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(top_text, text="English", fill="#FFFFFF")
    canvas.itemconfig(bottom_text, text=english_word, fill="#FFFFFF")


showing_back = window.after(1, show_back)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas_image = canvas.create_image(400, 263, image=front_image)
top_text = canvas.create_text(400, 150, text=f"French", font=("Ariel", 40, "italic"))
bottom_text = canvas.create_text(400, 263, text=f"English", font=("Ariel", 60, "bold"))


canvas.grid(column=0, row=0, columnspan=2)
generate_new_word()

right_button = Button(image=right_image, highlightthickness=0, fg=BACKGROUND_COLOR,
                      command=right_button)
wrong_button = Button(image=wrong_image, highlightthickness=0, fg=BACKGROUND_COLOR,
                      command=generate_new_word)

right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)


window.mainloop()
