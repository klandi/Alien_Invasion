# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from alien_invasion import AlienInvasion


def print_message(msg):
    # Use a breakpoint in the code line below to debug your script.
    print(f'ALERT: {msg}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_message('Starting Alien Invasion')
    ai = AlienInvasion()
    ai.run_game()
