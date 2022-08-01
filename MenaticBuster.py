#!/usr/bin/python3
import argparse
from argparse import RawTextHelpFormatter
import logging
import random
import requests
import queue
import sys
import os
import threading
import time

color = True

machine = sys.platform # Detecting the os
if machine.lower().startswith(("os", "win", "darwin","ios")): 
    color = False # Colors will not be displayed on windows or Apple machines
if not color:
	reset = red = white = green  = blue = yellow = ""
else:                                                 
    white = "\033[97m"
    red = "\033[91m"    
    reset = "\033[0m"
    green = "\033[92m"
    blue = "\033[34m"
    yellow = "\033[1;33m"

banner = f'''{red}                                                                                 

    ▒█▀▄▀█ █▀▀ █▀▀▄ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ 　 ▒█▀▀█ █░░█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 
    ▒█▒█▒█ █▀▀ █░░█ █▄▄█ ░░█░░ ▀█▀ █░░ 　 ▒█▀▀▄ █░░█ ▀▀█ ░░█░░ █▀▀ █▄▄▀ 
    ▒█░░▒█ ▀▀▀ ▀░░▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀ 　 ▒█▄▄█ ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀                                                                                                                                         
    — 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝚋𝚢 𝙲𝚢𝚋𝚎𝚛 𝙼𝚎𝚗𝚊𝚝𝚒𝚌                          ~Version 1.0{reset}'''


middle_finger = f"""{red}
________________$$$$
______________$$____$$
______________$$____$$
______________$$____$$
______________$$____$$
______________$$____$$
__________$$$$$$____$$$$$$
________$$____$$____$$____$$$$
________$$____$$____$$____$$__$$
$$$$$$__$$____$$____$$____$$____$$
$$____$$$$________________$$____$$
$$______$$______________________$$
__$$____$$______________________$$
___$$$__$$______________________$$
____$$__________________________$$
_____$$$________________________$$
______$$______________________$$$
_______$$$____________________$$
________$$____________________$$
_________$$$________________$$$
__________$$________________$$
__________$$$$$$$$$$$$$$$$$$$$

{reset}"""
            


def MenaticBuster(passed_arguements):

    global file_extensions
    file_extensions = []

    if passed_arguements.extensions != None:
        file_extensions = passed_arguements.extensions.replace(
            ' ', '').replace('.', '').split(",")
        for eachfile_extension in range(len(file_extensions)):
            file_extensions[eachfile_extension] = '.' + file_extensions[eachfile_extension]     

    for each_thread in range(passed_arguements.threads):
        threads = threading.Thread(target=Bruteforcer, args = (
            passed_arguements, file_extensions))
        threads.daemon = True
        threads.start()
        try:
            while True:
                threads.join(1)
                if not threads.is_alive():
                    break
                time.sleep(2)
        except:
            RuntimeError("Something does not seem right. It completely Failed")


def check_wordlist_path(user_arguments, passed_arguements):
    if not os.path.exists(passed_arguements):
        print(f"{white}[{red}!{white}] The file {green}{passed_arguements}{white} path you entered is wrong you stupid little SKID!{reset}")
    else:
        print(f"\n{white}[☣] Bruteforce List  →  {green}{passed_arguements}{reset}")
        brutelistfile = open(passed_arguements, 'r')
        return brutelistfile


def save_target_log(hit_url):
    tstamp = time.localtime()
    timestamp = time.strftime("%H:%M:%S", tstamp)
    file = open(f'Hit_Log.txt', 'a')
    file.write(f'[{timestamp}] : {hit_url}\n')


