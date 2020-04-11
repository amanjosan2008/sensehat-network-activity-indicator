# Raspberry Pi Sensehat based Network-Activity-Indicator
Use Raspberry Pi SenseHat  to indicvate incoming or outgoing network traffic

On the Raspberry Pi install the Sense Hat and power it up.

Install Packet capture utilities:
```
sudo apt install tshark
pip3 install pyshark
sudo apt-get install libxslt-dev
sudo dpkg-reconfigure wireshark-common
sudo chmod +x /usr/bin/dumpcap
```

Install SenseHat:
```
sudo apt update
sudo apt install sense-hat
```

Run the script:
```
python3 sense_pcap.py
```
