#Emilie Mancera

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# On crée laliste des couleurs
COLORS = [arcade.color.BRILLIANT_ROSE, arcade.color.BUBBLE_GUM, arcade.color.AMBER, arcade.color.ALICE_BLUE, arcade.color.ALMOND, arcade.color.ANTIQUE_WHITE, arcade.color.BRIGHT_LILAC, arcade.color.BLUE_VIOLET]

class Balle:
    def __init__(self, position_x, position_y, change_x, change_y, rayon, color):
        #On determine les attributs de la classe Balle
        self.x = position_x
        self.y = position_y
        self.vx = change_x
        self.vy = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        #On cree la variable pour que les balles bougent
        self.x += self.vx
        self.y += self.vy
        if self.x < self.rayon:
            self.vx *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            self.vx *= -1
        if self.y < self.rayon:
            self.vy *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.vy *= -1

    def draw(self):
        #on cree la variable pour dessiner les balles
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
    # on determine les attributs aux rectangles
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color, angle):
        self.x = position_x
        self.y = position_y
        self.vx = change_x
        self.vy = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0

    def update(self):
        # on cree la variable pour que les rectangles bougent
        arcade.start_render()
        self.x += self.vx
        self.y += self.vy
        if self.x < self.width/2:
            self.vx *= -1
        if self.x > SCREEN_WIDTH - self.width/2:
            self.vx *= -1
        if self.y < self.height/2:
            self.vy *= -1
        if self.y > SCREEN_HEIGHT - self.height/2:
            self.vy *= -1


    def draw(self):
        # on cree la variable pour dessiner les rectangles
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    #on cree la fenetre et on definit les objets pour permettre de creer le jeu
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.liste_balles = []
        self.liste_rectangles = []

    def on_draw(self):
        # methode pour que les dessins saffichent a lecran
        arcade.start_render()
        for balles in self.liste_balles:
            balles.draw()
        for rectangles in self.liste_rectangles:
            rectangles.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        #quand on clique = une balle/rectangle apparait
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(10, 30)
            color = random.choice(COLORS)
            balles = Balle( x, y, 3, 3, rayon, color)
            self.liste_balles.append(balles)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            color = random.choice(COLORS)
            width = 50
            height = 30
            angle = 0
            rectangles = Rectangle(x, y, 3, 3, width, height, color, angle)
            self.liste_rectangles.append(rectangles)

    def on_update(self, delta_time: float):
        for balles in self.liste_balles:
            balles.update()
        for rectangles in self.liste_rectangles:
            rectangles.update()

def main():
    MyGame()
    arcade.run()

main()