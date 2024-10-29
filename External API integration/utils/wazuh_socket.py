from socket import AF_UNIX, SOCK_DGRAM, socket
import json

SOCKET_ADDR="/var/ossec/queue/sockets/queue"

def send_msg(msg: dict, agent: dict) -> None:
    if agent:
        location = f"[{agent['id']}] ({agent['name']}) {agent['ip'] if 'ip' in agent else 'any'}"
        location = location.replace('|', '||').replace(':', '|:')
        string = f"1:{location}->virustotal:{json.dumps(msg)}"
    else:
        string = f'1:virustotal:{json.dumps(msg)}'
    try:
        sock = socket(AF_UNIX, SOCK_DGRAM)
        sock.connect(SOCKET_ADDR)
        sock.send(string.encode())
        sock.close()
    except Exception as e:
        logger.error(f"send_msg: {e}")
        sys.exit(1)
