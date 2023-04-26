from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        for laser in range(len(self.laser_beams)):
            if self.laser_beams[laser].lifespan >= 0:
                self.laser_beams[laser].display()

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel)
            )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        if len(self.asteroids) > 0:
            for i in reversed(range(len(self.asteroids))):
                for j in reversed(range(len(self.laser_beams))):
                    if (
                        abs(self.laser_beams[j].x - self.asteroids[i].x)
                        < max(self.asteroids[i].radius,
                              self.laser_beams[j].radius)
                        and
                        abs(self.laser_beams[j].y - self.asteroids[i].y)
                        < max(self.asteroids[i].radius,
                              self.laser_beams[j].radius)
                    ):
                        self.blow_up_asteroid(i, j)
                        del self.laser_beams[j]
                        break
        else:
            self.asteroid_destroyed = True

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                      abs(self.spaceship.x - self.asteroids[i].x)
                      < max(self.asteroids[i].radius, self.spaceship.radius)
                      and
                      abs(self.spaceship.y - self.asteroids[i].y)
                      < max(self.asteroids[i].radius, self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Position of the asteroid that is hit
        x = self.asteroids[i].x
        y = self.asteroids[i].y
        # Velocity of the laser beam that hits the asteroid
        x_vel = self.laser_beams[j].x_vel
        y_vel = self.laser_beams[j].y_vel

        if self.asteroids[i].asize == "Large":
            # Add two med size asteroids which fly off
            # perpendicularly to the direction of the laser beam
            # reduce x_vel and y_vel by 1/2
            # to maintain the miliar flying speed
            self.asteroids.append(Asteroid(self.SPACE, asize="Med", x=x, y=y,
                                           x_vel=-y_vel/2, y_vel=x_vel/2))
            self.asteroids.append(Asteroid(self.SPACE, asize="Med", x=x, y=y,
                                           x_vel=y_vel/2, y_vel=-x_vel/2))

        if self.asteroids[i].asize == "Med":
            # Add three med size asteroids which two fly off
            # perpendicularly to the direction of the laser beam
            # and the third flies off in the same direction
            # reduce x_vel and y_vel by 1/2
            # to maintain the miliar flying speed
            self.asteroids.append(
                Asteroid(self.SPACE, asize="Small", x=x, y=y,
                                           x_vel=-y_vel/2, y_vel=x_vel/2))
            self.asteroids.append(
                Asteroid(self.SPACE, asize="Small", x=x, y=y,
                                           x_vel=y_vel/2, y_vel=-x_vel/2))
            self.asteroids.append(
                Asteroid(self.SPACE, asize="Small", x=x, y=y,
                                           x_vel=x_vel/2, y_vel=y_vel/2))

        del self.asteroids[i]  # Remove the asteroid that is hit
