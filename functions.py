def add_un(word):
    word='un'+word
    return word
word = input('Write a word')
print(add_un(word))
#2
def add_s(word2):
    word2=word2+'s'
    return word2
word2= input('Write a word')
print(add_s(word2))
#3
import math
def circle_area(diameter):
    radius=diameter/2
    area=math.pi*radius**2
    return area
diameter=float(input('enter the diameter'))
print(circle_area(diameter))
#4
def rectangle_area(height,width):
    area=height*width
    return area
height=float(input('enter height'))
width=float(input('enter width'))
print('The area of the rectangle is',rectangle_area(height,width))