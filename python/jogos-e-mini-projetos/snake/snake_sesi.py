import pygame
import sys
import time
import random

class SnakeGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up the display
        self.frame_size_x = 1400
        self.frame_size_y = 720
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))
        pygame.display.set_caption('Cobra irritante')

        # Colors
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        # FPS controller
        self.fps_controller = pygame.time.Clock()

        # Game variables
        self.speed = 20
        self.square_size = 20
        self.direction = 'RIGHT'
        self.head_pos = [120, 60]
        self.snake_body = [[120, 60]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // self.square_size)) * self.square_size,
                         random.randrange(1, (self.frame_size_y // self.square_size)) * self.square_size]
        self.food_spawn = True
        self.score = 0

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score: ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.frame_size_x / 10, 15)
        else:
            score_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 1.25)

        self.game_window.blit(score_surface, score_rect)

    def check_collision(self):
        if self.head_pos[0] < 0 or self.head_pos[0] > self.frame_size_x - self.square_size or \
                self.head_pos[1] < 0 or self.head_pos[1] > self.frame_size_y - self.square_size:
            return True

        for block in self.snake_body[1:]:
            if self.head_pos[0] == block[0] and self.head_pos[1] == block[1]:
                return True

        return False

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == ord('w')) and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif (event.key == pygame.K_DOWN or event.key == ord('s')) and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif (event.key == pygame.K_RIGHT or event.key == ord('d')) and self.direction != 'LEFT':
                        self.direction = 'RIGHT'
                    elif (event.key == pygame.K_LEFT or event.key == ord('a')) and self.direction != 'RIGHT':
                        self.direction = 'LEFT'

            # Update snake position
            if self.direction == 'UP':
                self.head_pos[1] -= self.square_size
            elif self.direction == 'DOWN':
                self.head_pos[1] += self.square_size
            elif self.direction == "LEFT":
                self.head_pos[0] -= self.square_size
            else:
                self.head_pos[0] += self.square_size

            # Check for collision
            if self.check_collision():
                self.__init__()  # Restart the game
                continue

            # Eating apple
            self.snake_body.insert(0, list(self.head_pos))
            if self.head_pos[0] == self.food_pos[0] and self.head_pos[1] == self.food_pos[1]:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()

            # Spawn food
            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (self.frame_size_x // self.square_size)) * self.square_size,
                                 random.randrange(1, (self.frame_size_y // self.square_size)) * self.square_size]
                self.food_spawn = True

            # GFX
            self.game_window.fill(self.black)
            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, self.blue, pygame.Rect(pos[0] + 2, pos[1] + 2,
                                                                          self.square_size - 2, self.square_size - 2))

            pygame.draw.rect(self.game_window, self.red, pygame.Rect(self.food_pos[0], self.food_pos[1],
                                                                     self.square_size, self.square_size))

            self.show_score(1, self.white, 'consolas', 20)
            pygame.display.update()
            self.fps_controller.tick(self.speed)

# Run the game
if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()
