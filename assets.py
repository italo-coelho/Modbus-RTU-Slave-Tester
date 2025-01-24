def print_header():
    print("  __  __           _ _                 ____ _____ _   _ ")
    print(" |  \/  | ___   __| | |__  _   _ ___  |  _ \_   _| | | |")
    print(" | |\/| |/ _ \ / _` | '_ \| | | / __| | |_) || | | | | |")
    print(" | |  | | (_) | (_| | |_) | |_| \__ \ |  _ < | | | |_| |")
    print(" |_|  |_|\___/ \__,_|_.__/ \__,_|___/ |_| \_\|_|  \___/ ")
    print("\n")

def print_help():
    print()
    print(f"{'Command':<15} {'Description':<25}")
    print(f"{'-------':<15} {'-----------':<25}")
    print(f"{'port':<15} {'List and select serial ports':<25}")
    print(f"{'id':<15} {'Set modbus slave ID':<25}")
    print(f"{'baudrate':<15} {'Set serial communication speed':<25}")
    print(f"{'connect':<15} {'Configure slave device from current parameters':<25}")
    print(f"{'param':<15} {'List current parameters':<25}")
    print(f"{'back':<15} {'Return to main menu':<25}")
    print(f"{'exit':<15} {'Close this program':<25}")
    print()




if __name__ == "__main__":
    # print_header()
    print_help()