import json
from pymodbus.client.sync import ModbusTcpClient as PyModbusTcpClient

class ModbusTCPClient:
    def __init__(self, ip, port=502):
        self.ip = ip
        self.port = port
        self.client = PyModbusTcpClient(ip, port=port)

    def connect(self):
        self.client.connect()

    def send_data(self, data, register_address):
        try:
            # Serialize the data to JSON
            data_json = json.dumps(data)
            # Convert the JSON data to bytes
            data_bytes = data_json.encode('utf-8')
            # Write the data to a holding register
            self.client.write_registers(register_address, [byte for byte in data_bytes])
            print("Data sent successfully.")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def close(self):
        self.client.close()

# Example usage for Modbus TCP/IP
if __name__ == "__main__":
    # Define the Modbus device's IP address
    MODBUS_IP = '0.0.0.0'
    # Define the data to be sent
    data = {
        "temperature": 25,
        "humidity": 60,
        "status": "ok"
    }
    # Create a Modbus TCP/IP client
    tcp_client = ModbusTCPClient(MODBUS_IP)
    try:
        # Connect to the Modbus TCP/IP device
        tcp_client.connect()
        # Send data to Modbus TCP/IP device
        tcp_client.send_data(data, register_address=100)
    finally:
        # Close the Modbus TCP/IP connection
        tcp_client.close()
