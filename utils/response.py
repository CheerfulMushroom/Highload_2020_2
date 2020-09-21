import asyncio
import mimetypes
from datetime import datetime
from os.path import getsize
from socket import socket
from config import Config

STATUS_MESSAGES = {
    200: 'OK',
    400: 'Bad Request',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
}


class Response:
    def __init__(self, method='GET', protocol='HTTP/1.1', status=200, filepath=None):
        self._method = method
        self._protocol = protocol
        self._status = status

        self._headers = {
            'Server': 'lebedevaa',
            'Date': datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            'Connection': 'close'
        }

        self._filepath = filepath
        if filepath is None:
            return

        try:
            file_size = getsize(self._filepath)
            mime_type, _ = mimetypes.guess_type(self._filepath)
            self._headers.update({'Content-Length': file_size})
            self._headers.update({'Content-Type': mime_type})
        except OSError:
            pass

    @property
    def status(self):
        return self._status

    async def send(self, client_socket: socket):
        loop = asyncio.get_event_loop()

        raw_utf = f'{self._protocol} {self._status} {STATUS_MESSAGES[self._status]}\r\n' + \
                  '\r\n'.join([f'{key}: {value}' for key, value in self._headers.items()]) + '\r\n\r\n'
        raw_bytes = raw_utf.encode()

        await loop.sock_sendall(client_socket, raw_bytes)

        if self._filepath is not None and self._method == 'GET':
            with open(self._filepath, 'rb') as file:
                part = file.read(Config.bytes_per_send)
                while len(part) > 0:
                    await loop.sock_sendall(client_socket, part)
                    part = file.read(Config.bytes_per_send)
