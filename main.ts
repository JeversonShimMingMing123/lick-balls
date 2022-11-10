input.onButtonPressed(Button.A, function () {
    zoombit.move(MotorDirection.Forward, 128)
    basic.pause(3800)
    zoombit.brake()
    rekabit.setRgbPixelColor(0, 0x000000)
    basic.pause(100)
    rekabit.setAllRgbPixelsColor(0x00ffff)
    rekabit.setAllRgbPixelsColor(0x000000)
    for (let index = 0; index < 4; index++) {
        rekabit.setRgbPixelColor(0, 0xff8000)
        basic.pause(100)
    }
    zoombit.turn(TurnDirection.Right, 128)
    basic.pause(650)
    zoombit.brake()
    zoombit.move(MotorDirection.Forward, 132)
    basic.pause(2000)
    zoombit.brake()
    for (let index = 0; index < 4; index++) {
        rekabit.setRgbPixelColor(0, 0xff8000)
        basic.pause(100)
        rekabit.setRgbPixelColor(0, 0x000000)
        basic.pause(100)
    }
    zoombit.turn(TurnDirection.Right, 128)
    basic.pause(500)
    zoombit.move(MotorDirection.Forward, 128)
    basic.pause(2000)
    zoombit.brake()
    music.playMelody("A B A B A B A B ", 120)
})
basic.showString("Bog bog")
rekabit.clearAllRgbPixels()
basic.forever(function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        # # . # #
        # # . # #
        `)
})
