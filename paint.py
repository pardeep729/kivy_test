from random import random

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button, Label


class PaintingWidget(Widget):
    def on_touch_down(self, touch):
        # Set Color
        colour = (random(), 1., 1.)
        # Use canvas Context Manager so that graphics are drawn
        with self.canvas:
            Color(*colour, mode='hsv')

            # Draw circles where clicked
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            # On first touch, create the new line
            touch.ud['line'] = Line(points=(touch.x, touch.y))


    def on_touch_move(self, touch):
        # While still holding down, add all points along route to the line's points attributes
        touch.ud['line'].points += (touch.x, touch.y)


class PaintingApp(App):
    def build(self):
        self.title = 'Simple Painting App' # Set title of application

        self.main = Widget() # Create main parent widget to hold all child widgets
        
        # Painting widget
        self.painting_widget = PaintingWidget()
        self.main.add_widget(self.painting_widget) # Add widget to parent

        # Clear button
        self.clear_button =  Button(text='Clear canvas')
        self.clear_button.bind(on_release=self.clear_canvas) # Clear canvas on press button
        self.main.add_widget(self.clear_button) # Add widget to parent

        return self.main

    def clear_canvas(self, obj):
        """
        Clear canvas of all paintings

        Parameters:
            obj: The kivy object that triggered the method (will be a "clear canvas" button)
        """
        self.painting_widget.canvas.clear()



if __name__ == '__main__':
    paint_app = PaintingApp()
    paint_app.run()