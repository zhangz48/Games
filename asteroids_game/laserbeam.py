from flying_object import FlyingObject


class LaserBeam(FlyingObject):
    """A single laser torpedo"""
    def __init__(self, SPACE, x, y, x_vel, y_vel):
        self.LASER_SPEED_FACTOR = 5
        self.SPACE = SPACE
        self.rotation = 0.0
        self.radius = 2.5
        self.diam = self.radius*2
        self.x_vel = x_vel * self.LASER_SPEED_FACTOR
        self.y_vel = y_vel * self.LASER_SPEED_FACTOR
        self.x = x + x_vel
        self.y = y + y_vel
        self.lifespan = 100

    def draw_me(self):
        FILL_COLOR = 1
        fill(FILL_COLOR)
        noStroke()
        ellipse(0, 0, self.diam, self.diam)
        self.lifespan -= 1
