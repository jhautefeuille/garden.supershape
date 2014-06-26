#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Shape
=====

The Shape class displays a supershape chart.

'''

__title__ = 'garden.supershape'
__version__ = '0.1.5'
__author__ = 'julien@hautefeuille.eu'
__all__ = ('Shape',)

# Main Kivy import
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.utils import get_color_from_hex
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.properties import BoundedNumericProperty
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import Bezier
from kivy.graphics import Line, Point
from kivy.graphics import Scale, Translate, Rotate, PopMatrix, PushMatrix

# Computing import
import math

def superformula(a, b, m, n1, n2, n3, phi):
    ''' 
    Computes the position of the point on a
    superformula curve.
    Superformula has first been proposed by Johan Gielis
    and is a generalization of superellipse.
    see: http://en.wikipedia.org/wiki/Superformula
    '''

    t1 = math.cos(m * phi / 4.0) / a
    t1 = abs(t1)
    t1 = math.pow(t1, n2)

    t2 = math.sin(m * phi / 4.0) / b
    t2 = abs(t2)
    t2 = math.pow(t2, n3)

    t3 = -1 / float(n1)
    r = math.pow(t1 + t2, t3)
    if abs(r) == 0:
        return (0, 0)
    else:
        return (r * math.cos(phi), r * math.sin(phi))

def supershape(
        width,
        height,
        m,
        n1,
        n2,
        n3,
        point_count=100,
        percent=1.0,
        a=1.0,
        b=1.0,
        travel=None):

    '''
    Supershape, generated using the superformula first proposed
    by Johan Gielis.

    - `points_count` is the total number of points to compute.
    - `travel` is the length of the outline drawn in radians.
      3.1416 * 2 is a complete cycle.
    '''
    travel = travel or (math.pi * 2)

    # Compute points
    phis = [i*travel/point_count for i in range(int(point_count * percent))]
    points = [superformula(a, b, m, n1, n2, n3, x) for x in phis]

    # Scale and transpose
    path = []
    for x, y in points:
        x *= width
        y *= height
        path.append((x, y))

    return path


class Shape(RelativeLayout):
    '''
    Shape class
    '''

    shape_size = BoundedNumericProperty(256, min=1, max=512, errorvalue=512)
    color = StringProperty('3619ffff')
    bg_color = StringProperty('19526699')
    a = BoundedNumericProperty(1, min=0.1, max=1, errorvalue=1)
    b = BoundedNumericProperty(1, min=0.1, max=1, errorvalue=1)
    m = BoundedNumericProperty(7, min=-100, max=100, errorvalue=16)
    n1 = BoundedNumericProperty(2, min=1, max=50, errorvalue=4)
    n2 = BoundedNumericProperty(8, min=1, max=50, errorvalue=4)
    n3 = BoundedNumericProperty(4, min=1, max=50, errorvalue=10)
    nbp = BoundedNumericProperty(100, min=2, max=1000, errorvalue=100)
    percent = BoundedNumericProperty(1, min=1, max=10, errorvalue=1)
    travel = BoundedNumericProperty(2, min=2, max=100, errorvalue=2)
    line = BooleanProperty(False)
    wdth = BoundedNumericProperty(1, min=1, max=10, errorvalue=1)
    path = ListProperty()

    def __init__(self, **kwargs):
        super(Shape, self).__init__(**kwargs)
        self.bind(
            pos=self.update,
            size=self.update,
            shape_size=self.update,
            color=self.update,
            bg_color=self.update,
            a=self.update,
            b=self.update,
            m=self.update,
            n1=self.update,
            n2=self.update,
            n3=self.update,
            nbp=self.update,
            percent=self.update,
            travel=self.update,
            line=self.update,
            wdth=self.update)

    def update(self, *args):
        with self.canvas:
            # Refresh canvas
            self.canvas.clear()

            # Background configuration
            Color(
                get_color_from_hex(self.bg_color)[0],
                get_color_from_hex(self.bg_color)[1],
                get_color_from_hex(self.bg_color)[2], 100)
            Rectangle(pos=self.pos, size=self.size)

            # Path configuration
            Translate(self.width / 2, self.height / 2)
            Color(
                get_color_from_hex(self.color)[0],
                get_color_from_hex(self.color)[1],
                get_color_from_hex(self.color)[2], 100)

            s = supershape(
                width=self.shape_size / 2.0,
                height=self.shape_size / 2.0,
                m=self.m,
                n1=self.n1,
                n2=self.n2,
                n3=self.n3,
                point_count=self.nbp,
                percent=self.percent,
                a=self.a,
                b=self.b,
                travel=math.pi * self.travel)

            # clear path list
            self.path[:] = []
            for elem in s:
                self.path.append(elem[0])
                self.path.append(elem[1])

            if self.line:
                Line(
                    points=(self.path),
                    width=self.wdth,
                    cap="round",
                    joint="round",
                    close=True)
            else:
                Point(
                    points=(self.path),
                    pointsize=self.wdth,
                    cap="round",
                    joint="round",
                    close=True)

class ShapeTest(App):
    """
    Example application
    """
    
    def build(self):
        shape = Shape(n1=7, color='3619ffff', bg_color='19526699', size_hint=(0.8, 1))
        return shape

if __name__ in ('__main__'):
    ShapeTest().run()