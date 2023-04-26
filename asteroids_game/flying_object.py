class FlyingObject:
    """Handles common behaviors for flying objects"""
    def display(self):
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel

        if self.x > (self.SPACE['w'] + self.radius):
            self.x = self.radius
        elif self.x > self.SPACE['w'] - self.radius:
            self.position_and_draw(self.x - self.SPACE['w'], self.y)

        if self.y > (self.SPACE['h'] + self.radius):
            self.y = self.radius
        elif self.y > (self.SPACE['h'] - self.radius):
            self.position_and_draw(self.x, self.y - self.SPACE['h'])

        if self.x < -self.radius:
            self.x = (self.SPACE['w'] - self.radius)
        elif self.x < self.radius:
            self.position_and_draw(self.x + self.SPACE['w'], self.y)

        if self.y < -self.radius:
            self.y = (self.SPACE['h'] - self.radius)
        elif self.y < self.radius:
            self.position_and_draw(self.x, self.y + self.SPACE['h'])

        self.position_and_draw(self.x, self.y)

        # Calculate rotation for objects that have a rot_vel attribute
        if hasattr(self, "rot_vel"):
            self.rotation += self.rot_vel

    def position_and_draw(self, x, y):
        translate(x, y)
        rotate(radians(self.rotation))
        self.draw_me()
        rotate(-radians(self.rotation))
        translate(-x, -y)
