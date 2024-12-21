import pygame
import time

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick connected.")
    pygame.quit()
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

axis_threshold = 0.5
try:
    while True:
        # Pump the event handler to handle events such as pressing buttons
        pygame.event.pump()

        axis_0 = joystick.get_axis(0)  # Axis 0 (left-right)
        axis_1 = joystick.get_axis(1)  # Axis 1 (up-down)

        # Conditional logic based on button presses
        if joystick.get_button(0):  # If Button 0 is pressed
            print("Button 0 is pressed! Taking action A.")
            # Insert your action here for Button 0

        if joystick.get_button(1):  # If Button 1 is pressed
            print("Button 1 is pressed! Taking action B.")
            # Insert your action here for Button 1

        if joystick.get_button(2):  # If Button 2 is pressed
            print("Button 2 is pressed! Taking action C.")
            # Insert your action here for Button 2

        if joystick.get_button(3):  # If Button 3 is pressed
            print("Button 3 is pressed! Taking action D.")
            # Insert your action here for Button 3

        if joystick.get_button(4):  # If Button 3 is pressed
            print("Button 4 is pressed! Taking action e.")
            # Insert your action here for Button 3

        if joystick.get_button(5):  # If Button 3 is pressed
            print("Button 5 is pressed! Taking action q.")
            # Insert your action here for Button 3

        if joystick.get_button(9):  # If Button 3 is pressed
            print("Button 9 is pressed! Taking action start.")
            # Insert your action here for Button 3

        if axis_0 < -axis_threshold:  # Joystick pushed left
            print("Joystick moved left! Taking action Left.")
            # Insert your action for left movement (e.g., turn left)

        elif axis_0 > axis_threshold:  # Joystick pushed right
            print("Joystick moved right! Taking action Right.")
            # Insert your action for right movement (e.g., turn right)

            # Axis 1 (up-down movement)
        if axis_1 < -axis_threshold:  # Joystick pushed up
            print("Joystick moved up! Taking action Up.")
            # Insert your action for upward movement (e.g., move forward)

        elif axis_1 > axis_threshold:  # Joystick pushed down
            print("Joystick moved down! Taking action Down.")
            # Insert your action for downward movement (e.g., move backward)
        # Add conditions for more buttons as needed
        # ...

        # You can still read and print axis values, too

        # Sleep to avoid overwhelming output
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")

# Quit pygame
pygame.quit()
