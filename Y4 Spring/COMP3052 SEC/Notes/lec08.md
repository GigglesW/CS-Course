# lec08: Network Security

[toc]

## Two Threat Models

- **Passive attackers**
    - Eavesdropping / wiretapping / sniffing
    - **Traffic analysis**
    - 不直接干扰通信内容，而是通过**监听**网络流量来获取信息
- **Active attackers**
    - Spoofing attacks (**phishing**, email)
    - Squatting attacks

**Each protocol carries the protocol in the layer above by appending headers to it**

<img src="./assets/截屏2025-03-13 13.08.42.png" alt="截屏2025-03-13 13.08.42" style="zoom:50%;" />

## IPSec

**IP Security**

- IP is connectionless and stateless
    - Best effort service
    - No delivery guarantee **(provided by TCP)**
    - No order guarantee **(provided by TCP)**
- IPv4 No guaranteed security support
- IPv6 security support is guaranteed - IPSec

**IPSec**

- Optional in IPv4, **mandatory support** in IPv6
- Two major security mechanisms
    - **IP Authentication Header (AH)**
    - **IP Encapsulating Security Payload (ESP)**
- Does not contain any mechanisms to **prevent traffic analysis**

**Encapsulating Security Payload (ESP)**

- Includes an additional header within the IP packet that **describes what encryption and authentication** is in use

<img src="./assets/截屏2025-03-13 13.39.38.png" alt="截屏2025-03-13 13.39.38" style="zoom:50%;" />

- **Transport Mode**

    - **Transport mode** simply encrypts packets, providing **host-to-host encryption** but using the original header

    - Prevents contents being read, but doesn’t stop traffic analysis or manipulation of the header

- **Tunnel Mode**

    - **Tunnel mode** (usually gateway-to-gateway) protects some segment of a channel with encryption

    - **Provides some resistance to traffic analysis**, and completely protects manipulation of the payload

    - **VPNs are commonly implemented this way**


> **Transport Mode（传输模式）**
>
> - 在**传输模式**下，**仅加密数据包的有效载荷**（即数据部分），而**保持原始的IP头部不变**。
> - **主要特点**：
>     - **主机到主机的加密**：数据的加密仅保护实际传输的数据部分，不对整个数据包进行加密。
>     - **防止内容被读取**：通过加密有效载荷，**防止数据内容被窃取**。
>     - **不能阻止流量分析**：由于IP头部没有加密，攻击者可以看到通信的元数据（如源IP、目的IP和数据包大小等），从而进行**流量分析**。
>     - **不能阻止头部篡改**：IP头部未加密，攻击者仍有可能对数据包头部进行**篡改**。
>
> **Tunnel Mode（隧道模式）**
>
> - 在**隧道模式**下，**整个IP数据包**（包括头部和有效载荷）都被加密，并封装在新的IP包中，通常用于**网关到网关的通信**。
> - **主要特点**：
>     - **提供更高的安全性**：不仅加密了有效载荷，还加密了IP头部，因此能够有效防止**流量分析**和**头部篡改**。
>     - **适合VPN使用**：由于隧道模式对整个数据包进行加密，它常用于**虚拟专用网络（VPN）**中，以确保两端之间的通信安全。

**ESP in Transport Mode**

<img src="./assets/截屏2025-03-13 13.47.18.png" alt="截屏2025-03-13 13.47.18" style="zoom:50%;" />

**ESP in Tunnel Mode**

<img src="./assets/截屏2025-03-13 13.47.31.png" alt="截屏2025-03-13 13.47.31" style="zoom:50%;" />

## ARP Cache Poisoning

**Address Resolution Protocol (ARP)**

- ARP is a protocol used (in IPv4) to **obtain physical MAC addresses for given IPs**
    - **ARP**是用于在**IPv4**网络中将**IP地址**映射到**物理MAC地址**的协议
    - It is used prior to constructing IP and TCP packets for communication
    - **Network layer**
    

<img src="./assets/截屏2025-03-13 13.56.51.png" alt="截屏2025-03-13 13.56.51" style="zoom:50%;" />

**ARP Spoofing**

