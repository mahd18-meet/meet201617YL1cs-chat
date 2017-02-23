#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE! MAHD QUMSEYA 


#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
#import the Client class from the turtle_chat_client module
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
#####################################################################################
#####################################################################################


from turtle_chat_widgets import Button
from turtle_chat_widgets import TextInput
from turtle_chat_client import Client
import turtle
turtle.ht()


#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (for example, self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (for example, go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################
wn=turtle.Screen()
wn.bgcolor("green")
class TextBox(TextInput):
    def draw_box(self):
        box_turtle = turtle.clone()
        box_turtle.speed(0)
        box_turtle.penup()
        box_turtle.goto(100,100)
        box_turtle.pendown()
        box_turtle.goto(100,-100)       #This creates a box for the input
        box_turtle.goto(-100,-100)
        box_turtle.goto(-100,100)
        box_turtle.goto(100,100)
        box_turtle.ht()

    def write_msg(self):
        self.writer.clear()
        self.new_msg=self.new_msg
        self.writer.clear()
        self.writer.write(self.get_msg())   
        
        

Test = TextBox()
