from tkinter import *
import random

width = 800
height = 400
side_w = 10
side_h = 100
ball_r = 22
ball_speed = 16
ball_x = ball_speed
ball_y = ball_speed
right_line = width

root = Tk()
root.title("ARCANOID")
c = Canvas(root, width=width, height=height, background="black")
c.pack()
c.create_line(0, 0, 0, height, fill="white", width='5')

c.create_line(width, 0, width, height, fill="white")
c.create_line(-1, 0, width, 0, fill='white', width='5')
c.create_line(0, height, width + 1, height, fill='white', width='1')

ball = c.create_oval(10, height / 2 - 11, 32, height / 2 + 11, fill="#7FFFD4", outline='#7FFFD4')
left_side = c.create_line(side_w / 2, 0, side_w / 2, side_h, width=side_w, fill="white")
right_line_w = c.create_line(width, 0, width, height, fill="white")


def spawn():
    global ball_x
    c.coords(ball, 10, height / 2 - 11, 32, height / 2 + 11)
    ball_x = -ball_speed


def push(action):
    global ball_x, ball_y
    if action == "clap":
        ball_y = random.randrange(-10, 10)
        ball_x = -ball_x
    else:
        ball_y = -ball_y


def move_ball():
    ball_left = c.coords(ball)[0]
    ball_top = c.coords(ball)[1]
    ball_right = c.coords(ball)[2]
    ball_bot = c.coords(ball)[3]
    ball_center = (ball_top + ball_bot) / 2

    if ball_right + ball_x < right_line and ball_left + ball_x > side_w:
        c.move(ball, ball_x, ball_y)

    elif ball_right == right_line or ball_left == side_w:
        if ball_right > width / 2:
            if c.coords(right_line_w)[1] < ball_center < c.coords(right_line_w)[3]:
                push('clap')
            else:
                spawn()
        else:
            if c.coords(left_side)[1] < ball_center < c.coords(left_side)[3]:
                push('clap')
            else:
                spawn()
    else:
        if ball_right > width / 2:
            c.move(ball, right_line - ball_right, ball_y)
        else:
            c.move(ball, -ball_left + side_w, ball_y)

    if ball_top + ball_y < 0 or ball_bot + ball_y > height:
        push('other')


left_side_s = 0


def move_side():
    global left_side, left_side_s
    c.move(left_side, 0, left_side_s)
    if c.coords(left_side)[1] < 0:
        c.move(left_side, 0, -c.coords(left_side)[1])
    elif c.coords(left_side)[3] > height:
        c.move(left_side, 0, height - c.coords(left_side)[3])


def stop_side(event):
    global left_side_s
    if event.keysym in "ws":
        left_side_s = 0


c.bind("<KeyRelease>", stop_side)


def move_keypress(event):
    global left_side_s
    if event.keysym == "w":
        left_side_s = -20
    elif event.keysym == "s":
        left_side_s = 20


c.bind("<KeyPress>", move_keypress)


def main():
    move_ball()
    move_side()
    root.after(45, main)


c.focus_set()

main()
root.mainloop()