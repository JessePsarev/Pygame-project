import pygame

class Key:
    def __init__(self, pos, image):
        self.pos = pygame.Vector2(pos)
        self.image = image
        self.rect = self.image.get_rect(center=(int(self.pos.x), int(self.pos.y)))
        self.radius = self.rect.width / 2  # Use actual image dimensions for hitbox
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect.topleft)

    def touches_circle(self, circle_pos, radius):
        # Use actual key radius (half of image size) for accurate hitbox
        dx = circle_pos.x - self.rect.centerx
        dy = circle_pos.y - self.rect.centery
        return (dx * dx + dy * dy) < ((self.radius + radius) ** 2)

    def collect(self):
        self.collected = True