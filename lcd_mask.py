#! /usr/bin/env python3

def mask_LCD():
    import LCD_drivers
    from time import sleep

    display = LCD_drivers.Lcd()
    # Main body of code

    print("Writing mask found")
    display.lcd_clear()
    display.lcd_display_string("   MASK FOUND   ", 1)  # Write line of text to first line of display
    display.lcd_display_string(" You may enter  ", 2)  # Write line of text to second line of display
    sleep(.5)

