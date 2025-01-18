# Weight Reading Script for MK10 with Prolific Driver

This script reads stable weight data from an MK10 scale connected via a serial port using the Prolific driver. It processes raw data received from the scale, filters out invalid readings, and returns a stable weight measurement.

---

## Features
- **Serial Communication**: Connects to the MK10 scale via a specified COM port.
- **Stable Weight Detection**: Filters out inconsistent or invalid weight readings and only returns stable values.
- **Error Handling**: Handles serial connection issues and invalid data gracefully.
- **Customizable Settings**: Allows configuration of COM port, baud rate, and timeout.

---

## Requirements

### Hardware
- **MK10 Scale**
- **Prolific USB-to-Serial Driver** (Driver zip file is in the same folder as this script)

### Software
- Python 3.13.1
- Required Python Libraries: `pyserial`

---

## Installation

1. **Install Python 3.13.1**: Download and install Python from [python.org](https://www.python.org/).
2. **Install `pyserial`**: 
   ```bash
   pip install pyserial
   ```
3. **Install Prolific Driver**: Ensure the Prolific USB-to-Serial driver is installed on your system. Download it from the [Prolific website](http://www.prolific.com.tw/) if necessary or use the zip file in the same folder as this script.

---

## Usage

1. **Connect the MK10 scale**:
   - Use a USB-to-serial adapter (with the Prolific driver installed) to connect the scale to your computer.
   - Note the COM port assigned to the device (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux).

2. **Run the Script**:
   - Update the `port` variable if your device uses a different COM port.
   - Run the script:
     ```bash
     python read_weight.py
     ```

3. **Output**:
   - The script will attempt to connect to the scale and read the weight.
   - If successful, it will print the stable weight in kilograms.

---

## Configuration

The script allows you to customize the following parameters:

- **`port`**: The serial port to which the MK10 scale is connected (default: `COM3`).
- **`baudrate`**: The communication speed between the computer and scale (default: `9600`).
- **`timeout`**: Time in seconds to wait for a response (default: `1`).

Example:
```python
python weight.py
```

---

## Troubleshooting

### Common Issues
1. **No Data Received**:
   - Verify that the correct COM port is specified.
   - Check that the MK10 scale is powered on and connected.

2. **Invalid or Skipped Readings**:
   - Ensure the scale is properly calibrated.
   - Verify that the Prolific driver is installed and updated.

3. **Serial Connection Error**:
   - Confirm the serial port is not in use by another application.
   - Restart the script or reconnect the scale.

---

## Example Output

```plaintext
Connected to COM3. Waiting for stable data...
Stable weight detected: 12.34
Final stable weight: 12.34 KG
```

---

## License
This script is open-source and can be modified to suit your specific needs. Please acknowledge the original author when redistributing.

---

## Author
Developed for interfacing with MK10 scales via Prolific drivers. For questions or feedback, contact [armughan.ahmad03@gmail.com].