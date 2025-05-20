# lec14: Database Security 

[toc]

## Database Security

<img src="./assets/截屏2025-05-13 14.55.04.png" alt="截屏2025-05-13 14.55.04" style="zoom:50%;" />

**SQL Security**

- **Three Entities**
    - Users
    - Actions
    - Objects
- Users invoke actions on objects
- Newly created objects are owned by the creator

### Views

**Why Views**

- Views are a flexible way of creating policies closer to application requirements
- Views can enforce context-dependent and data-dependent policies
- Views can implement controlled invocation
- Data can be easily reclassified

**Why Not**

- INSERT / UPDATE actions depend on the CHECK options, else might be blind inserts
- Definitions must be correct in order to capture intended security policy
- Completeness and consistency are not achieved automatically
- Can quickly become very inefficient

## Statistical Database

**Statistical Database**

- Where access to data is restricted, access to **aggregates** might still be permitted:

- COUNT, SUM, AVG, MAX, MIN

**Tracking**

- **Direct attack**
    - Aggregate is computed to capture information of individual data elements
- **Indirect**
    - Combines information from several aggregates
- **Tracker Attack**
    - Generalised indirect attack

**Further Defences**

- **Data swapping** – Swap records but keep stats the same
- **Noise addition** – Alter aggregate output (a little)
- **Table splitting** – Separate data completely
- **User tracking** – Log queries

## SQL Injection

- **SQL Injection**
    - **Unexpected user input can completely rewrite the query.**
- **Blind SQL Injection**
    - A blind SQL injection performs database analysis without any actual output
    - 通过分析数据库的响应，推测出数据和结构
- **Fingerprinting the DB**
    - Some commands are specific to an individual DBMS, Once you know the DB, access the system tables:
    - **The process of identifying the type of the DBMS used by a target system**
    - 攻击者利用特定的 SQL 命令来识别数据库管理系统（DBMS）类型
- **Second Order SQL Injection**
    - **Store the exploit in one pass, then have it executed later**
    - 攻击者通过先存储恶意数据在数据库中，然后等待系统在后续的操作中执行这些恶意数据，从而实现攻击