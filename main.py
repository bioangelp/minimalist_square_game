#pgzero
import random

# Global variables and data structures
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("track_down")  # Used to indicate the player's path
cell3 = Actor("muerte")
cell4 = Actor("win")

# Game window settings
size_w = 51
size_h = 30
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
TITLE = "minimalist_square_game"
FPS = 30

# UI elements
background = Actor("background")
play = Actor("play", (900, 300))

# Tracking movement
path_taken = []  # List to store positions the player has passed through

# Game mode
mode = "game"
win = 0
current_player = 1

# Player's old position
old_position = (0, 0)
old_x = 0
old_y = 0       
             #1   #2   #3   #4   #5   #6   #7   #8   #9   #10  #11  #12  #13  #14   #15 #16  #17  #18  #19  #20  #21  #22  #23  #24  #25  #26  #27  #28  #29  #30  #31  #32  #33  #34  #35 #36  #37  #38  #39  #40   #40  #41  #42  #43  #44  #45 #46  #47  #48  #49  #51 
my_map = [  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], #1
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #3
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #4
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #5
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #6
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #7
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #8
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #9
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #10
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #11
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #12
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #13
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #14
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #15
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], #1
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #3
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #4
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #5
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #6
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #7
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #8
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #9
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #10
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #11
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #12
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #13
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #14
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']] #15
                      

#Unit Class Definitions
initial_position = 0
class Unit:
    def __init__(self, name, sprite, vida, ataque, defensa, velocidad, bonus, position=(0, 0), abilities=[]):
        self.name = name
        # Ensure the sprite is correctly initialized with the provided sprite name or default to "stand"
        self.sprite = Actor(sprite if sprite else "stand")
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.bonus = bonus
        self.position = position
        self.abilities = abilities
        self.update_sprite_position()

    def update_sprite_position(self):
        # Update the sprite's position
        self.sprite.pos = self.position

    def draw(self):
        # Draw the sprite on the screen at its current position
        self.sprite.draw()

    # You might also want to include an update method here to handle logic updates
    def update(self):
        # Logic to update the unit's state
        pass

    def update_sprite_position(self):
        self.sprite.pos = self.position

    def distance_to(self, other_unit):
        # Calculate the distance between self and another unit
        dx = self.position[0] - other_unit.position[0]
        dy = self.position[1] - other_unit.position[1]
        return (dx**2 + dy**2) ** 0.5

    def move(self, direction):
        global initial_position, path_taken
        initial_position = self.position  # Store initial position for comparison after movement
        while self.can_move(direction):
            if direction == "up":
                self.position = (self.position[0], self.position[1] - 1)
            elif direction == "down":
                self.position = (self.position[0], self.position[1] + 1)
            elif direction == "left":
                self.position = (self.position[0] - 1, self.position[1])
            elif direction == "right":
                self.position = (self.position[0] + 1, self.position[1])
        
            # If the character has moved, record the new position
            if initial_position != self.position:
                path_taken.append(self.position)  # Add the moved-to position
            
        self.update_sprite_position()

    def can_move(self, direction):
        # Cálculo de la nueva posición potencial basada en la dirección
        new_x, new_y = self.position
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        # Verificar si la nueva posición está dentro de los límites del mapa
        if 0 <= new_x < size_w and 0 <= new_y < size_h:
            # Verificar si la nueva posición no es una pared ('0')
            return my_map[new_y][new_x] != '0'
        return False
    
    def update_position(self, keyboard, WIDTH, HEIGHT, cell):

        if keyboard.right and self.position[0] + 1 < WIDTH // cell.width or keyboard.d and self.position[0] + 1 < WIDTH // cell.width:
            self.position = (self.position[0] + 1, self.position[1])
            self.sprite.image = 'stand'
        elif keyboard.left and self.position[0] - 1 >= 0 or keyboard.a and self.position[0] - 1 >= 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif keyboard.down and self.position[1] + 1 < HEIGHT // cell.height or keyboard.s and self.position[1] + 1 < HEIGHT // cell.height:
            self.position = (self.position[0], self.position[1] + 1)
        elif keyboard.up and self.position[1] - 1 >= 0 or keyboard.w and self.position[1] - 1 >= 0:
            self.position = (self.position[0], self.position[1] - 1)

        # Update sprite position based on the updated unit position
        self.sprite.topleft = (self.position[0] * cell.width, self.position[1] * cell.height)

    def update_sprite_position(self):
        # Update the sprite's position based on grid coordinates
        self.sprite.pos = (self.position[0] * cell.width + cell.width // 2, self.position[1] * cell.height + cell.height // 2)


# Clases:
# Protagonista 
char = Unit(name='Hero', sprite='stand', vida=100, ataque=5, defensa=3, velocidad=2, bonus = 0, position=(1, 1))

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == "0":
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif (j, i) in path_taken:  # Verificar si la posición está en path_taken
                cell2.left = cell.width*j  # cell2 tiene la imagen de 'track_down' o la imagen que indique el camino recorrido
                cell2.top = cell.height*i
                cell2.draw()
            elif my_map[i][j] == "1":
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == "2":
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == "3":
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 
            elif my_map[i][j] == "4":
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 

def victory():
    global win, mode
    # Convert character position to map grid coordinates
    char_grid_x = char.position[0] // cell.width
    char_grid_y = char.position[1] // cell.height
    
    # Check if the character is on a 'win' tile
    if my_map[char_grid_y][char_grid_x] == '4':
        win = 1
    elif char.vida <= 0:
        win = -1
    
    if win != 0:
        mode = "fin"


def draw():
    if mode == "menu":
        background.draw()
        play.draw()

    elif mode == "game":
        screen.fill("#2f3542")
        map_draw()
        char.sprite.draw() 
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(str(char.vida), center=(75, 475), color='white', fontsize=20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(str(char.ataque), center=(425, 475), color = 'white', fontsize = 20)
    elif mode == "fin":
        if win == 1:
            screen.draw.text("Felicidades has ganado", center=(200, 200), color = 'red', fontsize = 20)
            screen.draw.text("Presiona enter para no reiniciar", center=(200, 300), color = 'red', fontsize = 20)
        elif win == -1:
            screen.draw.text("Felicidades has perdido", center=(200, 200), color = 'red', fontsize = 20)
            screen.draw.text("Presiona enter para no reiniciar", center=(200, 300), color = 'red', fontsize = 20)

def update(dt):
    global old_position, initial_position, path_taken
    old_position = char.position  # Guardar la posición vieja antes de moverse, para usos futuros.
    
    direction = None
    if keyboard.right:
        direction = "right"
    elif keyboard.left:
        direction = "left"
    elif keyboard.down:
        direction = "down"
    elif keyboard.up:
        direction = "up"
    
    if direction:
        char.move(direction) 
    
def on_key_down(key):
    if keyboard.d and char.x + 50 < WIDTH - 50: # LEFT
        char.x += 50
        char.image = "stand"
    elif keyboard.a  and char.x - 50 > 50: # DERECHA
        char.x -= 50
        char.image = "run1"
    elif keyboard.w and char.y - 50 > 50: # UP
        char.y -= 50
    elif keyboard.s and char.y + 50 < HEIGHT - 50: # DOWN
        char.y += 50

# Menu change: 
def on_mouse_down(pos):
    global mode
    if mode == 'menu':
        play_button_rect = Rect((WIDTH // 2 - 64, HEIGHT // 2 - 64), (237, 126))  
        if play_button_rect.collidepoint(pos):
            mode = 'game'  # Change mode to game
    else:
        mode = 'menu'  # For demonstration, click anywhere to return to menu