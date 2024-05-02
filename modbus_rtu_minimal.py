import minimalmodbus

class ModbusConnection:
    def __init__(self, port, slave_address, baudrate=9600, parity='O', timeout=1):
        """
        Initialize ModbusConnection class with serial port parameters and slave address.

        Parameters:
        - port: The serial port name (e.g., '/dev/ttyUSB0').
        - slave_address: The Modbus slave address (unit ID).
        - baudrate: Baud rate for serial communication (default: 9600).
        - parity: Parity setting for serial communication (default: 'O' for Odd parity).
        - timeout: Timeout value for serial communication in seconds (default: 1).
        """
        self.port = port
        self.slave_address = slave_address
        self.baudrate = baudrate
        self.parity = parity
        self.timeout = timeout

    def connect(self):
        """
        Connect to the Modbus slave device.
        """
        self.instrument = minimalmodbus.Instrument(self.port, self.slave_address)
        self.instrument.serial.baudrate = self.baudrate
        self.instrument.serial.parity = self.parity
        self.instrument.serial.timeout = self.timeout

    def write_data_to_registers(self, data, start_address=0):
        """
        Write data to holding registers of the Modbus slave device.

        Parameters:
        - data: List or tuple containing data to be written to registers.
        - start_address: Starting address in the Modbus register where the data will be written (default: 0).
        """
        try:
            # Open the serial port
            # self.instrument.serial.open()

            # Write data to holding registers
            self.instrument.write_registers(start_address, data)

            print("Data written to holding registers:", data)

        except Exception as e:
            print("An error occurred during Modbus communication:", e)

        finally:
            # Close the serial port
            self.instrument.serial.close()
if __name__ == "__main__":
    # Define the serial port parameters
    port = '/dev/ttyUSB0'
    baudrate = 9600
    parity = 'O'
    timeout = 1

    # Create Modbus connection object
    modbus_connection = ModbusConnection(port, 1, baudrate, parity, timeout)

    # Connect to the Modbus slave
    modbus_connection.connect()

    # Write data to holding registers
    write_data = [10, 20, 30, False, True]  # Example data to write
    modbus_connection.write_data_to_registers(write_data)
