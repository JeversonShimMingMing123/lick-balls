def on_button_pressed_a():
    zoombit.move(MotorDirection.FORWARD, 128)
    basic.pause(3800)
    zoombit.brake()
    rekabit.set_rgb_pixel_color(0, 0x000000)
    basic.pause(100)
    rekabit.set_all_rgb_pixels_color(0x00ffff)
    rekabit.set_all_rgb_pixels_color(0x000000)
    for index in range(4):
        rekabit.set_rgb_pixel_color(0, 0xff8000)
        basic.pause(100)
    zoombit.turn(TurnDirection.RIGHT, 128)
    basic.pause(650)
    zoombit.brake()
    zoombit.move(MotorDirection.FORWARD, 132)
    basic.pause(2000)
    zoombit.brake()
    for index2 in range(4):
        rekabit.set_rgb_pixel_color(0, 0xff8000)
        basic.pause(100)
        rekabit.set_rgb_pixel_color(0, 0x000000)
        basic.pause(100)
    zoombit.turn(TurnDirection.RIGHT, 128)
    basic.pause(500)
    zoombit.move(MotorDirection.FORWARD, 128)
    basic.pause(2000)
    zoombit.brake()
    music.play_melody("A B A B A B A B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    zoombit.move(MotorDirection.FORWARD, 128)
    basic.pause(3800)
    zoombit.brake()
    rekabit.set_rgb_pixel_color(0, 0x000000)
    basic.pause(100)
    rekabit.set_all_rgb_pixels_color(0x00ffff)
    rekabit.set_all_rgb_pixels_color(0x000000)
    for index3 in range(4):
        rekabit.set_rgb_pixel_color(1, 0xff8000)
        basic.pause(100)
    zoombit.turn(TurnDirection.LEFT, 128)
    basic.pause(650)
    zoombit.brake()
    zoombit.move(MotorDirection.FORWARD, 132)
    basic.pause(2000)
    zoombit.brake()
    for index4 in range(4):
        rekabit.set_rgb_pixel_color(1, 0xff8000)
        basic.pause(100)
        rekabit.set_rgb_pixel_color(1, 0x000000)
        basic.pause(100)
    zoombit.turn(TurnDirection.LEFT, 128)
    basic.pause(500)
    zoombit.move(MotorDirection.FORWARD, 128)
    basic.pause(2000)
    zoombit.brake()
    music.play_melody("A B A B A B A B ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Bog bog")
rekabit.clear_all_rgb_pixels()

def on_forever():
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                # # # # #
                # # # # #
    """)
basic.forever(on_forever)
