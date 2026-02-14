import turtle
import random

# --- Setting ---
screen = turtle.S  creen()
screen.title("Animal Race (Basic Shapes)")
screen.bgcolor("white")

# รายชื่อสัตว์ (เหลือแค่ชื่อที่จะใช้แสดงผล)
animals = ["Turtle", "Rabbit", "Bird", "Cat", "Dog"]
# สีประจำตัว (เอามาใช้แทนรูปภาพ)
colors = ["green", "pink", "blue", "orange", "brown"]

racers = []
start_y = -100

# --- Create Characters ---
# ใช้ zip เพื่อจับคู่ชื่อกับสี
for name, color in zip(animals, colors):
    t = turtle.Turtle()
    t.shape("turtle")   # ใช้รูปเต่าพื้นฐานของ Python แทน
    t.color(color)      # กำหนดสีให้ต่างกันแทนรูปภาพ
    t.penup()
    t.goto(-250, start_y)
    t.pendown()
    racers.append((t, name))
    start_y += 60

# --- Goal Line ---
finish_line = 250
line = turtle.Turtle()
line.penup()
line.goto(finish_line, -200)
line.left(90)
line.pendown()
line.forward(400)
line.hideturtle()

# --- Racing ---
winner = None
while not winner:
    for t, name in racers:
        t.forward(random.randint(1, 10))
        if t.xcor() >= finish_line:
            winner = name
            break

# --- Winner ---
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 200)
text.write(f"The winner is {winner.upper()}!", align="center", font=("Arial", 20, "bold"))

screen.mainloop()