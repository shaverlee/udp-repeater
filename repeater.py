
import socket
import json
import os.path

CONF_FILE = 'config.json'


def get_conf():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, CONF_FILE)) as f:
        return json.load(f)


def main():
    conf = get_conf()
    if not conf:
        return

    port = conf['port']
    sendto = [
        tuple(ip_port)
        for ip_port in conf['sendto']
    ]
    
    sender_socks = dict([
        [tuple(ip_port), socket.socket(type=socket.SOCK_DGRAM)]
        for ip_port in sendto
    ])

    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    while True:
        data = sock.recvfrom(4096)[0]
        for ip_port in sendto:
            sender_socks[ip_port].sendto(
                data,
                socket.SOCK_NONBLOCK,
                ip_port,
            )


if __name__ == '__main__':
    main()
