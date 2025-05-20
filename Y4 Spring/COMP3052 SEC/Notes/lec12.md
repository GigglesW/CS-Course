# lec12: Intrusion Detection

[toc]

## Network Attack Models

<img src="./assets/截屏2025-05-13 02.31.32.png" alt="截屏2025-05-13 02.31.32" style="zoom:50%;" />

**Intruders**

- **伪装者**（Masquerader）：外部未经授权的攻击者，通过合法用户账户获得访问权限。
- **误用者**（Misfeasor）：合法用户滥用自己的权限。
- **隐秘者**（Clandestine）：攻击者获取了控制权，避开了审计

## Intrusion Detection System (IDS)

**Misuse vs. Anomaly**

-  **Misuse detection**
    - **Based on signatures**
    - Can miss novel or variant attacks
    - Unsuitable for **zero-day attack detection**
- **Anomaly detection**
    - **Detects deviations from normal behaviour**
    - Can generate too many false alerts
    - What is deﬁned as ‘normal’ can change over time

> A **zero-day vulnerability** is a hidden flaw in software that the developer doesn't know about yet, so there’s no fix for it.
> A **zero-day attack** happens when hackers find and use this flaw to break into systems before anyone has a chance to fix it.

**Current IDS Issues**

- **Misuse detection is pretty straightforward**
    - need to increase the speed of updating the signature database
- **Anomaly detection is by no means solved**
    - still massive research effort worldwide
    - look for novel solutions outside of statistical machine learning
    - cope with changing user and network behaviour

**Intrusion Detection/Prevention**

- **Intrusion Detection Systems (IDS)**
    - Detects possible intrusion attempts
    - Generates alerts and logs for administrators
- **Intrusion Prevention Systems (IPS)**
    - Identical to IDS except also **stops the attack**
    - 检测+阻止

## IDS Deployment

- **Network-based:**
    - Monitors network traffic and analyses a variety of packets from different protocols to identify suspicious activity
- **Host-based:**
    - Monitors the characteristics of a single host to find suspicious activity including resource / app usage
    - In many ways modern Anti-Virus does this

### Network-based IDS 

- Placed at a **viewpoint on a network** to examine and analyse traffic
    - Installed on a firewall or in a DMZ
    - Installed behind a screened subnet
- May perform deeper analysis than many firewalls, e.g. stateful protocol analysis and deep packet inspection
- **Pros**
    - **Centralized Monitoring**
    - **Powerful Correlation Techniques**
    - **Better at Detecting DDoS Attacks**
    
- **Cons**
    - **Difficulty in Detecting Fragmented Packet-Based Attacks**
    - **Harder to Detect Phishing or Trojan Attacks**
    - **Limited Deep Packet Inspection**
    

### Host-based IDS

- Additional layer of security software running on a host within a protected LAN or VPN
- Creates **a profile of usage** for specific users
- **Pros**
    - **Deep Monitoring**
    - **Packet Inspection**
- **Cons**
    - **Single Host Limitation**
    - **Resource Intensive:** 


### Components of IDS

- **Sensors / Agents**: collect and collate data from multiple viewpoints on a network
- **Analysers**: ascertain if an intrusion has taken place
- **Reporting**: notify the administrators via alerts, usually a console or graphical interface is required

## Detection Modes

- **Stateful Protocol Analysis**
    - More complex version of a **stateful packet filter**
- **Signature-based Detection**
    - Fingerprinting sequences of operations or packets
- **Anomaly-based Detection**
    - Build a model of “normal” and find deviations

### Protocol Analysis

- Hold detailed session information on protocols being used, examine for attacks:
    - Why is this user logging in as root?
    - Why is this command being sent a 1000 byte buffer as a parameter?
- Computationally costly, and requires the IDS to have all possible versions of these protocols described in its database

### Signature-based Detection

- **Signature-based Detection:**
    - **Store some small code signature for each virus**
    - Scan files either in bulk or at runtime, compare with the signatures on file
    - Generic signatures
- **If operations match a defined signature, then an alarm is triggered**
- Include some form of attack language
    - Mechanisms to describe sequences of events
    - Maintain and monitor intermediate states and event transitions
- **Pros**
    - Computationally efficient
    - Will always spot a known attack or vulnerability
- **Cons**
    - Will always miss an unknown attack or vulnerability
    - Detailed signature databases must be kept up-to-date

**SNORT**

- Snort is a powerful and well established IDS
- Uses rules to analyse **network packets**, and then can provide alerts or logging

### Anomaly-based Detection

- **Heuristics**
    - Determine what actions and rules a virus program will normally adopt
    - Start the program in a VM and see what it does
- Anomaly detection has wide-ranging applications from IDS to banking fraud
- Build up a picture of normal usage, and detect when usage moves beyond what is normal
    - This may involve usage of network, applications, storage, system calls etc.
- Always a trade off between false positives and false negatives

**What is Normal?**

- Run a host within a quarantined environment and collect training data
- Constructed by monitoring audit logs
- Sometimes rely on analysis of sequences of system calls through normal behaviour