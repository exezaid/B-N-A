import subprocess
import re

class Commands(object):

    def get_gateway(self):
        """docstring for fname"""
        trace_out = subprocess.Popen(["traceroute","-m 1","-q 5" ,"8.8.8.8"], shell=False, stdout=subprocess.PIPE)
        file_out = trace_out.stdout.read()
        txt=file_out
        re1='.*?'   # Non-greedy match on filler
        re2='(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?![\\d])'   # Uninteresting: ipaddress
        re3='.*?'   # Non-greedy match on filler
        re4='(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?![\\d])'   # Uninteresting: ipaddress
        re5='.*?'   # Non-greedy match on filler
        re6='(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?![\\d])'   # Uninteresting: ipaddress
        re7='.*?'   # Non-greedy match on filler
        re8='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])' # IPv4 IP Address 1

        rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
        m = rg.search(txt)
        if m:
            ipaddress1=m.group(1)
            print ipaddress1+"\n"
            self.gateway = ipaddress1

    def get_private_ip(self):
        """docstring for fname"""
        ip_out = subprocess.Popen(["ifconfig" ,"wlan0"], shell=False, stdout=subprocess.PIPE)
        txt2 = ip_out.stdout.read()
        re1='.*?'   # Non-greedy match on filler
        re2='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])' # IPv4 IP Address 1
        rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
        m = rg.search(txt2)
        if m:
            ipaddress=m.group(1)
            print ipaddress+"\n"
            self.private_ip = ipaddress


if __name__ == '__main__':
    cmd = Commands()
    cmd.get_gateway()
    cmd.get_private_ip()
