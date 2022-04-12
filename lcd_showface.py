#! /usr/bin/env python3

def ShowFace_LCD():
    import LCD_drivers
    from time import sleep

    display = LCD_drivers.Lcd()
    # Main body of code

    print("Writing show face")
    display.lcd_clear()
    display.lcd_display_string("  Please  show  ", 1)  # Write line of text to first line of display
    display.lcd_display_string("   your  face   ", 2)  # Write line of text to second line of display
    sleep(1)
    #display.lcd_clear()

