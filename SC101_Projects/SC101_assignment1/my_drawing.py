"""
File: my_drawing.py
Name: Annie Huang
----------------------
This file creates a drawing using by campy.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Aliens
    The most adorable character in Toy Story. Despite having three eyes, they look lovable, never scary.
    """
    window = GWindow(width=800, height=500)
    # background
    bg = GRect(window.width, window.height)
    bg.filled = True
    bg.fill_color = 'paleturquoise'
    window.add(bg)

    # bubble
    bubble = GOval(480, 480, x=(window.width-480)/2, y=(window.height-480)/2)
    bubble.filled = True
    bubble.fill_color = 'ivory'
    bubble.color = 'ivory'
    window.add(bubble)

    # finger
    l_finger = GOval(25, 25, x=308, y=350)
    l_finger.filled = True
    l_finger.fill_color = 'yellowgreen'
    l_finger.color = 'yellowgreen'
    window.add(l_finger)

    r_finger = GOval(25, 25, x=467, y=350)
    r_finger.filled = True
    r_finger.fill_color = 'yellowgreen'
    r_finger.color = 'yellowgreen'
    window.add(r_finger)

    # hands
    l_hand = GPolygon()
    l_hand.add_vertex((305, 350))
    l_hand.add_vertex((350, 290))
    l_hand.add_vertex((350, 380))
    l_hand.filled = True
    l_hand.fill_color = 'dodgerblue'
    l_hand.color = 'dodgerblue'
    window.add(l_hand)

    r_hand = GPolygon()
    r_hand.add_vertex((495, 350))
    r_hand.add_vertex((450, 290))
    r_hand.add_vertex((450, 380))
    r_hand.filled = True
    r_hand.fill_color = 'dodgerblue'
    r_hand.color = 'dodgerblue'
    window.add(r_hand)

    # cloth
    cloth = GRect(130, 140, x=(window.width-130)/2, y=(window.height-140)/2+130)
    cloth.filled = True
    cloth.fill_color = 'dodgerblue'
    cloth.color = 'blue'
    window.add(cloth)

    # belt
    belt = GRect(130, 15, x=(window.width-130)/2, y=(window.height-15)/2+140)
    belt.filled = True
    belt.fill_color = 'royalblue'
    belt.color = 'royalblue'
    window.add(belt)

    buckle = GRect(40, 25, x=(window.width-40)/2, y=(window.height-25)/2+140)
    buckle.filled = True
    buckle.fill_color = 'royalblue'
    buckle.color = 'royalblue'
    window.add(buckle)

    # neck
    neck = GOval(130, 50, x=(window.width-130)/2, y=(window.height-50)/2+60)
    neck.filled = True
    neck.fill_color = 'darkviolet'
    neck.color = 'darkviolet'
    window.add(neck)

    # feet
    l_feet = GOval(75, 40, x=(window.width-130)/2-10, y=(window.height-40)/2+200)
    l_feet.filled = True
    l_feet.fill_color = 'royalblue'
    l_feet.color = 'royalblue'
    window.add(l_feet)

    r_feet = GOval(75, 40, x=(window.width-130)/2+65, y=(window.height-40)/2+200)
    r_feet.filled = True
    r_feet.fill_color = 'royalblue'
    r_feet.color = 'royalblue'
    window.add(r_feet)

    # ears
    ear1 = GPolygon()
    ear1.add_vertex((255, 180))
    ear1.add_vertex((270, 280))
    ear1.add_vertex((300, 250))
    ear1.filled = True
    ear1.fill_color = 'yellowgreen'
    ear1.color = 'yellowgreen'
    window.add(ear1)

    ear2 = GPolygon()
    ear2.add_vertex((545, 180))
    ear2.add_vertex((530, 280))
    ear2.add_vertex((500, 250))
    ear2.filled = True
    ear2.fill_color = 'yellowgreen'
    ear2.color = 'yellowgreen'
    window.add(ear2)

    # face
    face = GOval(width=230, height=150, x=(window.width-230)/2, y=(window.height-150)/2)
    face.filled = True
    face.fill_color = 'yellowgreen'
    face.color = 'yellowgreen'
    window.add(face)

    # 3 eyes and pupils
    eye2 = GOval(40, 40, x=(window.width-40)/2, y=(window.height-40)/2-40)
    eye2.filled = True
    eye2.fill_color = 'white'
    eye2.color = 'white'
    window.add(eye2)
    pupil2 = GOval(13, 13, x=(window.width-13)/2, y=(window.height-13)/2-40)
    pupil2.filled = True
    pupil2.fill_color = 'black'
    pupil2.color = 'black'
    window.add(pupil2)

    eye1 = GOval(40, 40, x=(window.width-40)/2-60, y=(window.height-40)/2-30)
    eye1.filled = True
    eye1.fill_color = 'white'
    eye1.color = 'white'
    window.add(eye1)
    pupil1 = GOval(13, 13, x=(window.width-13)/2-55, y=(window.height-13)/2-30)
    pupil1.filled = True
    pupil1.fill_color = 'black'
    pupil1.color = 'black'
    window.add(pupil1)

    eye3 = GOval(40, 40, x=(window.width-40)/2+60, y=(window.height-40)/2-30)
    eye3.filled = True
    eye3.fill_color = 'white'
    eye3.color = 'white'
    window.add(eye3)
    pupil3 = GOval(13, 13, x=(window.width-13)/2+55, y=(window.height-13)/2-30)
    pupil3.filled = True
    pupil3.fill_color = 'black'
    pupil3.color = 'black'
    window.add(pupil3)

    # head
    deco = GOval(15, 15, x=(window.width-15)/2, y=120)
    deco.filled = True
    deco.fill_color = 'yellowgreen'
    deco.color = 'yellowgreen'
    window.add(deco)

    rect = GRect(3, 60, x=deco.x+6, y=deco.y)
    rect.filled = True
    rect.fill_color = 'yellowgreen'
    rect.color = 'yellowgreen'
    window.add(rect)

    # mouth
    mouth = GOval(25, 30, x=(window.width-25)/2, y=270)
    mouth.filled = True
    mouth.fill_color = 'black'
    mouth.color = 'black'
    window.add(mouth)

    # text
    oh = GLabel('O')
    oh.color = 'purple'
    oh.font = '-70'
    window.add(oh, x=210, y=oh.height+100)

    o2 = GLabel('O')
    o2.color = 'purple'
    o2.font = '-70'
    window.add(o2, x=270, y=o2.height+70)

    o3 = GLabel('O')
    o3.color = 'purple'
    o3.font = '-70'
    window.add(o3, x=330, y=o3.height+50)

    o4 = GLabel('O')
    o4.color = 'purple'
    o4.font = '-70'
    window.add(o4, x=390, y=o4.height+40)

    h1 = GLabel('H')
    h1.color = 'purple'
    h1.font = '-70'
    window.add(h1, x=450, y=h1.height+50)

    h2 = GLabel('H')
    h2.color = 'purple'
    h2.font = '-70'
    window.add(h2, x=505, y=h2.height+80)

    mark = GLabel(' !! ')
    mark.color = 'purple'
    mark.font = '-70'
    window.add(mark, x=540, y=mark.height+120)


if __name__ == '__main__':
    main()
