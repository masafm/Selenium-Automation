#!/usr/bin/env python3

def crypt(src_text, key):
    if src_text and key:
        xor_code = key
        while len(src_text) > len(xor_code):
            xor_code += key
        return "".join([chr(ord(data) ^ ord(code))
            for (data, code) in zip(src_text, xor_code)]).encode().hex()
        
def decrypt(hex_text, key):
    if hex_text and key:
        try:
            crypt_data = bytes.fromhex(hex_text).decode()
        except ValueError:
            crypt_data = None
            
        if crypt_data:
            xor_code = key
            while len(crypt_data) > len(xor_code):
                xor_code += key
            return "".join([chr(ord(data) ^ ord(code))
                for (data, code) in zip(crypt_data, xor_code)])
