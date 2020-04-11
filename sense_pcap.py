#!/usr/bin/python3
from sense_hat import SenseHat
from time import sleep
import pyshark

sense = SenseHat()

capture = pyshark.LiveCapture(interface='wlan0', only_summaries=True, bpf_filter='ip and tcp port not 22')

src_ip = '192.168.1.35'

#print('Ready..')


def inward():
    #print("In")
    sense.set_pixel(1,2,0,200,0)
    sense.set_pixel(0,3,0,200,0)
    sense.set_pixel(0,4,0,200,0)
    sense.set_pixel(1,3,0,200,0)
    sense.set_pixel(1,4,0,200,0)
    sense.set_pixel(2,3,0,200,0)
    sense.set_pixel(2,4,0,200,0)
    sleep(0.01)
    sense.clear()

def outward():
    #print("out")
    sense.set_pixel(6,5,200,0,0)
    sense.set_pixel(5,3,200,0,0)
    sense.set_pixel(5,4,200,0,0)
    sense.set_pixel(6,3,200,0,0)
    sense.set_pixel(6,4,200,0,0)
    sense.set_pixel(7,3,200,0,0)
    sense.set_pixel(7,4,200,0,0)
    sleep(0.01)
    sense.clear()

def pcap():
    for packet in capture.sniff_continuously():
        #print(packet.source, packet.destination, packet.protocol)
        if src_ip in packet.source:
          outward()
        else:
          inward()

if __name__ == '__main__':
    pcap()
