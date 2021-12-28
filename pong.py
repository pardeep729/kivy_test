import kivy
kivy.require("2.0.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from random import randint


class PongPaddle(Widget):
    score = NumericProperty(0)
    can_bounce = BooleanProperty(True)

    def bounce_ball(self, ball):
        if self.collide_widget(ball) and self.can_bounce:
            # speedup = 1.1
            # offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            # ball.velocity = speedup * (offset - ball.velocity)
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            self.can_bounce = False
        elif not self.collide_widget(ball) and not self.can_bounce:
            self.can_bounce = True


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        Update the position depending on current velocity
        """

        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)


    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def serve_ball(self, vel=(4, 0)):
        """
        When the ball spawns, it must be given a random initial velocity
        """

        self.ball.center = self.center # Centre ball to centre of game screen
        self.ball.velocity = vel

    def update(self, dt):
        """ 
        Call this method every frame to update the game screen
        """

        # Update the ball position
        self.ball.move()

        # Bounce ball off paddles (if there is a collision)
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Flip velocity if top or bottom wall
        # if (self.ball.y < 0) or (self.ball.top > self.height):
        #     self.ball.velocity_y *= -1
        # if (self.ball.x < 0) or (self.ball.right > self.width):
        #     self.ball.velocity_x *= -1
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity *= -1

        # Update scores and spawn new ball
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))


class PongApp(App):
    def build(self):
        pong_game = PongGame() # Create instance of PongGame widget
        pong_game.serve_ball() # Serve ball at start of game
        Clock.schedule_interval(pong_game.update, 1.0 / 60.0) # Schedule game update every 1/60 of a second
        return pong_game


if __name__ == '__main__':
    pong_app = PongApp()
    pong_app.run()