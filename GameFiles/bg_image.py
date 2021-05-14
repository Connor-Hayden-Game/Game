# this files purpose is to hold background image information
# that we will use at a later date, worry about functionality first

bg_image = ImageTk.PhotoImage(Image.open(r"C:\Users\hayde\Desktop\Project\img\bg.png"))
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.create_image(0,0, image=bg_image, anchor="nw")
