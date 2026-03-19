import arcade
import random
SPRITE_SCALING_PLAYER = 0.25
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_POISON=0.1
COIN_COUNT = 50
POISON_COUNT=50
delta_time=3


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

class Coin(arcade.Sprite):
    def update(self, delta_time=1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1
class Poison(arcade.Sprite):
    def update(self, delta_time=1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.player_list=None
        self.coin_list=None
        self.poison_list=None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BANANA_YELLOW)
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.poison_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("coins.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)
        for i in range(POISON_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            poison = Poison("poison.png", SPRITE_SCALING_POISON)

            # Position the coin
            poison.center_x = random.randrange(SCREEN_WIDTH)
            poison.center_y = random.randrange(SCREEN_HEIGHT)
            poison.change_x = random.randrange(-3, 4)
            poison.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.poison_list.append(poison)
    

    def on_draw(self):
        self.clear()
    # Draw the sprite lists here. Typically sprites are divided into
        # different groups. Other game engines might call these "sprite layers"
        # or "sprite groups." Sprites that don't move should be drawn in their
        # own group for the best performance, as Arcade can tell the graphics
        # card to just redraw them at the same spot.
        # Try to avoid drawing sprites on their own, use a SpriteList
        # because there are many performance improvements in that code.
        self.coin_list.draw()
        self.player_list.draw()
        self.poison_list.draw()
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.coin_list)==0:
            arcade.draw_text("GAME OVER",SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED,50,anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.poison_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        poison_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.poison_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        for poison in poison_hit_list:
            poison.remove_from_sprite_lists()
            self.score -= 1

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