def Bruteforcer(passed_arguements, file_extensions=None):
    try:
        if passed_arguements.url != None:
            url = passed_arguements.url
            if not passed_arguements.url.startswith('http://'):
                url = 'http://' + url
            if not url.endswith('/'):
                url = url + '/'
            else:
                url = url
        elif passed_arguements.url == None:
            print(middle_finger)
            print(f"\n{red}[!WARNING!] BRUH! COME ON, ENTER A URL TO BRUTEFORCE, DONT BE A PROPER SKID, OH MY DAYS!!!\n")


    except:
        raise ValueError(f"{red}[!] The following {passed_arguements.url} URL invalid Please Correct it{reset}")

    if passed_arguements.bruteforcelist !=None:
        word_list = passed_arguements.bruteforcelist
        word_queue = queue.Queue()
    else:
        print("[!WARNING!]IS YOUR DADDY GOING TO ENTER THE PATH TO THE WORDLIST? DONT BE A SCRIPT KIDDIE. USE THE HELP MENU AND USE THE RIGHT OPTION FOR THE TOOL TO WORK")
        print("\n[!WARNING!]TYPE python3 menaticbuster --help AND LOOK AT THE GOD DAMN [OPTIONS] MENU, FOOL!!!\n")
        exit(1)
    for each_word in word_list:
        each_word = each_word.rstrip()
        word_queue.put(each_word)
    found_url = []
    while not word_queue.empty():
        wordfromqueue = word_queue.get()
        hitlist = []

        if file_extensions:
            for extension in file_extensions:
                hitlist.append(f"{wordfromqueue}{extension}")
        else:
            hitlist.append(f"{wordfromqueue}")

        for brute in hitlist:
            try:

                hit_url = f"{url}{brute}"
                headers = {"User-Agent":f"{random.choice(userAgents)}"}
                response = requests.get(hit_url, headers=headers, verify=True, allow_redirects=True, timeout=5) 
                if response.status_code == 200:
                    if passed_arguements.save_output:
                        save_target_log(hit_url)
                    found_url.append(hit_url)
                    
                    print(f"{white}[{green}{response.status_code}{white}]FOUND| {green}{hit_url}{white}\n")

                elif response.status_code == 404:
                    if passed_arguements.verbose:
                        print(f"{white}[{red}{response.status_code}{white}] NOT FOUND| {red}{hit_url}{reset}\n")
                    else:
                        pass
                else:
                    if passed_arguements.verbose:
                        print(
                            f"{white}[{blue}{response.status_code}{white}] | {blue}{hit_url}{reset}")
                    else:
                        pass
            
            except requests.Timeout:
                if passed_arguements.verbose:
                	print(f"{white}[{yellow}!{white}] Request Timeout | {yellow}{hit_url}{reset}")

user_arguments = argparse.ArgumentParser(exit_on_error=False)
user_arguments = argparse.ArgumentParser(
    formatter_class=RawTextHelpFormatter,
    prog='MenaticBuster',
    description=f'MenaticBuster v1.0 - created by Cyber Menatic | {green} https://github.com/Menatic007/Menatic-Buster.git {reset}',
    epilog=f'{white}Menatic Buster is a Fast Directory Busting/Brute-forcing Tool, written in Python..{reset}')
user_arguments.add_argument('-t', dest='threads', type=int, help='Threads (default = 10)',
                            metavar='THREADS', default=10)
user_arguments.add_argument('-u', dest='url', type=str, help='Takes the URL as an argument',
                            metavar='URL', required=False, )
user_arguments.add_argument('-w', dest='bruteforcelist', help="Requires the path to the wordlist", type=lambda x: check_wordlist_path(user_arguments, x),
                            metavar='BRUTEFORCELIST', required=False)
user_arguments.add_argument('-o', '--output', dest='save_output', help='outputs the results to a file', action='store_true')
user_arguments.add_argument(
    '-v', dest='verbose', help='Shows the network logs and errors if any', action='store_true')
user_arguments.add_argument('-x', dest='extensions', help='looks for specific file extensions',
                            metavar='EXTENSIONS')
user_arguments.add_argument('-q', '--QUIET', dest='quiet', action='store_true',
                            default=False, help='does not display a banner and executes in quiet mode')
passed_arguements = user_arguments.parse_args()

userAgents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4091.2 Safari/537.36",
                           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
                           "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.90 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
                           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
                           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36,gzip(gfe)",
                           "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
                           "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.185.1002 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.99",
                           "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
                           "Mozilla/5.0 (Linux; Android 11; SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
                           "Mozilla/5.0 (Linux; Android 8.0.0; SM-A750GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/169.1.385914506 Mobile/15E148 Safari/604.1",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36/swoLZb83-26"]

if __name__ == '__main__':
    try:
        print(f"{white}[☣] Locking on Target → {green}{passed_arguements.url}{reset}")
        if passed_arguements.quiet:
            pass
        else:
            print(banner)
            print(f"""{green}
__________________________________________________________________________
       
        [☠] TARGET SUCCESSFULLY LOCKED IN. BUSTING TARGET NOW [☠]
__________________________________________________________________________
        
        {reset}""")
        MenaticBuster(passed_arguements)
    except KeyboardInterrupt:
        if passed_arguements.verbose:
            print(f"{white}[{red}!{white}] Detected Ctrl + C. I am Exiting...BYE{reset}");time.sleep(1);sys.exit(1)
        sys.exit(1)
    except Exception as e:
        if passed_arguements.verbose:
            print(f"{white}[{red}!{white}] An error occured: {red}{e}{reset}")
