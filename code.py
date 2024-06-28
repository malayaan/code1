import pygame
import random

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
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
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
pygame.display.set_caption("Tetris")

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
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Piece()
        self.game_over = False
        self.score = 0

    def draw(self):
        screen.fill(BLACK)
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                pygame.draw.rect(screen, color, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
        
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_piece.color,
                                     ((self.current_piece.x + x) * BLOCK_SIZE,
                                      (self.current_piece.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1))
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 10))

        pygame.display.flip()

    def move_piece(self, dx, dy):
        if self.is_valid_move(self.current_piece, dx, dy):
            self.current_piece.move(dx, dy)
        elif dy > 0:
            self.lock_piece()

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
        self.current_piece = Piece()
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

def main():
    game = Game()
    fall_time = 0
    fall_speed = 0.5
    
    while not game.game_over:
        fall_time += clock.get_rawtime()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move_piece(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate_piece()

        if fall_time / 1000 > fall_speed:
            game.move_piece(0, 1)
            fall_time = 0

        game.draw()

    print(f"Game Over! Score: {game.score}")
    pygame.quit()

if __name__ == "__main__":
    main()