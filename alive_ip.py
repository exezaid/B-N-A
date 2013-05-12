import re
from subprocess import Popen, PIPE, STDOUT
from ifconfig import ifconfig
from script_commands import Commands

class CurrentIp():
    def __init__(self, interface = 'wlan0'):
        self.ifconfig_output = ifconfig(interface)

    def ip(self):
        return self.ifconfig_output['addr']

    def netmask(self):
        return self.ifconfig_output['netmask']


class FPing():
    def __init__(self, ip):
        self.pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        self.ip = ip
        self.cache = None

    def fping_ip_range(self):
        arr = self.ip.split(".")
        arr[3] = "0/24"
        return (".").join(arr)

    def build_command(self):
        return ["fping", "-g", "-a", "-s", self.fping_ip_range()]

    def run(self):
        if self.cache:
            return self.cache
        else:
            self.cache = Popen(self.build_command(),
                               stdout=PIPE,
                               stderr=STDOUT).communicate()[0]
            return self.cache

    def alive_ips(self):
       arr = self.run().split("\n")
       return filter(lambda cad: self.pattern.match(cad), arr)

    def remove_special_ip(self, ip_list):
       ip_list = self.alive_ips()
       for ip in ip_list:
           ip_list.remove(ip)
       return ip_list

if __name__ == "__main__":
    cmd = Commands()
    ip = cmd.private_ip
    fping = FPing(ip)

    print fping.remove_special_ip(cmd.ips())
