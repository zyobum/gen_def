# NDEF URL Encoder

This Python script takes a URL as a command line argument, generates an NDEF (NFC Data Exchange Format) message containing a URI record for that URL, and writes the raw NDEF data to a binary file. The name of the output file is derived from the URL, with the protocol part removed, non-alphanumeric characters replaced with underscores, and prefixed with "ndef_".

## Dependencies

This script uses the `ndeflib` library. You can install it with pip:

```bash
pip install ndeflib
```

## Usage

You can run the script from the command line with the URL as an argument:

```bash
python gen_ndef.py https://linktr.ee/0xjz
```

The script will print the NDEF data in hexadecimal format to the console and write the raw NDEF data to a binary file. The name of the output file will also be printed to the console.

## Example

Command:

```bash
python gen_ndef.py https://linktr.ee/0xjz
```

Output:

```
NDEF Hex Data:  9101081d55036c696e6b74722e65652f30786a7afe
Output Filename: ndef_linktr.ee_0xjz.bin
```

In this example, the script writes the raw NDEF data to a binary file named `ndef_linktr.ee_0xjz.bin`.
