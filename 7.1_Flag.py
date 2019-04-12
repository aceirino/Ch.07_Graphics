import arcade
arcade.open_window(494,260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y_offset in range(0,260,40):
    arcade.draw_lrtb_rectangle_filled(0,494,y_offset+20,y_offset+0,arcade.color.RED)
arcade.draw_rectangle_filled(98.8,195,197.6,150,arcade.color.BLUE)
for i in range(0,125,30):
    arcade.draw_text("*   *   *   *   *   *",16.38,231.92-i,arcade.color.WHITE,20)
for y in range(0,91,30):
    arcade.draw_text("  *   *   *   *   *   ",17,216.92-y,arcade.color.WHITE,20)
arcade.finish_render()
arcade.run()