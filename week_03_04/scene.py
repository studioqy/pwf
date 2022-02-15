'''
Week 4 Assignment Scenery
Displays nice pleasant scenery
May 15 2021
'''
import tkinter as tk
from math import ceil


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_sky(canvas)
    #draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    grass_x = 0
    grass_y = 300
    grass_height = 20
    grass_color = "chartreuse4"
    grass_range = int(ceil(scene_right/(grass_height*2)))
    draw_cloud(canvas, 40, 50, 320, 150, "white smoke")
    draw_cloud(canvas, 180, 115, 370, 180, "white smoke")
    draw_cloud(canvas, 580, 145, 920, 265, "gainsboro")
    draw_cloud(canvas, 530, 130, 700, 200, "gray91")
    draw_cloud(canvas, 400, 35, 600, 90, "snow")
    draw_tree(canvas, 370, 200, 390, 300, 300, 160, 440,
              260, 340, 145, 480, 230, 370, 200, 463, 245)
    draw_grass(canvas, scene_right, grass_range, grass_x,
               grass_y, grass_height, grass_color)
    draw_grass(canvas, scene_right, grass_range,
               grass_x, 350, grass_height, "chartreuse3")
    draw_grass(canvas, scene_right, grass_range,
               grass_x, 400, grass_height, "chartreuse2")
    draw_grass(canvas, scene_right, grass_range,
               grass_x, 450, grass_height, "chartreuse1")
    #draw_cloud(canvas, cloud_x, cloud_y, cloud_x1, cloud_x2, cloud_color)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
                            trunk_right, trunk_bottom,
                            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
                          skirt_right, skirt_bottom,
                          skirt_left, skirt_bottom,
                          outline="gray20", width=1, fill="dark green")


def draw_sky(canvas):
    canvas.create_rectangle(0, 0, 800, 500, fill="sky blue")
# Call the main function so that
# this program will start executing.


def draw_grass(canvas, width, grass_range, grass_x, grass_y, grass_height, grass_color):
    for i in range(grass_range):
        grass_x2 = grass_x + grass_height
        grass_y2 = grass_y - grass_height
        grass_x3 = grass_x2 + grass_height
        canvas.create_polygon(grass_x, grass_y, grass_x2, grass_y2,
                              grass_x3, grass_y, grass_x3, 500, 0, 500, fill=grass_color)
        grass_x = grass_x3


def draw_cloud(canvas, cloud_x, cloud_y, cloud_x2, cloud_y2, cloud_color):
    canvas.create_oval(cloud_x, cloud_y, cloud_x2, cloud_y2,
                       fill=cloud_color, outline=cloud_color)


def draw_tree(canvas, trunk_x, trunk_y, trunk_x2, trunk_y2, leaf1_x, leaf1_y, leaf1_x2, leaf1_y2, leaf2_x, leaf2_y, leaf2_x2, leaf2_y2, leaf3_x, leaf3_y, leaf3_x2, leaf3_y2):
    canvas.create_rectangle(trunk_x, trunk_y, trunk_x2,
                            trunk_y2, fill="sienna4", outline="sienna4")
    canvas.create_rectangle(leaf1_x, leaf1_y, leaf1_x2,
                            leaf1_y2, fill="green4", outline='green4')
    canvas.create_rectangle(leaf2_x, leaf2_y, leaf2_x2,
                            leaf2_y2, fill="green3", outline='green3')
    canvas.create_rectangle(leaf3_x, leaf3_y, leaf3_x2,
                            leaf3_y2, fill="green2", outline='green2')


main()
