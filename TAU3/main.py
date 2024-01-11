import random

class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start = (random.randint(0, rows-1), 0)
        self.stop = (random.randint(0, rows-1), cols-1)
        self.obstacles = set()

        # Losowo generuj przeszkody
        self.generate_obstacles()

    def generate_obstacles(self):
        num_obstacles = random.randint(5, (self.rows * self.cols) // 3)
        for _ in range(num_obstacles):
            obstacle_row = random.randint(0, self.rows - 1)
            obstacle_col = random.randint(0, self.cols - 1)

            # Upewnij się, że przeszkoda nie jest na START, STOP lub już istnieje
            while (obstacle_row, obstacle_col) in {self.start, self.stop} or (obstacle_row, obstacle_col) in self.obstacles:
                obstacle_row = random.randint(0, self.rows - 1)
                obstacle_col = random.randint(0, self.cols - 1)

            self.obstacles.add((obstacle_row, obstacle_col))

    def display_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) == self.start:
                    print('A', end=' ')
                elif (row, col) == self.stop:
                    print('B', end=' ')
                elif (row, col) in self.obstacles:
                    print('X', end=' ')
                else:
                    print(' ', end=' ')
            print()

    def move(self, direction):
        current_row, current_col = self.start

        if direction == 'right':
            current_col += 1
        elif direction == 'left':
            current_col -= 1
        elif direction == 'up':
            current_row -= 1
        elif direction == 'down':
            current_row += 1

        # Sprawdź, czy nowa pozycja jest poprawna
        if 0 <= current_row < self.rows and 0 <= current_col < self.cols and (current_row, current_col) not in self.obstacles:
            self.start = (current_row, current_col)
            return True
        else:
            print("Niemożliwy ruch!")
            return False

# Przykładowe użycie
if __name__ == "__main__":
    rows, cols = 5, 5
    game_board = GameBoard(rows, cols)

    print("Plansza początkowa:")
    game_board.display_board()

    # Indywidualne sterowanie, dopóki niemożliwy ruch
    while True:
        print("Wybierz kierunek (right, left, up, down):")
        chosen_direction = input().lower()

        if chosen_direction in ['right', 'left', 'up', 'down']:
            moved = game_board.move(chosen_direction)
            game_board.display_board()

            if not moved:
                break
        else:
            print("Nieprawidłowy kierunek. Wybierz ponownie.")
