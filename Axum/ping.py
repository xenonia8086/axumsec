import socket
import struct
import time

ICMP_ECHO_REQUEST = 8
ICMP_CODE = 0

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

def pingx(idntx, sequence_number):
    icmp_t = ICMP_ECHO_REQUEST
    icmp_c = ICMP_CODE
    icmp_cksum = 0  
    icmp_id = idntx
    icmp_seq_num = sequence_number
    icmp_data = b"abcdefghijklmnopqrstuvwxyz"  

    icmp_ck = icmp_cksum  

   
    icmp_header = struct.pack("bbHHh", icmp_t, icmp_c, icmp_ck, icmp_id, icmp_seq_num)

    icmp_ck = socket.htons(~(icmp_cksum & 0xffff) & 0xffff)
    icmp_header = struct.pack("bbHHh", icmp_t, icmp_c, icmp_ck, icmp_id, icmp_seq_num)

    
    icmp_packet = icmp_header + icmp_data
    return icmp_packet


def pingy(destination, identifier, sequence_number):
    packet = pingx(identifier, sequence_number)
    raw_socket.sendto(packet, (destination, 0))



