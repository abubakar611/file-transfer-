# File Transfer System

This project demonstrates a simple file transfer system using sockets in Python. It consists of a sender and a receiver that transfer files over a network connection.

## Features

- **Send Files**: Send a file from the sender to the receiver.
- **Receive Files**: Receive and save the file on the receiver's end.

## Files

1. **sender.py**: The sender script that encrypts and sends a file.
2. **receiver.py**: The receiver script that receives and saves the file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. No additional packages are needed for this basic implementation.

## Usage

### Sender

1. Edit `sender.py` to specify the file you want to send and the destination IP and port.
2. Run the sender script:
   ```bash
   python sender.py
   ```

### Receiver

1. Edit `receiver.py` to specify the save path for the received file and the IP and port to listen on.
2. Run the receiver script:
   ```bash
   python receiver.py
   ```

## Example

1. Start the receiver script.
2. Start the sender script to send a file.
