import logging
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModbusCommunicator:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, parity='O', timeout=1):
        self.client = ModbusClient(method='rtu', port=port, baudrate=baudrate, parity=parity, timeout=timeout)

    def connect(self):
        """
        Connects to the Modbus slave device.
        
        Returns:
            True if connection is successful, False otherwise.
        """
        try:
            return self.client.connect()
        except Exception as e:
            logger.error("Connection failed: %s", e)
            return False

    def read_holding_registers(self, start_address, count, slave_id=1):
        """
        Reads data from holding registers of the Modbus slave device.
        
        Args:
            start_address (int): Starting address of the registers to read.
            count (int): Number of registers to read.
            slave_id (int, optional): Slave ID of the device (default: 1).
        
        Returns:
            list: List of read register values or None if an error occurs.
        """
        try:
            response = self.client.read_holding_registers(start_address, count, unit=slave_id)
            if response.isError():
                logger.error("Modbus error response: %s", response)
                return None
            else:
                return response.registers
        except Exception as e:
            logger.error("An error occurred during Modbus read: %s", e)
            return None

    def write_holding_registers(self, start_address, data, slave_id=1):
        """
        Writes data to holding registers of the Modbus slave device.
        
        Args:
            start_address (int): Starting address of the registers to write.
            data (list): List of data values to write.
            slave_id (int, optional): Slave ID of the device (default: 1).
        
        Returns:
            True if write operation is successful, False otherwise.
        """
        try:
            write_response = self.client.write_registers(start_address, data, unit=slave_id)
            if write_response.isError():
                logger.error("Modbus error response: %s", write_response)
                return False
            else:
                logger.info("Data written to holding registers: %s", data)
                return True
        except Exception as e:
            logger.error("An error occurred during Modbus write: %s", e)
            return False

    def close(self):
        """
        Closes the Modbus connection.
        """
        try:
            self.client.close()
            logger.info("Connection closed")
        except Exception as e:
            logger.error("Error occurred while closing connection: %s", e)

if __name__ == "__main__":
    # Create a ModbusCommunicator object with desired settings (optional)
    communicator = ModbusCommunicator(port='/dev/ttyUSB0', baudrate=9600, parity='O', timeout=1)
    connection_status = communicator.connect()
    if connection_status:
        logger.info("Connected to Modbus slave device!")
    else:
        logger.error("Connection failed. Please check the communication settings.")
        # Handle connection error (e.g., exit program)
    # Define the data you want to write
    write_data = [10, 20, 30, False, True]  # Example data (adjust data types as needed)
    write_success = communicator.write_holding_registers(start_address=1, data=write_data, slave_id=1)
    if write_success:
        logger.info("Data written successfully to holding registers!")
        # Read from holding registers after writing
        read_data = communicator.read_holding_registers(start_address=1, count=len(write_data))
        if read_data is not None:
            logger.info("Data read successfully from holding registers: %s", read_data)
        else:
            logger.error("Failed to read data from holding registers after write operation.")
    else:
        logger.error("Write operation failed. Check for errors.")
        # Handle write error (e.g., retry, log the error)

    # Close the Modbus connection
    communicator.close()
