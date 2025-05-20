# lec03: Foundations of Security

[toc]

## Key Concepts

**Key Concepts**

- Computer Security 
    - Confidentiality 
    - Integrity 
    - Availability 
- Accountability 
- Nonrepudiation

### Computer Security

- **Traditionally defined by three areas: CIA**
- **Confidentiality**: prevention of unauthorised **disclosure** of information
- **Integrity**: prevention of unauthorised **modification** of information
- **Availability**: prevention of unauthorised **withholding** of information

### Confidentiality

- **Privacy** – protection of personal data
- **Secrecy** – protection of data of an organisation
- Examples:
    - Hide document’s content 
    - Hide document’s existence (Unlinkability and Anonymity)

### Integrity

- **Informally**: Making sure everything is as it is supposed to be.
- **Formally**: Integrity deals with the prevention of unauthorised writing.
- Examples: Distributed bank transactions, Database records
- **Authenticity**

    - `Authenticity = Integrity + Freshness`

    - Freshness may seem trivial, but it’s pretty important in bank transactions!

### Availability

- **Availability**
    - “The property of being **accessible and useable** upon demand by an authorised entity.”
- We want to prevent **denial of service (DoS)**

### Accountability

- Users should be held responsible for their actions
- System should identify and authenticate users
    - Audit trail should be kept

### Non-Repudiation

- Non-repudiation provides un-forgeable evidence
    - Evidence verifiable by a third party
    - E.g., notaries, digital certificates, …
- Nonrepudiation of:
    - **origin – sender identification** 
    - **delivery – delivery confirmation**
- Relate to physical security (keycards,…)

### Reliability

- **Reliability** - against (accidental) failures 
- **Safety** - impact of system failures on their environment
- Security is an aspect of reliability, and vice versa!

## Data vs. Infomation

- Security is about **controlling access to information** and resources
    - This can be difficult, thus controlling access to data is more viable 
    - **Data** – Means to represent information 
    - **Information** – (subjective) interpretation of data

**Problems of Inference**

- Focusing on data can still leave information vulnerable 
- Consider a medical database
    - Medical records cannot be queried 
    - Aggregates like prescription totals can be
- Carefully chosen queries can narrow down who has what conditions
    - A covert channel

## Principles of Computer Security Design

- **Fundamental Design Principles:**
    - Focus of Control 
    - Complexity vs. Assurance 
    - Centralised or Decentralised Controls 
    - Layered Security
- **Focus of Control**
    - 1st Design Decision:
    - In a given application, should the protection mechanisms in a computer system focus on: Data Operations Or users?
- **Complexity vs. Assurance** 
    - 2nd Design Decision:
    - Do you prefer simplicity- and higher assurance- to a feature-rich security environment?
- **(De) Centralised Controls**
    - 3rd Design Decision:
    - Should the tasks of defining and enforcing security be given to a central entity or should they be left to individual components in a system?
    - Central entity – could mean a bottleneck 
    - Distributed solution – more efficient but harder to manage
- **The Layer Below**
    - 4th Design Decision:
    - How can you prevent an attacker getting access to a layer below the protection mechanism?

**The onion model**

<img src="./assets/截屏2025-03-10 14.44.07.png" alt="截屏2025-03-10 14.44.07" style="zoom:50%;" />

