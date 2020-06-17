
import socket
import sys


def my_hex(bytes):
    return ' '.join(['%02X' % ord(b) for b in bytes])


def main(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    while True:
        data, ip = sock.recvfrom(4096)
        print('%d <<< %s' % (len(data), str(ip)))
        print(my_hex(data))


if __name__ == '__main__':
    port = int(sys.argv[1])
    main(port)
