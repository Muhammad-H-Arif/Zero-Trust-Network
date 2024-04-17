
#!/bin/bash

iptables -F
iptables -X

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

iptables -A INPUT -s 192.168.1.0/24 -d 192.168.2.0/24 -j ACCEPT
iptables -A INPUT -s 192.168.2.0/24 -d 192.168.1.0/24 -j ACCEPT

iptables -A INPUT -p tcp -s 10.0.0.1 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

iptables -A INPUT -j LOG --log-prefix "Dropped packet: "
iptables -A INPUT -j DROP

iptables-save > /etc/iptables/rules.v4
