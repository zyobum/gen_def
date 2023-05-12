import sys
import ndef
import binascii
import re

# Check if URL was passed as argument
if len(sys.argv) < 2:
    print("Please provide a URL as a command line argument.")
    sys.exit(1)

# Get URL from command line argument
url = sys.argv[1]

# Create an NDEF record
record = ndef.UriRecord(url)

# Create an NDEF message and encode it into bytes
ndef_bytes = b''.join(ndef.message_encoder([record]))

# Convert bytes to hex
ndef_hex = binascii.hexlify(ndef_bytes).decode()

# Print hex to screen
print("NDEF Hex Data: ", ndef_hex)

# Remove the protocol part from the URL
sanitized_url = re.sub(r'^https?://', '', url)

# Replace non-alphanumeric characters with underscore and prefix with "ndef_"
filename = "ndef_" + re.sub(r'\W+', '_', sanitized_url) + '.bin'

# Print output filename
print("Output Filename: ", filename)

# Write bytes to binary file
with open(filename, 'wb') as file:
    file.write(ndef_bytes)
    
