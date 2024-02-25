#pgzero
import random, time

# Actores y variables globales, estructura de datos
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("track_down")  # el camino que deja
cell3 = Actor("muerte")
cell4 = Actor("win")

# Configuracion de pantalla
size_w = 51
size_h = 28
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
TITLE = "minimalist_square_game"
FPS = 30

# Tracking movement 
path_taken = []  # Se guarda por que casillas a pasado el jugador

# Game mode
mode = "game"
win = 0
current_player = 1

# Timer setup
start_time = time.time()
duration = 60  # cuanto dura el timer

# Coordenadas
old_position = (0, 0)
old_x = 0
old_y = 0       
             #1   #2   #3   #4   #5   #6   #7   #8   #9   #10  #11  #12  #13  #14   #15 #16  #17  #18  #19  #20  #21  #22  #23  #24  #25  #26  #27  #28  #29  #30  #31  #32  #33  #34  #35 #36  #37  #38  #39  #40   #40  #41  #42  #43  #44  #45 #46  #47  #48  #49  #51 
my_map = [  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], #1
            ['0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0'], #3
            ['0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #4
            ['0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'], #5
            ['0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'], #6
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0'], #7
            ['0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'], #8
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'], #9
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #10
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #11
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #12
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #13
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #14
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #15
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #1
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #3
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #4
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #5
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #6
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #7
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #8
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #9
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #10
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #11
            ['0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #12
            ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'], #13
            ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0'], #14
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']] #15
                      

#Unit Class Definitions
initial_position = 0
class Unit:
    def __init__(self, name, sprite, vida, ataque, defensa, velocidad, bonus, position=(0, 0), abilities=[]):
        self.name = name
        # se asegura de que el actor y el sprite son los mismo
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
        # Actualiza la posicion del sprite
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
        global old_position
        old_position = char.position  # Save the old position before moving
    
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
            check_win_condition()  # Check if the player has won after moving
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

    def move_unit_in_direction(unit, direction):
        # Keep moving in the direction until a boundary or non-movable tile is reached
        global path_taken
        while unit.can_move(direction):
            # Update the unit's position based on the direction
            new_x, new_y = unit.position
            if direction == "up":
                new_y -= 1
            elif direction == "down":
                new_y += 1
            elif direction == "left":
                new_x -= 1
            elif direction == "right":
                new_x += 1
            # Set the new position
            unit.position = (new_x, new_y)
            path_taken.append(unit.position)  # Add the new position to the path taken
            # Update the sprite position to reflect the new location
            unit.update_sprite_position()

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
                
total_floor_tiles = sum(row.count('1') for row in my_map)

def check_win_condition():
    global win, mode
    # Calcula el numero de casillas por los que has pasado
    unique_tiles_covered = len(set(path_taken))

    # checha si ya has pasado por todas las casillas para que ganes.
    if unique_tiles_covered >= total_floor_tiles:
        win = 1
        mode = "fin"

def check_for_death():
    global win, mode
    # Obtener la posicion del jugador
    grid_x, grid_y = char.position
    # te mata si la casilla en la que estas es igual a 3
    if my_map[grid_y][grid_x] == '3':
        win = -1
        mode = "fin"

def draw():
    if mode == "menu":
        screen.fill("#4397b3")
        screen.draw.text("Minimalist_square_game", center=(WIDTH // 2 - 20, HEIGHT // 2  - 40), color='white', fontsize=40)
        screen.draw.text("Presiona enter para empezar el juego", center=(WIDTH // 2, HEIGHT // 2), color='white', fontsize=40)
    elif mode == "game":
        screen.fill("#4397b3")
        map_draw()
        char.sprite.draw() 
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = int(max(duration - elapsed_time, 0))
        screen.draw.text(f"Tiempo: {remaining_time}", center=(WIDTH // 2, 25), color='white', fontsize=20)
    elif mode == "fin":
        if win == 1:
            screen.draw.text("Ganaste", center=(WIDTH // 2, HEIGHT // 2), color='red', fontsize=40)
        elif win == -1:
            screen.fill("#4397b3")
            screen.draw.text("Game Over: Te moriste !", center=(WIDTH // 2, HEIGHT // 2), color='white', fontsize=40)
            screen.draw.text("Presiona enter para volver al menu", center=(WIDTH // 2, HEIGHT // 2 + 50), color='white', fontsize=20)

def update(dt):
    global mode, win, start_time
    if mode == "game":
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(duration - elapsed_time, 0)

        if remaining_time <= 0 and mode == "game":
            win = -1
            mode = "fin"

    # Controles, logica del movimieto
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
        char.move_unit_in_direction(direction)  # Adjusta el metodo
        check_win_condition()  # Revisa si ya ganaste
        check_for_death()  # Si ya te has chocado con "muerte" 

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
        char.move_unit_in_direction(direction) # Adjusta el metodo
        check_win_condition()  # Revisa si ya ganaste
    
def on_key_down(key):
    global mode, start_time
    if key == keys.RETURN:  # SI key esta presionada
        if mode == 'menu':
            mode = 'game'  # Switch to game mode
            start_time = time.time()  # Reset the start time
        elif mode == 'game' or mode == 'fin':  # Regresar al menu
            mode = 'menu'
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