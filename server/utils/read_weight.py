import serial
import time


def read_weight(port="/dev/com3", baudrate=9600, timeout=1):
    try:
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            print(f"Connected to {port}. Waiting for stable data...")

            buffer = ""  # Temporary buffer to store incoming data
            stable_weight = None  # To store the final stable weight

            while True:
                raw_data = ser.read(128)  # Read a chunk of bytes (adjust as needed)
                if raw_data:
                    # Decode the raw bytes and append to the buffer
                    buffer += raw_data.decode("utf-8", errors="replace")

                    # Split the buffer by '=' delimiter
                    parts = buffer.split("=")

                    if len(parts) > 1:
                        # Process the first part (i.e., the weight reading)
                        weight = parts[0].strip()[
                            ::-1
                        ]  # Reverse the string if necessary

                        # Skip invalid readings ("None" or "-")
                        if weight in ["None", "-"]:
                            print(f"Skipping invalid reading: {weight}")
                            buffer = parts[
                                -1
                            ]  # Keep the last incomplete part in the buffer
                            continue

                        # If we get a stable weight, update the stable_weight variable
                        if stable_weight is None or stable_weight == weight:
                            stable_weight = weight
                            print(f"Stable weight detected: {stable_weight}")
                        else:
                            # If there's a discrepancy in weight readings, reset and continue
                            print("Discrepancy found, resetting stable weight...")
                            stable_weight = None

                        # Clear the buffer to continue reading the next part
                        buffer = parts[-1]

                # Wait a bit before reading again to ensure stability
                time.sleep(0.1)

                # If a stable weight is detected, return it
                if stable_weight:
                    print(f"Final stable weight: {stable_weight}")
                    return stable_weight

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
