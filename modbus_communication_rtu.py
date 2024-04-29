from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusIOException

class ModbusRTUClient:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.client = ModbusClient(method='rtu', port=port, baudrate=baudrate, timeout=timeout)

    def connect(self):
        try:
            self.client.connect()
            print("Connected to Modbus RTU device")
        except Exception as e:
            print("Error occurred while connecting to Modbus RTU device:", e)

    def write_registers(self, address, values, slave_address=1):
        try:
            response = self.client.write_registers(address, values, unit=slave_address)
            if response.isError():
                print("Error writing to registers:", response)
                return False
            else:
                print("Data written to registers successfully")
                return True
        except ModbusIOException as e:
            print("Modbus IO Error:", e)
            return False

    def read_registers(self, address, count, slave_address=1):
        try:
            response = self.client.read_holding_registers(address, count, unit=slave_address)
            if response.isError():
                print("Error reading registers:", response)
                return None
            else:
                return response.registers
        except ModbusIOException as e:
            print("Modbus IO Error occurred:", e)
            return None

    def close(self):
        self.client.close()
        print("Connection closed")

# Usage example
if __name__ == "__main__":
    # Create an instance of the ModbusRTUClient class
    modbus_client = ModbusRTUClient(port='COM2')

    # Connect to the Modbus RTU device
    modbus_client.connect()

    # Read from Modbus registers
    registers = modbus_client.read_registers(address=1, count=4)
    if registers is not None:
        print("Data read from registers:", registers)

    # Write to Modbus registers
    write_data = [True, 12345]  # Example write data
    if modbus_client.write_registers(address=4, values=write_data):
        print("Data written to registers successfully")

    # Close the connection
    modbus_client.close()
