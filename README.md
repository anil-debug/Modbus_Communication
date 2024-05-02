# Modbus Communication README

This repository contains two Python files for communicating with Modbus devices using different protocols: Modbus TCP/IP and Modbus RTU.

## Files

### 1. modbus_communication_tcp.py

This file provides a Python class `ModbusTCPClient` for communicating with Modbus devices over TCP/IP protocol.

#### Usage:

1. Ensure you have the required Python packages installed: `pymodbus`.

2. Modify the `MODBUS_IP` variable in the usage example to match the IP address of your Modbus device.

3. Run the script to send data to the Modbus TCP/IP device.

### 2. modbus_communication_rtu.py

This file provides a Python class `ModbusRTUClient` for communicating with Modbus devices over RTU (Remote Terminal Unit) protocol.

#### Usage:

1. Ensure you have the required Python packages installed: `pymodbus`.

2. Modify the `port` variable in the usage example to match the serial port connected to your Modbus RTU device.

3. If your Modbus RTU device requires a specific slave address, you need to set it in the `slave_address` parameter of the `ModbusRTUClient` class initialization. This address corresponds to the Modbus device's address on the RS-485 network. For example:
   
    ```python
    # Create an instance of the ModbusRTUClient class
    modbus_client = ModbusRTUClient(port='COM2', slave_address=1)
    ```

4. Run the script to read and write data to the Modbus RTU device.
### 3. modbus_communication_rtu_overtcp.py

This file provides a Python class `ModbusRTUOVERTCPClient` for communicating with Modbus devices over RTU (Remote Terminal Unit) protocol via TCP/IP.

#### Usage:

1. Ensure you have the required Python packages installed using the provided `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
2. Modify the server_ip variable in the usage example to match the IP address of your Modbus TCP server.
3. Run the script to read and write data to the Modbus RTU device over TCP/IP.
---

Feel free to update the scripts and usage examples as needed for your specific Modbus devices and configurations.
