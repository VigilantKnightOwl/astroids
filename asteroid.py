import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # in the Astroid class
    def draw(self, screen: pygame.Surface) -> None:
        # override from CircleShape
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # must override
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(rand_angle)
            new_vector2 = self.velocity.rotate(rand_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2