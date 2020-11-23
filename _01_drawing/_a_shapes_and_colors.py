import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    myTurtle = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    myTurtle.shape('turtle')
    # Set your turtle's speed using .speed(2)
    myTurtle.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    myTurtle.color('green')
    myTurtle.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range (4):
        myTurtle.forward(100)
        myTurtle.left(90)
    # TEST    Did your turtle draw a square?
        
    # Move your turtle to a new place on the screen using .goto(x, y)
    myTurtle.goto(100,100)
    # x=0 and y=0 is the center of the screen
    
    # Have your turtle draw a circle using .circle(radius, steps=30)
    myTurtle.begin_fill()
    myTurtle.circle(100, steps = 30)
    myTurtle.end_fill()
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    myTurtle.goto(-150,-150)
    myTurtle.pencolor('black')
    myTurtle.color('red')
    myTurtle.begin_fill()
    myTurtle.circle(50,360,5)
    myTurtle.end_fill()

    myTurtle.goto(-200, 100)
    myTurtle.pencolor('orange')
    myTurtle.color('purple')
    myTurtle.begin_fill()
    for i in range (3):
        myTurtle.forward(50)
        myTurtle.right(120)
    myTurtle.end_fill()

    myTurtle.goto(100, -150)
    myTurtle.pencolor('orange')
    myTurtle.color('pink')
    myTurtle.begin_fill()
    myTurtle.circle(50, 360, 7)
    myTurtle.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
