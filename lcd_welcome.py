#! /usr/bin/env python3

def Welcome_LCD():
    import LCD_drivers
    from time import sleep

    display = LCD_drivers.Lcd()
    # Main body of code
    #while True:
        # Remember that your sentences can only be 16 characters long!
    print("Writing to display")
    display.lcd_clear()
    display.lcd_display_string(" !! WELCOME !! ", 1)  # Write line of text to first line of display
    display.lcd_display_string("Initializing...", 2)  # Write line of text to second line of display
    sleep(0.2)
    #exit(1)
    #except KeyboardInterrupt:
        #If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        #display.lcd_clear()