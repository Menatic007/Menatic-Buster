# [🕸] Menatic Buster 

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/Menatic007/Menatic-Buster?style=flat-square)
![GitHub](https://img.shields.io/github/repo-size/Menatic007/Menatic-Buster)
![GitHub](https://img.shields.io/tokei/lines/github.com/Menatic007/Menatic-Buster)
![GitHub](https://img.shields.io/github/forks/Menatic007/Menatic-Buster?style=flat-square)
![GitHub](https://img.shields.io/github/stars/Menatic007/Menatic-Buster?style=social)

# [📑] Description

<p>A Fast CLI based Multi-Threaded Directory Bruteforcing  Tool written in Python. This tool can come in handy while doing CTF's or Bug Bounty Hunting to discover hidden directories and files by launching an attack against the web server. This is an inital realse of the tool, moving forward alot more upgrades will be added to enhance its speed and performance.</p> 

[![Screenshot-2022-06-12-at-21-10-53.png](https://i.postimg.cc/MGPCwc33/Screenshot-2022-06-12-at-21-10-53.png)](https://postimg.cc/R3tsQ0Bw)

# [❗️] Disclaimer 

<p>The exploits and malware built on this respository are mainly for POC and Educational purposes only. The developer is in no way responsible for any sort of misuse of tools and exploits or spreading of malware from this respository.</p>

# [✦] Installation

  <h2>Linux </h2>  

  - <code>git clone https://github.com/Menatic007/Menatic-Buster</code>
  - <code>cd Menatic-Buster</code>
  - <code>pip install -r requirements.txt</code>
  - <code>sudo chmod +x MenaticBuster</code>
  - <code>./MenaticBuster.py</code>
  
 # [⚙️] Usage
 ```
- Basic usage:

- ./MenaticBuster -u <target_url> -w <path/to/wordlist> 
 
- To use extensions and more features use the help menu and enter the respective command.
  
- Help Menu:
  
./MenaticBuster --help
 
- Note:
  
 Entering the wrong commands could lead to the tool abusing you.
 So make sure you enter the arguements correctly 😂
```
 # [⚒] Adding program into Binaries
  ```
 If you want to use the tool just by typing its name in the terminal, 
 then do the following after finishing the steps of Installation:
  
 sudo mv MenaticBuster.py /usr/bin/MenaticBuster
 sudo chmod +x /usr/bin/MenaticBuster
  
 Now you can run the tool just by typing:
 MenaticBuster [OPTIONS]
 ```
