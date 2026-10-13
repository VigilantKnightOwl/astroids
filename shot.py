import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)


    # in the Shot class
    def draw(self, screen: pygame.Surface) -> None:
        # override from CircleShape
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)


    def update(self, dt: float) -> None:
        # must override
        self.position += self.velocity * dt