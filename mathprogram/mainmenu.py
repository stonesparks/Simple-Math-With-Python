from tkinter import *


root = Tk()
root.geometry('800x600')
root.title("Main Screen")


frame = Frame(root, bg="light blue",bd=5)
frame.place(rely=0.25, relx=0.5, relheight=0.35, relwidth=0.70, anchor="center")
frame.config(highlightbackground='#00e1ff')

title_label = Label(frame,bg="light blue",bd=5)
title_label.place(rely=0.25, relx=0.5, relheight=1, relwidth=1, anchor="center")
title_label.config(font=("Courier", 30),text="Welcome to Sparks Math!")

msg_label = Label(frame,bg="light blue",bd=5)
msg_label.place(rely=0.75, relx=0.5, relheight=0.75, relwidth=1, anchor="center")
msg_label.config(font=("Courier", 30),text="Please Select Mode:")

sframe = Frame(root, bg="light blue",bd=5)
sframe.place(rely=0.60, relx=0.5, relheight=0.20, relwidth=0.85, anchor="center")
sframe.config(highlightbackground='#00e1ff')

select_add = Button(sframe, text="Basic Addition", font=200)
select_add.place(rely=0.5, relx=0.20, relheight=0.75, relwidth=0.20, anchor="center")

select_subtract = Button(sframe, text="Basic Subtraction", font=200)
select_subtract.place(rely=0.5, relx=0.40, relheight=0.75, relwidth=0.20, anchor="center")

select_2dadd = Button(sframe, text="2 Digit Addition", font=200)
select_2dadd.place(rely=0.5, relx=0.60, relheight=0.75, relwidth=0.20, anchor="center")

select_2dsub = Button(sframe, text="2 Digit Subtraction", font=200)
select_2dsub.place(rely=0.5, relx=0.80, relheight=0.75, relwidth=0.20, anchor="center")




root.mainloop()




