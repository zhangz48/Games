from flying_object import FlyingObject
from debris import Debris
import math


class Spaceship(FlyingObject, object):
    """A spaceship"""
    def __init__(self, SPACE):
        self.intact = True
        self.SPACE = SPACE
        self.x = self.SPACE['w']/2
        self.y = self.SPACE['w']/2
        self.x_vel = 0
        self.y_vel = 0
        self.rotation = 0.0
        self.rotation_speed_factor = 5
        self.tip_point = (0, -30)
        self.port_corner_point = (-16, 10)
        self.starboard_corner_point = (16, 10)
        self.radius = 30
        self.thrust = False

    def control(self, keycode, gc=None):
        """Handle keyboard operations on the spaceship"""
        if keycode == UP:
            self.thrust = True
            self.do_thrust()
        if keycode == RIGHT:
            self.rotation += self.rotation_speed_factor
        if keycode == LEFT:
            self.rotation -= self.rotation_speed_factor
        if keycode == ' ':
            if gc:
                gc.fire_laser(self.x, self.y, self.rotation)
        if keycode == 'keyup':
            self.thrust = False

    def do_thrust(self):
        """Set velocity when thruster is activated"""
        THRUST_FACTOR = 0.6
        self.x_vel = (self.x_vel + sin(radians(self.rotation))) * THRUST_FACTOR
        self.y_vel = (self.y_vel - cos(radians(self.rotation))) * THRUST_FACTOR

    def blow_up(self, fade):
        """Blow up the spaceship"""
        self.debris = [
            # Portside debris piece
            Debris(self.SPACE, self.rotation,
                   self.port_corner_point, self.tip_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation-45))/3,
                   - math.cos(math.radians(self.rotation-45))/3,
                   self.radius, fade),
            # Starboardside debris piece
            Debris(self.SPACE, self.rotation,
                   self.tip_point, self.starboard_corner_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation+45))/2.7,
                   - math.cos(math.radians(self.rotation+45))/3.0,
                   self.radius, fade),
            # Stern debris piece
            Debris(self.SPACE, self.rotation,
                   self.port_corner_point, self.starboard_corner_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation+180))/3.5,
                   - math.cos(math.radians(self.rotation+180))/3.7,
                   self.radius, fade)]
        self.intact = False

    def display(self):
        """Overrides the FlyingObject display method"""
        if self.intact:
            # Call the display method defined on
            # FlyingObject (the superclass)
            super(Spaceship, self).display()
        else:
            for piece in self.debris:
                piece.display()

    def draw_me(self):
        """Sets Processing values and calls draw functionality"""
        CYAN = (0, 1.0, 1.0)
        STROKE_WEIGHT = 3

        fill(0)
        strokeWeight(STROKE_WEIGHT)
        stroke(*CYAN)

        self.draw_ship()

        if (self.thrust):
            self.draw_thrust()

    def draw_ship(self):
        """Draws the spaceship triangle"""
        triangle(*
                 (
                    self.port_corner_point +
                    self.tip_point +
                    self.starboard_corner_point
                    )
                 )

    def draw_thrust(self):
        """Draws the thruster"""
        # Describe flame colors
        BLUE_FLAME_COLOR = (0.5, 1.0, 1.0)
        WHITE_FLAME_COLOR = (1.0, 1.0, 1.0)
        YELLOW_FLAME_COLOR = (1.0, 1.0, 0.5)
        YELLOW_ORANGE_FLAME_COLOR = (1.0, 0.8, 0.0)
        ORANGE_FLAME_COLOR = (1.0, 0.6, 0)

        # Y values with respect to the spaceship
        FLAME_BASE_Y = 20
        FLAME_SHORT_Y = 30
        FLAME_LONGEST_Y = 38
        FLAME_LONG_Y = 35
        FLAME_SHORTEST_Y = 25

        # X values with respect to the spaceship
        # Negate for port side
        CENTER = 0
        INNER = 4
        MID_OUTER = 8
        OUTER = 12

        stroke(*BLUE_FLAME_COLOR)
        line(CENTER, FLAME_BASE_Y, CENTER, FLAME_SHORT_Y)

        stroke(*WHITE_FLAME_COLOR)
        line(CENTER, FLAME_SHORT_Y, CENTER, FLAME_LONGEST_Y)

        stroke(*YELLOW_FLAME_COLOR)
        line(-INNER, FLAME_BASE_Y, -INNER, FLAME_LONG_Y)
        line(INNER, FLAME_BASE_Y, INNER, FLAME_LONG_Y)

        stroke(*YELLOW_ORANGE_FLAME_COLOR)
        line(-MID_OUTER, FLAME_BASE_Y, -MID_OUTER, FLAME_SHORT_Y)
        line(MID_OUTER, FLAME_BASE_Y, MID_OUTER, FLAME_SHORT_Y)

        stroke(*ORANGE_FLAME_COLOR)
        line(-OUTER, FLAME_BASE_Y, -OUTER, FLAME_SHORTEST_Y)
        line(OUTER, FLAME_BASE_Y, OUTER, FLAME_SHORTEST_Y)

        stroke(0.0, 0.0, 0.0)