- We can simply send an **unrequested ARP reply**, and **overwrite the MAC address in a host’s ARP cache** with our own

<img src="./assets/截屏2025-03-13 13.57.30.png" alt="截屏2025-03-13 13.57.30" style="zoom:50%;" />

**ARP Protection**

- Some OSs **ignore unsolicited ARP requests**, or can be configured to use ARP differently
- Some software, such as intrusion detection packages, will include **ARP spoofing detection**
    - Maintain a log of current MAC:IP assignments and ARP requests / replies
    - Allows us to spot suspicious messages such as unsolicited ARP replies

## DNS Spoofing

**Domain Name System (DNS)**

- DNS translates **domain names into IP addresses**
    - **DNS**用于将**域名**转换为**IP地址**
    - E.g. `nottingham.ac.uk -> 128.243.80.167`
- **DNS packets are UDP**: Stateless, on the **transport layer**
- DNS resolvers will cache the IPs for a while

<img src="./assets/截屏2025-03-13 14.05.52.png" alt="截屏2025-03-13 14.05.52" style="zoom:50%;" />

**DNS Spoofing**

- If we can poison the cache of a nameserver people are using, we can replace a website lookup with our IP
    - Can be achieved through prior **ARP cache poisoning, a reply flood or a Kaminsky attack**

<img src="./assets/截屏2025-03-13 14.07.30.png" alt="截屏2025-03-13 14.07.30" style="zoom:50%;" />

**DNS Protection**

- **Random query numbers** help protect against spoof replies
- **Randomise the source port**: Since the Kaminsky attack, most resolvers now **randomise the source port** too
- DNSSEC aims to tackle DNS exploits by authenticating the name server and providing integrity for the messages

## Denial of Service Attacks

- **DOS Attacks**

    - A denial of service attack is an attempt to **make a machine or network resource unavailable to its authorised / intended users**
- This will usually involve **flooding a machine with enough requests** that it can’t serve its legitimate purpose
- **DDOS Attacks**

    - A **distributed denial of service** occurs where there is **more than one attacking machine**

> **Simple Attack Example: TCP Syn Flooding**
>
> - **攻击者发起一个真实的连接请求**（即发送SYN请求），但随后**立即断开连接**。
> - **攻击者不会完成三次握手**，导致目标主机等待连接的完成。
> - **受害者不断处理这些未完成的连接**（称为半打开连接），而攻击者持续发起大量的SYN请求。
> - 最终，**受害者的半连接数达到上限**，无法再处理正常的连接请求，从而导致**拒绝服务**。

**Distributed Denial of Service (DDoS) Attack Example**

<img src="./assets/截屏2025-03-30 16.58.12.png" alt="截屏2025-03-30 16.58.12" style="zoom:50%;" />

## Amplification Attacks

**Amplification Attacks**

- **Regular attacks** are attacker’s bandwidth vs attacker’s target’s
    - 意味着攻击者需要足够的带宽来发送大量流量

- **Amplification attacks utilise some aspect of a network protocol to increase the bandwidth of an attack**
    - **放大攻击**则通过利用网络协议的某些特性，使攻击流量**成倍增加**，从而以较少的带宽发起更大规模的攻击。这种方式能够**增加攻击的效果**，以更少的资源对目标系统造成更大压力。


<img src="./assets/截屏2025-03-30 16.58.40.png" alt="截屏2025-03-30 16.58.40" style="zoom:50%;" />

**DNS Amplification**

- Recursive resolvers respond to DNS queries then return a response
- This response can be many times larger than the query
- 在**DNS放大攻击**中，攻击者通过向DNS服务器发送一个非常小的查询请求，服务器会返回**比查询请求大得多的响应**。攻击者利用这个特性，通过发送小请求来获得更大的响应，从而放大攻击流量并将其定向到目标系统。

**Smurf and Fraggle Attacks**

- **Smurf attacks** broadcast an ICMP Ping request to a router, but with a spoofed IP belonging to the victim
- A **Fraggle attack** is identical in principle, using UDP echo packets

<img src="./assets/截屏2025-03-30 16.59.13.png" alt="截屏2025-03-30 16.59.13" style="zoom:50%;" />
