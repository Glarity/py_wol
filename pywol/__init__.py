import socket
import struct


def send_wol(macaddress, ip_address="255.255.255.255", port=9):
    macaddress_split = macaddress.replace("-", "").replace(".", "").replace(":", "")
    message = b"FFFFFFFFFFFF" + (macaddress_split * 16).encode()
    data = b""
    for i in range(0, len(message), 2):
        data += struct.pack(b'B', int(message[i: i + 2], 16))
    curr_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    curr_socket.sendto(data, (ip_address, port))
    print("Sent WOL magic-packet for MAC {0} to {1}:{2}".format(macaddress, ip_address, port))
