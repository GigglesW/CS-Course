# lec04: Authentication

[toc]

## Authentication

- To allow someone access to an asset we must ensure:
    - They are permitted to access that asset
    - They are who they say they are
- We can attempt to verify identity using credentials
    - Something they are
    - Something they have
    - Something they know

## Passwords

### Usernames and Passwords

- Identification – Who you are
- Authentication – Verify that identity
- Authentication should expire
    - “Remember my credentials” turns this into something you have
- **Time of check to time of use – TOCTTOU**
    - Repeated authentication
    - At the start and during a session
    
- Passwords are digital keys
    - Simple to implement using existing libraries
    - Demonstrates someone is who they say they are

### Problems with passwords

- **People forget them**
- **They can be guessed**
- **Spoofing and Phishing**

> - **Spoofing** is when someone pretends to be someone else
> - **Phishing** is a type of spoofing where attackers send fake emails or messages to get you to share sensitive information

### Password Policies

-  **Common Password Policies**
    - Certain length, certain types of characters
    - No dictionary words
    - Change regularly
    - No previously used passwords
- This is not a great solution
    - People attempt to make their life easier by re-using passwords
    - When they’re forced to change to unique passwords, they’ll simply increment a counter

### Storing passwords

- Storing passwords in plain text is a terrible idea
    - You might be hacked
    - Administrators can read them
- Storing **encrypted passwords** is better, but not perfect
    - Where are the keys stored?
    - Administrators can still read them
- Using a **one-way hash function** is a much better solution:

> **Hash function is a one-way function that takes an arbitraty length of input and returns a fix-length output.**

<img src="./assets/截屏2025-03-10 15.00.47.png" alt="截屏2025-03-10 15.00.47" style="zoom:50%;" />

## Cracking passwords

- Password cracking falls into two **basic types**:
- **Online**: 
    - You do not have the hash, and are instead **attempting to gain access to an actual login terminal**
    - Online is usually attempted with phishing
- **Offline: **
    - **You have a copy of the password hash locally**
    - Offline password cracking is simply a case of **trying lots of possible passwords**, and seeing if we have a hash collision with a password list
    - This could be done with a **Brute Force approach**


### Dictionary Attacks

- Most password cracking is now achieved using **dictionary attacks rather than brute force**
    - **Using a dictionary of common words and passwords**
    - **Apply small variations to this list, trying them all**
    - Combine words from two different lists
- `qwerty1234password1` is unbreakable using brute force, but won’t last against a dictionary attack

### Password Salting

- We can improve security by prepending a **random “salt**” to a password before hashing
- The salt is stored unencrypted with the hash:

<img src="./assets/截屏2025-03-10 15.10.58.png" alt="截屏2025-03-10 15.10.58" style="zoom:50%;" />

- If we use a different random salt for each user, we get the following security benefits:

    - **Cracking multiple passwords is slower** – a hit is for a single user, not all users with that password
    - **Prevents rainbow table attacks** – we can’t pre-compute that many password combinations
- **Salting has no effect on the speed of cracking a single password** – so make your passwords good!

### Hashing Speed

- When password cracking, the **most important factor is hashing speed**
- Newer algorithms take longer
    - Partly because they’re more complex
    - But some have been specifically designed to take a while

## Multi-factor authentication

- **Combines something you know with something you have**
- Common examples:
    - **Text codes to mobiles**
    - **One time passwords**, Google Authenticator, Microsoft Authenticator etc.
    - USB devices e.g. Yubico/Yubikey
- New devices and TOCTTOU are common uses for two-factor authentication

## Biometrics

- Measurements of the human body, something **you are**
- Various forms, fingerprint recognition, iris / retina recognition, voice, gait, typing rhythm
- **Pros**
    - **Unique to Individuals**
    - **Convenient and User-friendly**

- **Cons**
    - **Once stolen, can't be changed**
    - **False Positives/Negatives**


### Biometric Accuracy

- Usually operate by finding “features” within data, then use these to learn a template for a given individual
- The accuracy of a biometric system is extremely important
    - False positive rate
    - False negative rate
- There will usually be a **trade-off between FP and FN rates**







