import pygame
import random
import math
import copy

# Initialisation
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Dimensions
BLOCK_SIZE = 20
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH * 2 + 12)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Formes des pièces
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

COLORS = [CYAN, YELLOW, MAGENTA, RED, GREEN, BLUE, ORANGE]

# Création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris vs Bot")

clock = pygame.time.Clock()

class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Game:
    def __init__(self, offset_x=0):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Piece()
        self.next_piece = Piece()
        self.game_over = False
        self.score = 0
        self.time = 0
        self.offset_x = offset_x

    def draw(self, screen):
        self.draw_psychedelic_background(screen)
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color != BLACK:
                    pygame.draw.rect(screen, color, (self.offset_x + x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
        
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_piece.color,
                                     (self.offset_x + (self.current_piece.x + x) * BLOCK_SIZE,
                                      (self.current_piece.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1))
        
        self.draw_next_piece(screen)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (self.offset_x + GRID_WIDTH * BLOCK_SIZE + 10, 10))

    def draw_psychedelic_background(self, screen):
        self.time += 0.05
        for x in range(self.offset_x, self.offset_x + GRID_WIDTH * BLOCK_SIZE):
            for y in range(SCREEN_HEIGHT):
                r = int((math.sin(x * 0.01 + self.time) + 1) * 127)
                g = int((math.sin(y * 0.01 + self.time + 2) + 1) * 127)
                b = int((math.sin((x+y) * 0.01 + self.time + 4) + 1) * 127)
                screen.set_at((x, y), (r, g, b))

    def draw_next_piece(self, screen):
        next_piece_x = self.offset_x + GRID_WIDTH * BLOCK_SIZE + 50
        next_piece_y = 100
        pygame.draw.rect(screen, WHITE, (next_piece_x - 10, next_piece_y - 10, 
                                         len(self.next_piece.shape[0]) * BLOCK_SIZE + 20, 
                                         len(self.next_piece.shape) * BLOCK_SIZE + 20), 2)
        for y, row in enumerate(self.next_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.next_piece.color,
                                     (next_piece_x + x * BLOCK_SIZE,
                                      next_piece_y + y * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    def move_piece(self, dx, dy):
        if self.is_valid_move(self.current_piece, dx, dy):
            self.current_piece.move(dx, dy)
            return True
        elif dy > 0:
            self.lock_piece()
            return False
        return False

    def is_valid_move(self, piece, dx, dy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = piece.x + x + dx, piece.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or \
                       (new_y >= 0 and self.grid[new_y][new_x] != BLACK):
                        return False
        return True

    def rotate_piece(self):
        rotated = list(zip(*self.current_piece.shape[::-1]))
        if self.is_valid_move(self.current_piece, 0, 0):
            self.current_piece.shape = rotated

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = Piece()
        if not self.is_valid_move(self.current_piece, 0, 0):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(cell != BLACK for cell in self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared ** 2 * 100

class Bot:
    def __init__(self, game):
        self.game = game

    def make_move(self):
        best_move = self.find_best_move()
        if best_move:
            rotation, x = best_move
            for _ in range(rotation):
                self.game.rotate_piece()
            dx = x - self.game.current_piece.x
            self.game.move_piece(dx, 0)
            while self.game.move_piece(0, 1):
                pass

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        piece = self.game.current_piece
        original_x, original_y = piece.x, piece.y
        original_shape = copy.deepcopy(piece.shape)

        for rotation in range(4):
            for x in range(GRID_WIDTH):
                piece.x, piece.y = x, 0
                if self.game.is_valid_move(piece, 0, 0):
                    while self.game.is_valid_move(piece, 0, 1):
                        piece.y += 1
                    score = self.evaluate_move()
                    if score > best_score:
                        best_score = score
                        best_move = (rotation, x)
            piece.rotate()

        piece.x, piece.y = original_x, original_y
        piece.shape = original_shape
        return best_move

    def evaluate_move(self):
        heights = [0] * GRID_WIDTH
        holes = 0
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.game.grid[y][x] != BLACK or (y >= self.game.current_piece.y and x >= self.game.current_piece.x and x < self.game.current_piece.x + len(self.game.current_piece.shape[0]) and y < self.game.current_piece.y + len(self.game.current_piece.shape) and self.game.current_piece.shape[y - self.game.current_piece.y][x - self.game.current_piece.x]):
                    heights[x] = GRID_HEIGHT - y
                    break
        
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - heights[x], GRID_HEIGHT):
                if self.game.grid[y][x] == BLACK and (y >= self.game.current_piece.y + len(self.game.current_piece.shape) or x < self.game.current_piece.x or x >= self.game.current_piece.x + len(self.game.current_piece.shape[0]) or not self.game.current_piece.shape[y - self.game.current_piece.y][x - self.game.current_piece.x]):
                    holes += 1

        bumpiness = sum(abs(heights[i] - heights[i+1]) for i in range(GRID_WIDTH-1))
        max_height = max(heights)

        return -(max_height * 0.510066 + holes * 0.35663 + bumpiness * 0.184483)

def main():
    player_game = Game()
    bot_game = Game(offset_x=GRID_WIDTH * BLOCK_SIZE + BLOCK_SIZE * 6)
    bot = Bot(bot_game)
    fall_time = 0
    fall_speed = 0.5
    
    while not (player_game.game_over and bot_game.game_over):
        fall_time += clock.get_rawtime()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_game.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    player_game.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    player_game.move_piece(0, 1)
                elif event.key == pygame.K_UP:
                    player_game.rotate_piece()

        if fall_time / 1000 > fall_speed:
            player_game.move_piece(0, 1)
            bot.make_move()
            fall_time = 0

        screen.fill(BLACK)
        player_game.draw(screen)
        bot_game.draw(screen)
        pygame.display.flip()

    print(f"Game Over! Player Score: {player_game.score}, Bot Score: {bot_game.score}")
    pygame.quit()

if __name__ == "__main__":
    main()