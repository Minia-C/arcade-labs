"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(900, 600, "Drawing Example")
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
# Set the background color

def __initial__():
 super().__init__(900, 600, "Drawing Example")
 arcade.set_background_color(arcade.color.BABY_BLUE)
 arcade.start_render()
 arcade.draw_rect_filled(arcade.XYWH(450, 390, 100, 120),arcade.color.CHINA_ROSE)
 arcade.draw_circle_filled(450, 500, 60, arcade.color.BANANA_YELLOW)
 arcade.draw_circle_filled(430, 500, 10, arcade.color.BLACK)
 arcade.draw_circle_filled(470, 500, 10, arcade.color.BLACK)
 arcade.draw_rect_filled(arcade.XYWH(425, 280, 40, 120),arcade.color.CHINA_ROSE)
 arcade.draw_rect_filled(arcade.XYWH(475, 280, 40, 120),arcade.color.CHINA_ROSE)
 arcade.draw_rect_filled(arcade.XYWH(425, 200, 45, 40),arcade.color.BLACK)
 arcade.draw_rect_filled(arcade.XYWH(475, 200, 45, 40),arcade.color.BLACK)
 arcade.finish_render()
arcade.run()
def on_draw(self):
 self.clear()
 super().__init__(900, 600, "Drawing Example")
 arcade.set_background_color(arcade.color.BABY_BLUE)
 arcade.start_render()
 arcade.draw_rect_filled(arcade.XYWH(450, 390, 100, 120),arcade.color.CHINA_ROSE)
 arcade.draw_circle_filled(450, 500, 60, arcade.color.BANANA_YELLOW)
 arcade.draw_circle_filled(450, 500, 10, arcade.color.BLACK)
 arcade.draw_rect_filled(arcade.XYWH(450, 280, 40, 120),arcade.color.CHINA_ROSE)
 arcade.draw_rect_filled(arcade.XYWH(475, 200, 45, 40),arcade.color.BLACK)
 arcade.finish_render()
arcade.run()
if __name__ == "__initial__":
    juego = ()



# Keep the window up until someone closes it.
arcade.finish_render()
arcade.run()