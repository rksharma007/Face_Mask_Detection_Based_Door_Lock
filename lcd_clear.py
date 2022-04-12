#! /usr/bin/env python3

def clear_LCD():
    import LCD_drivers
    from time import sleep

    display = LCD_drivers.Lcd()
    # Main body of code
    print("Clearing LCD display")
    display.lcd_clear()
    #sleep(1)
    #display.lcd_clear()