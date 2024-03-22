import ndef
import sys
import re

def create_http_ndef_record(url):
    # Create an NDEF URI record for the URL
    record = ndef.UriRecord(url)
    
    # Encode the NDEF record into a byte array
    ndef_data = b''.join(ndef.message_encoder([record]))
    
    # Prepend the NDEF message with the NDEF beginning header and append terminator
    full_ndef_message = bytes([0x03, len(ndef_data)]) + ndef_data + bytes([0xFE])
    
    return full_ndef_message

def safe_filename(url):
    # Remove the protocol part and replace unsuitable characters with underscores
    filename = re.sub(r'^https?://', '', url)  # Remove the protocol
    filename = re.sub(r'[^a-zA-Z0-9.-]', '_', filename)  # Replace unsuitable chars
    return filename[:255]  # Limit to 255 characters to ensure compatibility

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    if not (url.startswith('http://') or url.startswith('https://')):
        print("Error: URL should start with 'http://' or 'https://'")
        sys.exit(1)

    ndef_raw_data = create_http_ndef_record(url)

    # The raw NDEF data is ready to be written to an NFC tag
    print("NDEF raw data:", ndef_raw_data.hex())

    # Generate a safe filename from the URL
    filename = "ndef_" + safe_filename(url) + ".bin"
    with open(filename, 'wb') as file:
        file.write(ndef_raw_data)

    print(f"NDEF raw data written to: {filename}")

