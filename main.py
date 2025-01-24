import time
import serial
import minimalmodbus
import serial.tools.list_ports

from assets import *

port = ""
baudrate = -1
slave_id = -1

slave = None


def select_port():
    global port
    ports = serial.tools.list_ports.comports()
    print()
    print(f"{'Num.':<5} {'Port':<35} {'Description'}")
    print(f"{'----':<5} {'----':<35} {'-----------'}")
    i = 0
    for p in ports:
        print(f"{i+1:<5} {p.device:<35} ({p.description})")
        i += 1
    print()
    print("Select port number:")
    selected = int(input("> "))
    port = ports[selected-1].device
    print()


def select_id():
    global slave_id
    print()
    print("Type slave ID:")
    slave_id = int(input("> "))
    print()


def select_baud():
    global baudrate
    print()
    print("Type baudrate:")
    baudrate = int(input("> "))
    print()


def setup_slave():
    global slave
    instrument = minimalmodbus.Instrument(port, slave_id)
    instrument.serial.baudrate = baudrate
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1

    slave = instrument


def write_holding(address, value):
    global slave
    try:
        slave.write_register(address, value)
    except minimalmodbus.NoResponseError:
        return False
    except minimalmodbus.InvalidResponseError as e:
        return False
    except Exception as e:
        return False
    return True


def read_holding(address):
    global slave
    try:
        value = slave.read_register(address, 0, functioncode=3)
    except minimalmodbus.NoResponseError:
        value = -1
    except minimalmodbus.InvalidResponseError as e:
        value = -1
    except Exception as e:
        value = -1
    return value


def read_input(address):
    global slave
    try:
        value = slave.read_register(address, 0, functioncode=4)
    except minimalmodbus.NoResponseError:
        value = -1
    except minimalmodbus.InvalidResponseError as e:
        value = -1
    except Exception as e:
        value = -1
    return value


def list_param():
    print()
    print(f'{"Param.":<15} {"Value"}')
    print(f'{"------":<15} {"-----"}')
    print(f'{"port":<15} {port if port != "" else "None"}')
    print(f'{"id":<15} {slave_id if slave_id > 0 else "None"}')
    print(f'{"baudrate":<15} {baudrate if baudrate > 0 else "None"}')
    print()




if __name__ == "__main__":
    print_header()

    try:
        while(1):
            command = input("> ")
            command = command.lower()

            if(command == "exit"):
                break

            if(command == "help"):
                print_help()
            
            if(command == "param"):
                list_param()
            
            if(command == "port"):
                select_port()
            
            if(command == "id"):
                select_id()
            
            if(command == "baudrate"):
                select_baud()
            
            if(command == "connect"):
                if(port == ""):
                    select_port()
                if(slave_id <= 0):
                    select_id()
                if(baudrate <= 0):
                    select_baud()
                
                setup_slave()
                print("Connected!")
                print()
            
            if(command == "write"):
                if(slave == None):
                    print("Error: No slave device!")
                    print()
                    continue
                print()
                print("Type holding register address:")
                response = input("> ")
                if(response == "back"): continue
                else: address = int(response)
                print("Type value to write:")
                response = input("> ")
                if(response == "back"): continue
                else: value = int(response)
                if(write_holding(address, value)): print("Success!")
                else: print("Fail!")
                print()
            
            if(command == "read"):
                if(slave == None):
                    print("Error: No slave device!")
                    print()
                    continue
                print()
                print("Type input register address:")
                response = input("> ")
                if(response == "back"): continue
                else: address = int(response)
                data = read_input(address)
                if(data >= 0): print(f'IN[{address}] --> {data}')
                else: print("Fail!")
                print()

    except:
        pass
    
    print()
    print("------------")
    print("Ítalo Coelho")
    print("2025")