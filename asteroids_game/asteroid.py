from flying_object import FlyingObject


class Asteroid(FlyingObject):
    """An asteroid"""
    def __init__(self, SPACE, asize='Large',
                 x=100, y=100, x_vel=0.2, y_vel=0.25,
                 rot=0.0, rot_vel=1.0):
        self.SPACE = SPACE
        self.x = x
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rotation = rot
        self.rot_vel = rot_vel
        self.asize = asize
        if self.asize == 'Large':
            self.radius = 65
        if self.asize == 'Med':
            self.radius = 40
        if self.asize == 'Small':
            self.radius = 25

    def draw_me(self):
        STROKE_COLOR = (0.8, 0.8, 0.8)
        STROKE_WEIGHT = 3
        FILL_COLOR = 0

        stroke(*STROKE_COLOR)
        fill(FILL_COLOR)
        strokeWeight(STROKE_WEIGHT)

        beginShape()
        if self.asize == 'Large':
            self.large_shape()

        if self.asize == 'Med':
            self.med_shape()

        if self.asize == 'Small':
            self.small_shape()
        endShape(CLOSE)

    def large_shape(self):
        vertex(-30, -30)  # upper left
        vertex(0, -50)
        vertex(50, -40)  # upper right
        vertex(60, 0)
        vertex(30, 50)  # lower right
        vertex(0, 20)
        vertex(-40, 30)  # lower left
        vertex(-50, 0)

    def med_shape(self):
        vertex(-30, -25)  # upper left
        vertex(0, -30)
        vertex(30, -20)  # upper right
        vertex(25, 0)
        vertex(15, 10)  # lower right
        vertex(-10, 20)  # lower left
        vertex(-25, 0)

    def small_shape(self):
        vertex(0, -20)
        vertex(15, 0)
        vertex(0, 15)
        vertex(-18, 10)  # lower left
        vertex(-20, 0)
