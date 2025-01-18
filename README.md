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
- Python 3.11.11
- Required Python Libraries: `pyserial`

### Repo Structure
📂weight-reading <br/>
 ┣ 🖥️ server <br/>
 ┃ ┣ 🐍app.py                                   # FastAPI server script <br/>
 ┃ ┣ 📂utils <br/>
 ┃ ┃ ┣ 🐍__init__.py <br/>
 ┃ ┃ ┗ 🐍read_weight.py                         # Script to read weight data from MK10 scale <br/>
 ┣ 🐍__init__.py                                # __init__.py <br/>
 ┃ 📜README.md                                  # Documentation for the project <br/>
 ┣ 📜requirements.txt                           # List of dependencies <br/>
 ┣ 🐍weight.py                                  # Python script to read weight data from MK10 scale <br/>
 ┣ 📦PL2303_USB_Driver_Installer_v1.0.0.0.exe   # Prolific USB-to-Serial Driver Installer <br/>
 ┗ 🐙.gitignore                                 # Git ignore file

---

## Installation

1. **Install Python 3.11.11**: Download and install Python from [python.org](https://www.python.org/).
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

Here's the implementation of a simple FastAPI server that calls the `read_weight` function and returns the weight in a JSON response. The updated README file is also included below.

---

### FastAPI Server (`server/app.py`)

```python
from fastapi import FastAPI
from pydantic import BaseModel
from read_weight import read_weight

app = FastAPI()

class WeightResponse(BaseModel):
    weight: float
    unit: str = "KG"

@app.get("/weight", response_model=WeightResponse)
async def get_weight(port: str = "COM3", baudrate: int = 9600, timeout: int = 1):
    """
    Reads the weight from the MK10 scale and returns it as a JSON response.

    Query Parameters:
    - port: Serial port (default: COM3)
    - baudrate: Communication speed (default: 9600)
    - timeout: Serial read timeout (default: 1 second)
    """
    try:
        weight = read_weight(port=port, baudrate=baudrate, timeout=timeout)
        if weight:
            return {"weight": float(weight), "unit": "KG"}
        return {"weight": 0.0, "unit": "KG"}
    except Exception as e:
        return {"error": str(e)}
```

---

### Updated README

# Weight Reading Script with FastAPI for MK10 with Prolific Driver

This project reads stable weight data from an MK10 scale connected via a serial port using the Prolific driver. It includes:
- A Python script to process raw data from the MK10 scale.
- A FastAPI server to provide an API endpoint that returns the stable weight as a JSON response.

---

## Features
- **Serial Communication**: Connects to the MK10 scale via a specified COM port.
- **Stable Weight Detection**: Filters inconsistent readings and returns only stable values.
- **FastAPI Integration**: Exposes the weight-reading functionality via a REST API endpoint.

---

## Requirements

### Hardware
- **MK10 Scale**
- **Prolific USB-to-Serial Driver**

### Software
- Python 3.x
- Required Python Libraries:
  - `pyserial`
  - `fastapi`
  - `pydantic`
  - `uvicorn`

---

## Installation

1. **Install Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Install Required Libraries**:
   ```bash
   pip install pyserial fastapi pydantic uvicorn
   ```
3. **Install Prolific Driver**: Download and install the driver from the [Prolific website](http://www.prolific.com.tw/).

---

## Usage

### 1. Run the API Server
- Save the FastAPI server code to a file, e.g., `app.py`.
- Start the server:
  ```bash
  uvicorn app:app --reload --host 0.0.0.0 --port 8000
  ```

### 2. Access the Endpoint
The API exposes the `/weight` endpoint, which reads the weight from the MK10 scale and returns the result in JSON format.

- **Endpoint**: `GET /weight`
- **Query Parameters**:
  - `port` (default: `COM3`): Serial port to connect to.
  - `baudrate` (default: `9600`): Communication speed.
  - `timeout` (default: `1`): Serial read timeout in seconds.

#### Example Request
```bash
curl "http://127.0.0.1:8000/read_weight?port=COM3&baudrate=9600&timeout=1"
```

#### Example Response
```json
{
  "weight": 12.34,
  "unit": "KG"
}
```

### 3. Debugging and Testing
If you're not connected to a real scale, you can modify the `read_weight` function to simulate data for testing purposes.

---

## Troubleshooting

### Common Issues
1. **No Data Received**:
   - Verify the correct COM port is specified.
   - Ensure the MK10 scale is powered on and properly connected.

2. **Serial Connection Error**:
   - Ensure the Prolific driver is installed and updated.
   - Confirm the serial port is not in use by another application.

3. **API Connection Issues**:
   - Ensure the FastAPI server is running.
   - Check the port and host configuration in the `uvicorn` command.

---

## Example Output

#### API Response
```json
{
  "weight": 15.75,
  "unit": "KG"
}
```
### Deployment via Docker

```bash
docker compose up
```
---

## License
This script is open-source and can be modified to suit your specific needs. Please acknowledge the original author when redistributing.

---

## Author
Developed for interfacing with MK10 scales via Prolific drivers. For questions or feedback, contact [armughan.ahmad03@gmail.com].
