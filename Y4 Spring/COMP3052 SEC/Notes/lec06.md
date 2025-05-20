# lec06: Firewalls

[toc]

## Firewalls

**Firewalls**

- **A hardware and/or software system**
- **Prevents unauthorised access of packets from one network to another**
- All data leaving any subnet must pass through it

**Firewall Functions**

- Implements ‘**single point**’ security measures
- Security event monitoring through packet analysis and **logging**
- Network-based access control through implementation of a rule set

**Location**

- Many different possible locations – thus many different network architectures
- **Network Firewalls**: Placed between a **subnet and the internet**
- **Host-based Firewalls**: Placed on **individual machines**
- All traffic must go through the firewall for it to function correctly
- A standard home router is a good example of a network firewall

<img src="./assets/截屏2025-03-30 16.28.15.png" alt="截屏2025-03-30 16.28.15" style="zoom:50%;" />

**DMZ**

- A **demilitarized zone** is a small subnet that separates **externally facing services** from the **internal network**

<img src="./assets/截屏2025-03-30 16.28.43.png" alt="截屏2025-03-30 16.28.43" style="zoom:50%;" />

**Firewall Basic Function**

- Defends a protected network against parties accessing services that should only be available internally
- Can also restrict access from inside to outside services

**Firewalls are not enough**

- Cannot protect against **attacks that bypass the firewall**
    - E.g. Tunnelling
- Cannot protect against **internal threats or insiders**
    - Might help a bit by egress filtering
- Cannot protect against the transfer of virusinfected programs or files

**Firewall Types**

- Packet Filters
- Stateful Inspection
- Proxies
- Dynamic
- Kernel

## Packet Filters

- **Specify which packets are allowed or dropped**
- Rules based on:
    - **Source / Destination IP**
    - **TCP / UDP port numbers**
- Possible for both inbound and outbound traffic
- Can be implemented in a router by only examining packet headers
    - Operates on OSI layer 3 (IP) or layer 4 (TCP)

**Packet Filter Rules**

- Rule execution depends on implementation
    - **IPTABLES**: **First rule** to match is applied
    - **PF**: All rules are examined, **the last match** is applied
- Rules are organised in chains, which are logical subgroups of rules
- Depending on the packet, different chains are activated

### IPTABLES

- An application that provides access to the Linux firewall rule tables
    - Not actually a firewall, but configures the firewall
    - The firewall is mostly implemented as netfilter modules
- IPTABLES uses tables to store chains
    - Default is the filtering table
- Chains are ordered lists of rules
    - Rules match, or they don’t
- Matches result in a jump, else we check the next rule

- There can be multiple chains per table
    - E.g. a TCP handling chain
- Jumps can go to ACCEPT, DROP, LOG or another chain
- Complex behaviour can be built up

<img src="./assets/截屏2025-03-30 16.35.04.png" alt="截屏2025-03-30 16.35.04" style="zoom:50%;" />

- There are built-in tables in IPTABLES:
    - Filter (default)
    - NAT
    - Mangle – Packet alteration
    - Raw – Skips connection tracking
    - Security – mandatory access control
- The default table is the filtering table, including **Input, Output and Forward chains**

<img src="./assets/截屏2025-03-30 16.36.11.png" alt="截屏2025-03-30 16.36.11" style="zoom:50%;" />

<img src="./assets/截屏2025-03-30 16.36.35.png" alt="截屏2025-03-30 16.36.35" style="zoom:50%;" />

### Policies

- **Permissive (Black listing)**: allow everything except dangerous services
    - Easy to make a mistake or forget something
- **Restrictive (White listing)** : block everything except designated useful services
    - More secure by default
    - Fairly easy to DoS yourself!

**IPTABLES Policies**

- To use a **blacklisting policy**, we want to accept by default, then have rules that drop:

<img src="./assets/截屏2025-03-30 16.37.57.png" alt="截屏2025-03-30 16.37.57" style="zoom:50%;" />

- For a **whitelisting policy**, we want to drop by default, then let certain packets through:

<img src="./assets/截屏2025-03-30 16.38.19.png" alt="截屏2025-03-30 16.38.19" style="zoom:50%;" />

## Stateful Packet Filters

**Packet Filter Issues**

- Packet filters are simple, low level and have high assurance
- But, they cannot:
    - Prevent attacks that exploit application-specific vulnerabilities
    - Do not support higher-level authentication schemes

**Stateful Packet Filters**

- **A stateful firewall always keeps track of the state of network connections.**
- **Once a particular kind of traffic has been approved by a stateful firewall, it is added to a state table/connection table.**
- Understand requests and replies 
    - E.g. 3-way Handshake: SYN, SYN/ACK, ACK

**Connection Table Example**

<img src="./assets/截屏2025-03-30 16.39.28.png" alt="截屏2025-03-30 16.39.28" style="zoom:50%;" />

- **ACK** packets are used to keep track of the session
    - the connection is ongoing
- Packets without the ACK are the connection establishment messages

## Proxy Servers

- Proxy servers initiate a connection on our behalf
- They can block certain access, and scan for malicious files or web pages

<img src="./assets/截屏2025-03-30 16.41.05.png" alt="截屏2025-03-30 16.41.05" style="zoom:50%;" />

- Issues
    - Large overhead per connection
    - More expensive than packet filtering
    - Configuration is complex
    - A separate server is required for each servic

## Network Address Translation (NAT)

- The shortage of IP addresses mean that most routers now perform NAT automatically

<img src="./assets/截屏2025-03-30 16.42.01.png" alt="截屏2025-03-30 16.42.01" style="zoom:50%;" />

- The implicit advantage in NAT is that your machine is almost totally hidden from the internet
- Only established connections are forwarded to your internal machine
    - Or, specific port forwarding rules

