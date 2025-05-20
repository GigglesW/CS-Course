# lec09: Internet Security

[toc]

## Threat Model

**Browser Server Model**

<img src="./assets/截屏2025-05-13 02.11.50.png" alt="截屏2025-05-13 02.11.50" style="zoom:50%;" />

**Threat Model**

- Different from other threat models:
    - The attacker isn’t in control of the network
    - The attacker hasn’t got access to the target’s OS
- Instead, the attacker
    - Sees messages addressed to themselves or others
    - Sees data obtained from security compromises
    - Can make educated guesses

## Cookies

- HTTP is a stateless protocol
- Most of what we do online is stateful
- **Cookies are small text files used to provide persistence**

> An internet cookie is a **small piece of data that a website stores on your browser to remember your preferences, login status, or activity.**

**Types of Cookie**

- **Session** – Deleted when the browser exits, contain no expiration date
- **Persistent** – Expire at a given time
- **Secure** – Can only be used over HTTPS
- **HTTPOnly** – Inaccessible from JS

### Cookie Vulnerability 

- **Cookie Stealing (Session Hijacking):** Cookie stealing is when an attacker **takes a user's browser cookie to access their account** or personal information without permission.
- **Cross-Site Scripting (XSS):** Cross-site scripting (XSS) is a security flaw where **attackers inject harmful code into a website so that it runs in other users’ browsers**

### Cross-Site Scripting (XSS)

> **Cross-site scripting (XSS)** is a security flaw where **attackers inject harmful code into a website so that it runs in other users’ browsers**

**Preventing XSS**

- Websites must **aggressively escape HTML characters from any user input / output**
- When you consider all of the things people input on interactive websites, this can be a real problem

### Cross-Site Request Forgery (XSRF)

> **Cross-Site Request Forgery (CSRF)** is when a bad website tricks you into doing something on another website where you're already logged in
>
> **Example:** If you’re logged into your online bank, a hacker could make a fake request to transfer money from your account, and the bank would think it’s you doing it because you're already logged in.

**Preventing XSRF**

- **Use synchronizer tokens**
- Each website form has a one-time token that the server validates when the form is submitted

## SSL/TLS

- There are dangers associated with sending plain text cookies, passwords etc.
- SSL, and the newer TLS provide authenticated and encrypted sessions
- **Secure Socket Layer (SSL)** came first, then after v3.0 it became **Transport Layer Security (TLS)**, currently v1.3

### TLS

- Transport Layer Security has two layers:
- **The Record Layer**
    - Using established symmetric keys and other session info, will encrypt application packets, very like IPSec
- **The Handshake Layer**
    - Used to establish session keys, as well as authenticate either party – usually the server using a Public-Key Certificate

**TLS Handshake**

<img src="./assets/截屏2025-05-13 02.17.20.png" alt="截屏2025-05-13 02.17.20" style="zoom:50%;" />

**TLS Vulnerabilities**

- **Weak Cipher Suites**: If a website uses outdated or weak encryption methods, hackers can break the encryption and steal data. For example, using weak algorithms like RC4 can make TLS less secure.
- **Man-in-the-Middle Attacks**: If an attacker can intercept the communication (e.g., on a public Wi-Fi network), they might be able to alter or steal the data being sent, especially if the server's identity isn't properly verified.

**Heartbleed**

- **What is**: a security vulnerability in OpenSSL that allows attackers to access sensitive data from a server's memory
- **How to exploit**: sending a specially **crafted request** to a vulnerable server, allowing attackers to steal data from memory