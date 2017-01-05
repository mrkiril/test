import sys
import datetime
import time
import re
import socket
import base64
import json
import mimetypes
import os.path
import logging
import logging.config
import random
import string
import math
import hashlib
from time import sleep


class HttpClient(object):

    def __init__(self, **kwargs):       
        self.soket_stack = {}        
        self.text = b""
        self.sock = None
        self.tmp = "LALA"
    # def is_ready(self):
    #    pass
    # url https://www.google.com.ua/

    def head(self, url):
        host = re.search("(http://)?(.*)/", url, re.DOTALL)
        if host is None:
            print(host)
            logger.error("ERROR host")

        host = host.group(2)
        logger.info(host)
        addr = (host, 80)
        if ":" in host:
            n_host = host.split(":")
            addr = (n_host[0], int(n_host[1]))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)
        self.sock.setblocking(False)
        # sock.settimeout(2)

        CRLF = b"\r\n"
        q = b"GET" + b" " + url.encode() + b" HTTP/1.1" + CRLF
        q += b"Host: " + host.encode() + CRLF
        q += b"Connection: Keep-Alive" + CRLF
        q += b"User-Agent: Opera/9.80 (iPhone; Opera Mini/7.0.4/28.2555; U; fr) Presto/2.8.119 Version/11.10" + CRLF
        q += CRLF
        # sock.send(q)
        print()
        print(q)
        print()
        data = q
        data_size = len(data)
        total_sent = 0
        while len(data):
            try:
                sent = self.sock.send(q)
                total_sent += sent
                data = data[sent:]
                logger.info('Sending data')

            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e
                logger.info('Blocking with ' +
                            str(len(data)) + ' remaining')
                #print ('Blocking with', len(data), 'remaining')
                # select.select([], [sock], [])  # This blocks until

        assert total_sent == data_size  # True

        logger.info('Great!')
        print("\r\n" * 3)

        class getHttpClient(HttpClient):

            def __init__(self):
                super(getHttpClient, self).__init__()
                #print( self.tmp)
                #print( getHttpClient.tmp )
                self.tmp = url
                #self.sock = HttpClient.sock
        
        children = getHttpClient()
        children.sock = self.sock
        
        return children
        # return type(name, HttpClient.__bases__, dict(HttpClient.__dict__))()

    def isready(self):
        try:
            self.text += self.sock.recv(100)

        except socket.timeout as e:
            err = e.args[0]
            # this next if/else is a bit redundant, but illustrates how the
            # timeout exception is setup
            if err == 'timed out':
                sleep(1)
                logger.info('recv timed out, retry later')
                # continue

            else:
                logger.error(str(e))
                sys.exit(1)

        except BlockingIOError as e:
            # [Errno 11] Resource temporarily unavailable
            # continue
            return False

        else:
            if b"\r\n\r\n" in self.text:
                logger.info("All data is here")
                return True
            else:
                return False


lib = HttpClient()
logging.config.fileConfig(os.path.join(os.getcwd(), "setting", "logging.conf"))
logger = logging.getLogger("try3")


obj1 = lib.head("http://httpbin.org/get?key1=value1")
obj2 = lib.head("http://httpbin.org/get?key2=value2")
obj3 = lib.head("http://httpbin.org/get?key3=value3")
obj4 = lib.head("http://httpbin.org/get?key4=value4")
obj5 = lib.head("http://httpbin.org/get?key5=value5")

print( obj1.sock)
print( obj2.sock)
print( obj1.sock)
print( obj2.sock)

print("obj1: ", obj1.tmp)
print("obj2: ", obj2.tmp)
print("obj1: ", obj1.tmp)
print("obj2: ", obj2.tmp)

start_time = time.time()
while True:
    # if time.time() - start_time = 0.9
    status1 = obj1.isready()
    status2 = obj2.isready()
    status3 = obj3.isready()
    status4 = obj4.isready()
    status5 = obj5.isready()
    
    if status1 == True and status2 == True and status3 == True and status4 == True and status5 == True:        
        break

    else:
        sleep(0.1)
        logging.info("sleep 0.1")
        continue

print(obj1.text)
print("\r\n" * 5)
print(obj2.text)
print("\r\n" * 5)
print(obj3.text)
print("\r\n" * 5)
print(obj4.text)
print("\r\n" * 5)
print(obj5.text)
