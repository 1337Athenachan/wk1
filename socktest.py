#!/bin/bash

#Sockets 

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET is ipv4, sockstream is a port
s.connect((HOST,PORT))

