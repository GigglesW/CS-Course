iptables -F
iptables -A OUTPUT -o eth0 -p tcp --dport 80 -j DROP
iptables -A OUTPUT -o eth0 -p tcp --dport https -j DROP
