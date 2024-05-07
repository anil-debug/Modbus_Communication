from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ModbusIOException

class ModbusRTUOVERTCPClient:
    def __init__(self, server_ip, port=502):
        """
        Initialize the Modbus RTU over TCP client.

        Args:
            server_ip (str): The IP address of the Modbus TCP server.
            port (int, optional): The port number of the Modbus TCP server (default 502).
        """
        self.client = ModbusClient(server_ip, port)

    def connect(self):
        """
        Connect to the Modbus TCP server.
        """
        self.connection = self.client.connect()

    def read_registers(self, start_address, count, slave_id=1):
        """
        Read a specified number of registers from the Modbus TCP server.

        Args:
            start_address (int): The starting address of the registers to read.
            count (int): The number of registers to read.
            slave_id (int, optional): The slave ID of the Modbus device (default 1).

        Returns:
            list or None: A list containing the read register values if successful, otherwise None.
        """
        try:
            response = self.client.read_holding_registers(start_address, count, unit=slave_id)
            if response.isError():
                print("Modbus Error:", response)
                return None
            else:
                return response.registers
        except ModbusIOException as e:
            print("Modbus IO Exception:", e)
            return None
        except Exception as e:
            print("An error occurred during reading:", e)
            return None

    def write_registers(self, start_address, values, slave_id=1):
        """
        Write a list of values to specified registers on the Modbus TCP server.

        Args:
            start_address (int): The starting address of the registers to write to.
            values (list): A list containing the values to be written.
            slave_id (int, optional): The slave ID of the Modbus device (default 1).

        Returns:
            bool: True if writing was successful, False otherwise.
        """
        try:
            response = self.client.write_registers(start_address, values, unit=slave_id)
            if response.isError():
                print("Modbus Error:", response)
                return False
            else:
                print("Data written to registers successfully")
                return True
        except ModbusIOException as e:
            print("Modbus IO Exception:", e)
            return False
        except Exception as e:
            print("An error occurred during writing:", e)
            return False

    def close(self):
        """
        Close the connection to the Modbus TCP server.
        """
        self.client.close()

if __name__ == "__main__":
    # Example usage
    client = ModbusRTUOVERTCPClient('0.0.0.0', port=502)  # Replace with your Modbus TCP server IP address and port
    client.connect()

    # Read 4 registers starting from address 104
    read_data = client.read_registers(104, 4)
    if read_data is not None:
        print("Read data:", read_data)

    # Write a list of values (replace with your desired values)
    write_data = [True, 20, 30, 40]
    write_success = client.write_registers(104, write_data)
    if write_success:
        print("Write operation successful")

    # Remember to close the connection
    client.close()
