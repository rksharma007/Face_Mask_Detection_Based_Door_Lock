#! /usr/bin/env python3

def nomask_LCD():
    import LCD_drivers
    from time import sleep

    display = LCD_drivers.Lcd()
    # Main body of code

    print("Writing nomask found")
    display.lcd_clear()
    display.lcd_display_string(" NO MASK FOUND! ", 1)  # Write line of text to first line of display
    display.lcd_display_string("PUT YOUR MASK ON", 2)  # Write line of text to second line of display
    sleep(.5)


