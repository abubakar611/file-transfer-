# File Transfer with Sockets

This project demonstrates how to transfer files between a client and server using sockets. It includes both a sender script and a receiver script for simple file transmission.

## Features

- **File Transfer:** Allows a file to be sent from a client to a server over a network socket.
- **Basic Protocol:** Sends file metadata (name and size) followed by the file data.

## Components

### `sender.py`

This script handles the following tasks:
1. **Send File Data:** Opens the file to be sent, reads its data, and sends it to the receiver.
2. **Send Metadata:** Sends the file name and size before the actual file data.

#### Example Usage
```bash
python sender.py
```

### `receiver.py`

This script performs the following:
1. **Receive File Data:** Listens for incoming connections from the sender and receives the file data.
2. **Save File:** Writes the received file data to a local file.

#### Example Usage
```bash
python receiver.py
```

## Prerequisites

- Python 3.x

## Setup

1. **Prepare the Files:**
   - Place the file to be transferred (e.g., `resume.docx`) in the same directory as `sender.py`.

2. **Run the Scripts:**
   - Start the receiver script to listen for incoming connections.
   - Run the sender script to send the file.

## Troubleshooting

- **File Not Found Errors:** Ensure that the file to be sent exists and is located in the correct directory.
- **Connection Errors:** Verify that the server is running and listening on the correct port before running the sender script.


## Contact
For any questions or further information, please contact me at abubaabubakarjunaid611@gmail.com. Connect with me on LinkedIn.
