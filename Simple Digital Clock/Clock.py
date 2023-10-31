import datetime
import time

while True:
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Clear the console (optional, for a cleaner display)
    # You can skip this part if you're not working in a terminal/console.
    import os
    os.system("cls" if os.name == "nt" else "clear")

    # Display the formatted date and time
    print("Current Date and Time:", formatted_datetime)

    # Wait for a second before updating the display
    time.sleep(1)
