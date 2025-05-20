# lec13: Software Vulnerabilities 

[toc]

## Malware (Malicious Software)

**Vectors**

- **Vectors are the mechanism through which malware infects a machine**
- Usually the vector will be either a software vulnerability, or a human error
- In the case of human error, this often means someone has clicked “Yes” to something they shouldn’t have!

**Payloads**

- **Payloads are the actual malware deposited on the machine, or the harmful results**
- They range in severity:
    - Essentially do nothing
    - Messages and adverts
    - Recruited into a botnet or mail spam
    - Stealing private information
    - System destruction

### Viruses

- **A virus is a piece of self-replicating code**
- Propagates by attaching itself to a disk, file or document, which would usually be executable
- When the file is run, the virus runs, and attempts to proliferate
- Installs without the user’s knowledge or consent
- Requires human intervention to spread

**Virus Attachment Mechanisms**

- Historically, viruses installed themselves in the boot sectors of disk partitions
- Executable files may be sent as email attachments and require social engineering to entice users
- Script files for system admins including Windows batch files and UNIX shell scripts
- Documents containing macros
    - Older office formats, newer macro enabled workbooks

### Worms

- **Worms are self-replicating and stand-alone programs**
    - **Do not require human intervention**
- Scanning worms or email worms
- Exploit known software vulnerabilities in order to spread

### Trojans

- **A malicious program pretending to be a legitimate application**
- Often obtained in email attachments or on malicious websites
- Don’t replicate themselves user error

### Ransomware 勒索病毒

- **Usually encrypts or blocks access to files and demands a ransom**
- It is a clever attack, because if an anti-virus (AV) system removes it, it is often too late
- Usually distributed on malicious websites, or to already infected machines
- The file decryption keys are protected by encrypting using the public key of a C&C server

**Ransomware Variants**

- Most of the challenge in successfully using ransomware is tricking a user into running it, and bypassing AV and browser protections
    - Fake emails
    -  Malicious web pages
    - Obfuscated Javascript (JS) attachments
    - Deployed using exploit kits

### Rootkits and Backdoors

**Rootkits**

- **Hide the presence** of malicious code by hiding it from the operating system’s **process table**
- Often activated before or during a boot
- Used to hide other malware from standard countermeasures
- Often installs inside the kernel itself, hooking into system call tables, or loads from the master boot record

**Backdoors**

- Once you have access to a system, a backdoor can be used to provide easy access
- These often work in a client-server architecture, awaiting commands from a central server
    - Remote Administration Tool (RAT)
- More discrete methods will involve subtly changing existing software, or the kernel itself
- Reverse shells – connect back for instructions

## Exploits

**Exploits**

- The easiest way of getting access to a machine is having the user to install something for you not always possible!
- Failing this, we need an exploit that defeats the security perimeter put in place by the operating system

### Coding Flaws

### Common Vulnerabilities

### Buffer Overflows



