import random
from tkinter import *
from tkinter import messagebox
from winsound import *
complete = False
problem_streak = 0

x = random.randint(1, 9)
y = random.randint(1, 9)
equation = (x, '+', y)
answer = (x + y)


def start_problem():
    global x, y, equation, answer
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    equation = (x, '+', y)
    answer = int(x + y)
    label.config(text=equation)
    start_button.destroy()
def get_answer(en):
    global answer
    global problem_streak
    content2 = (entry.get())
    int_content2 = int(content2)
    if int_content2 == answer:
        start_problem()
        entry.delete(0,END)
        correct_false_label.config(text='Correct', fg='black',bg='#3aff24')
        problem_streak += 1
        streak_label.config(text=problem_streak)
        PlaySound('correct.wav', SND_FILENAME)
    else:
        start_problem()
        entry.delete(0, END)
        correct_false_label.config(text='False',fg='white',bg='red')
        PlaySound('incorrect.wav', SND_FILENAME)
        problem_streak = 0
        streak_label.config(text=problem_streak)


while complete == False:
    root = Tk()

    root.geometry('800x600')
    root.title("Math Generator")
    root.resize(width=False, height=False)
    background_image = PhotoImage(file='backgroundimage.png')
    background_label = Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    label = Label(root, bg="light blue", text="",bd=5)
    label.place(rely=0.25, relx=0.5, relheight=0.15, relwidth=0.40, anchor="center")
    label.config(font=("Courier", 60))
    label.config(highlightbackground='#00e1ff')

    lower_frame = Frame(root, bg='light blue')
    lower_frame.place(rely=0.6, relx=0.5, relheight=0.25, relwidth=.75, anchor="center")

    entry = Entry(lower_frame)
    entry.place(rely=0.5, relx=0.5, relheight=0.5, relwidth=0.15, anchor="center")
    entry.bind('<Return>', get_answer, start_problem,)
    entry.config(font=("Courier", 40))

    start_button = Button(label,text="Start",command=start_problem,font=200)
    start_button.place(rely=0.5, relx=0.5, relheight=0.95, relwidth=0.95, anchor="center")

    middle_frame = Frame(root,bg='black')
    middle_frame.place(rely=0.43, relx=0.5, relheight=0.10, relwidth=.75,anchor='center')

    correct_false_label = Label(middle_frame,text="", bg='black')
    correct_false_label.place(rely=0.5, relx=0.25, relheight=0.8, relwidth=0.45, anchor="center")
    correct_false_label.config(font=("Courier", 45))

    streak_label = Label(middle_frame, text="Streak " + str(problem_streak), bg='black',fg='white')
    streak_label.place(rely=0.5, relx=0.75, relheight=0.8, relwidth=0.45, anchor="center")
    streak_label.config(font=("Courier", 40))

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            global complete
            complete = True
            root.destroy()


    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

