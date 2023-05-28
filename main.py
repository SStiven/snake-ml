import pygame
from enum import Enum
import random
import sys

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

CREAM = (253, 246, 227)
GREEN = (133, 153, 0)
YELLOW = (181, 137, 0)
ORANGE = (203, 75, 22)
RED = (220, 50, 47)
WHITE = (255, 255, 255)

BLOCK_SIZE = 20
SPEED = 10

WINDOW_WIDTH = 800
WINDOWS_HEIGHT = 600

pygame.init()
windows = pygame.display.set_mode((WINDOW_WIDTH, WINDOWS_HEIGHT))

class Snake:
    def __init__(self, block_size):
        self.direction = Direction.RIGHT
        self.position = [WINDOW_WIDTH/2, WINDOWS_HEIGHT/2]
        self.BLOCK_SIZE = block_size
        self.alive = True

    def update(self):
        if not self.alive:
            return

        x = self.position[0]
        y = self.position[1]

        if self.direction == Direction.RIGHT:
            x += self.BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= self.BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= self.BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += self.BLOCK_SIZE


        if self.__is_inside_window(x, y):
            self.alive = False
            return

        self.position = [x, y]

    def __is_inside_window(self, x, y):
        return x < BLOCK_SIZE or x > WINDOW_WIDTH - BLOCK_SIZE*2 or y < BLOCK_SIZE or y > WINDOWS_HEIGHT - BLOCK_SIZE*2


class Food:
    def __init__(self, block_size):
        self.position = [random.randint(2, (WINDOW_WIDTH/block_size) - 3)*block_size, 
                         random.randint(2, (WINDOWS_HEIGHT/block_size) - 3)*block_size]

class Obstacle:
    def __init__(self, x, y):
        self.position = [x, y]

snake = Snake(BLOCK_SIZE)
foods = [Food(BLOCK_SIZE) for _ in range(10)]
obstacles = []

for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    obstacles.append(Obstacle(i, 0))
    obstacles.append(Obstacle(i, WINDOWS_HEIGHT - BLOCK_SIZE))

for i in range(0, WINDOWS_HEIGHT, BLOCK_SIZE):
    obstacles.append(Obstacle(0, i))
    obstacles.append(Obstacle(WINDOW_WIDTH - BLOCK_SIZE, i))

score = 0
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

if __name__  == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = Direction.DOWN

        windows.fill(CREAM)  

        pygame.draw.rect(windows, GREEN, pygame.Rect(snake.position[0], snake.position[1], BLOCK_SIZE, BLOCK_SIZE))

        for food in foods[:]:
            pygame.draw.rect(windows, YELLOW, pygame.Rect(food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))
            if snake.position == food.position:
                score += 1
                foods.remove(food)

        for obstacle in obstacles:
            pygame.draw.rect(windows, ORANGE, pygame.Rect(obstacle.position[0], obstacle.position[1], BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f"Score: {score}", True, WHITE)
        windows.blit(text, (WINDOW_WIDTH/2, 0))

        if not snake.alive:
            game_over_text = game_over_font.render("Game Over", True, RED)
            windows.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOWS_HEIGHT // 2 - game_over_text.get_height() // 2))

        snake.update()

        pygame.display.update()  

        pygame.time.Clock().tick(SPEED)
