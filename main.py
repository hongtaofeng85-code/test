def on_forever():
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.SMALL_SQUARE)
basic.forever(on_forever)
