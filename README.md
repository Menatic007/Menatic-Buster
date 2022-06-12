# [🕸] Menatic Buster 
<p>A Fast CLI based Multi-Threaded Directory Bruteforcing  Tool written in Python. This tool can come in handy while doing CTF's or Bug Bounty Hunting to discover hidden directories and files by launching an attack against the web server. This is an inital realse of the tool, moving forward alot more upgrades will be added to enhance its speed and performance.</p> 
# [❗️] Disclaimer 
<p>The exploits and malware built on this respository are mainly for POC and Educational purposes only. The developer is in no way responsible for any sort of misuse of tools and exploits or spreading of malware from this respository.</p>
# [✦] Installation
  <h2> Linux </h2>  

  - <code>gitclone https://github.com/Menatic007/Menatic-Buster</code>
  - <code>cd Menatic-Buster</code>
  - <code>pip install requirements.txt</code>
  - <code>sudo chmod +x MenaticBuster</code>
  - <code>sudo ./MenaticBuster</code>
  
 # [] Usage
``` 
- Basic usage:
- ./MenaticBuster -u <target_url> -w <path/to/wordlist> 
 
- To use extensions and more features use the help menu and enter commands the respective command.
  
- Help Menu:
  
  ./MenaticBuster --help
  
 - Note:
  
  Enter the wrong commands could lead to the tool abusing you. So 
  make sure you enter the commands and arguements correctly 😂
 ``` 
  # [] Adding program into Binaries
  ```
  If you want to use the tool just by typing its name in the terminal, 
  then do the following after finishing the steps of Installation:
  
  sudo mv MenaticBuster.py /usr/bin/MenaticBuster
  sudo chmod +x /usr/bin/MenaticBuster
  ```
