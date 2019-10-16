#!/usr/bin/env python
from cli import cli
import subproccess

#This Script test outbound connectivity, if it fails it will reset modem

def test_conn():
	
	ipadd = "10.73.131.44"

    response = subprocess.run(["ping", "-c", "1", ipadd], stdout=subprocess.PIPE)
    answer = response.returncode
    if answer == 1:
        print("Cannot Ping")
        return False
    elif answer == 0:
        print("Can Ping!")
        return True

def log(message, severity):
    cli('send log {} {}'.format(severity, message))


def reschedule(seconds, diff):
    UPDATE_SCRIPT_FIRING_COMMANDS = """
 event manager applet ACL-SYNC-CHECK
 event timer watchdog time %s
 action 1.0 cli command "enable"
 action 1.1 cli command "guestshell run /home/guestshell/reboot_conn.py
"""
    configure(UPDATE_SCRIPT_FIRING_COMMANDS % (seconds))
    if answer == False:
	    log("Cannot Reach Headend",4)
        cli('test cellular 0/2/0 modem-power-cycle')


def main():

	answer = test_conn()
    #specify in seconds how long to wait between checks.
    reschedule(1800, answer)



if __name__ == "__main__":
    main()