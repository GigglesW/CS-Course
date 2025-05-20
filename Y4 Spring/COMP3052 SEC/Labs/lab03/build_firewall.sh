# Clear all current rules 
iptables -F

# Input chain 
# Rules to accept packets if they meet criteria 
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 
iptables -A INPUT -i eth0 -p tcp --dport ssh -j ACCEPT 
iptables -A INPUT -i eth0 -p tcp --dport 80 -j ACCEPT 
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT 
iptables -I INPUT -i lo -j ACCEPT

# Drop all remaining packets 
iptables -A INPUT -j DROP

# Output chain 
# Rules to accept packets if they meet criteria 
iptables -A OUTPUT -o eth0 -p tcp --sport ssh -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp --sport 80 -j ACCEPT 
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT 
iptables -I OUTPUT -o lo -j ACCEPT

# Drop all remaining packets 
iptables -A OUTPUT -j DROP
