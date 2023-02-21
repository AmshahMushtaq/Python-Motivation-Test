from graphics import *
import random, time

def closingGraphic():
    win = GraphWin("Thank You for Taking Assessment", 400, 400)
    circle = Circle(Point(200,200), 150)
    circle.setFill('light blue')
    circle.draw(win)
    message1 = Text(Point(win.getWidth()/2, 200), 'Thank you for taking our Motivation Test!')
    message1.setStyle("bold")
    message1.setSize(15)
    message1.draw(win)
    time.sleep(3)
    for i in range(80):
        r = random.randrange(5)
        b = random.randrange(256)
        g = random.randrange(5)
        color = color_rgb(r, g, b)
        
        radius = random.randrange(3, 40)
        x = random.randrange(5, 395)
        y = random.randrange(5, 395)
        
        circle = Circle(Point(x,y), radius)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(0.09)

    message = message = Text(Point(win.getWidth()/2, 380), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()    
closingGraphic()

