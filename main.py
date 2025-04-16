import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameTime = pygame.time.Clock()
    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        updatables.update(dt)
        for asteroid in asteroids:
            if (asteroid.checkCollision(player)):
                print("Game over!")
                return
        
        for asteroid in asteroids:
            for shot in shots:
                if (asteroid.checkCollision(shot)):
                    asteroid.split()
                    
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = gameTime.tick(60) / 1000
    
if __name__ == "__main__":
    main()