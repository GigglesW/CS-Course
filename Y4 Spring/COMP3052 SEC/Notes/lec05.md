# lec05: Access Control

[toc]

## Access Control fundamentals

**Authentication & Authorisation**

- Subject / Principal – an active entity
- Object – resource being accessed
- Access an operation
- ==**Reference monitor – grants or denies access**==

**Access control has two steps:**

- **Authentication**: Decide who has access to the system 身份验证
- **Authorisation**: Of those with access, who is authorised to do something to the resource (object) 授权

## Principles, Subjects and Objects

- **Principal**: “An entity that can be granted access to objects or can make statements affecting access control decisions”
    - E.g **user identity** in an OS
    - Used when discussing security policies
- **Subject**: “An active entity within an IT system”
    - E.g. **process running** under a user identity
    - Used when discussing operational systems enforcing policies
- **Object** – Files or resources
    - E.g. **Memory, printers, directories**
- **Subject vs Object**: Distinguish between the **active and passive** party in an access request

## Access control structures

### Access Operations

- **Access modes**
    - **Observe** – Subject may look at contents of an object
    - **Alter** – Subject may change the contents of an object
- **Too abstract for practical use!**

**General Model**

- We’ll settle on some common access on files:
    - **Read** – Simply viewing (Confidentiality)
    - **Write** – Includes changing, appending, deleting (Integrity)
    - **Execute** – Can run the file without knowing its contents

**Ownership**

- Who is in charge of setting security policies?
- Discretionary: Owner can be defined for each resource
    - Owner controls who gets access
- Mandatory: Could be a system-wide policy
- Most OSs support the concept of ownership

**Access Control Structures**

- Access Control Matrix
- Access Control Lists
- Capabilities

### Access Control Matrix

- Access rights are defined individually for each combination of subject and object
    - Quite an abstract concept, but would allow for very fine grained control
    - Not practical, think of the memory required in scaling it up!

<img src="./assets/截屏2025-03-30 15.56.09.png" alt="截屏2025-03-30 15.56.09" style="zoom:50%;" />

### Access Control List

- Stored with an object itself, corresponding to **a column of an ACM**

<img src="./assets/截屏2025-03-30 15.56.25.png" alt="截屏2025-03-30 15.56.25" style="zoom:50%;" />

- **Pros**
    - Much less memory intensive
    - If stored with a file is quick to access
- **Cons**
    - Management of individual subjects is cumbersome
    - Obtaining an overview of permissions is challenging
    - Tedious to set this up properly for all subjects and objects

### Capabilities

- Access rights are stored with a subject, not a resource
- Every subject is given a capability:
    “An unforgeable token specifying the subject’s access rights”
- Corresponds to **a row in an access control matrix**:

<img src="./assets/截屏2025-03-30 15.58.24.png" alt="截屏2025-03-30 15.58.24" style="zoom:50%;" />

- Typically associated with discretionary access control
    - Subjects can pass on their capabilities
- **Not widely used** – e.g. exists in Linux but **rare**
- Difficult to get an overview of access rights on a file, and revoke them

## Groups and Roles

### Groups

- Users with similar access rights can be collected into groups
- Groups are given permissions to access objects

**Negative Permissions**

- An operation that a user cannot perform
- Policy conflict – resolved by the reference monitor

<img src="./assets/截屏2025-03-30 16.03.00.png" alt="截屏2025-03-30 16.03.00" style="zoom:50%;" />

### Roles

**Alternatives**

- **Identity Based Access Control (IBAC)**
    - **The standard approach** we’ve been discussing, e.g. **ACLs**
    - Scales better than a matrix, but not to enterprise level
- **Role-based Access Control (RBAC)**
    - **Access is based on a role**, e.g. accountants should access certain financial files
    - Easier to scale and use, but nothing is perfect!

**Role-based Access Control**

- **A role – Collection of application specific operations or resource access**
- Subjects derive access rights from the role they perform
- RBAC focuses on users and the jobs they perform
- Much **more applicable to large networks** and organisations

- Layers (between subjects and objects)
    - Roles – collection of procedures assigned to users
    - Procedures – high level access control methods
    - Data types – each object of certain data type

### Roles vs. Groups

- Sound the same, but are subtly different
    - Groups are **collections of users**
    - Roles are **collections of permissions**
- Most operating systems are user / group based, so role-based access can be provided using nested groups

<img src="./assets/截屏2025-03-30 16.06.12.png" alt="截屏2025-03-30 16.06.12" style="zoom:50%;" />

## **Evaluating Security Polices**

- At a basic level: quality check against Access Control Entry
- More complicated:
    - Protection Rings
    - Partial Orderings
    - Lattices

**Privileges**

- A **collection of rights** to execute certain operations
- Come pre-defined with an OS
- An intermediate layer between subjects and operations
- Usually associated with operating system functions
    - Installing software, network access etc.

### Protection Rings

- **Hardware-based access control**
- Each subject and object assigned a number depending on importance
- Decisions are made by comparing **subject’s to object’s numbers**

<img src="./assets/截屏2025-03-30 16.08.47.png" alt="截屏2025-03-30 16.08.47" style="zoom:50%;" />

### Partial Ordering

- Imagine groups containing students in year 1, year 2 etc.
- Partial orderings ( ≤ ) provide relations between subsets of groups
- For example, {Year1} ≤ {Year1, Year2}
- A security policy might grant access to an object if the subject label is ≤ object label

<img src="./assets/截屏2025-03-30 16.09.22.png" alt="截屏2025-03-30 16.09.22" style="zoom:50%;" />

### Lattices

<img src="./assets/截屏2025-03-30 16.09.46.png" alt="截屏2025-03-30 16.09.46" style="zoom:50%;" />

