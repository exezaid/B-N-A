import unittest
from mock import create_autospec
from alive_ip import CurrentIp, FPing

class CurrentIpTest(unittest.TestCase):
    def setUp(self):
        ifconfig = create_autspec(ifconfig, )
        ifconfig = Mock(return_value = {'addr': '255.255.255.255',
                                        'brdaddr': '255.255.255.255',
                                        'hwaddr': '93:09:ff:ff:ff:ff',
                                        'netmask': '255.255.255.255'}
                       )
        self.current_ip = CurrentIp()
        self.current_ip.ifconfig = ifconfig

    def test_ip(self):
        self.assertEqual(self.current_ip.ip(), '255.255.255.255')

    def test_netmask(self):
        self.assertEqual(self.current_ip.netmask(), '255.255.255.255')

class FPingTest(unittest.TestCase):
    def setUp(self):
        #self.alive_ip_list = []
        self.alive_ips = [
          "10.92.0.1",
          "10.92.0.63",
          "10.92.0.80",
          "10.92.0.86",
          "10.92.0.81"
        ]
        self.fping_output = \
                    """
                    10.92.0.1
                    10.92.0.63
                    10.92.0.80
                    10.92.0.86
                    10.92.0.81
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.3
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.4
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.5
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.6
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.7
                    ICMP Host Unreachable from 10.92.0.162 for ICMP Echo sent to 10.92.0.8
                    """
        self.fping = FPing('255.255.255.255')
        self.fping.run = Mock(return_value = self.fping_output)

    def test_fping_ip_range(self):
        self.assertEqual(self.fping.fping_ip_range(), '255.255.255.0/24')

    def test_alive_ip(self):
        self.assertEqual(self.fping.alive_ips, self.alive_ip_list)

    def test_build_command(self):
        self.assertEqual(self.fping.build_command(), "fping -g -a -s 255.255.255.0/24")

    def test_alive_ips(self):
        self.assertEqual(self.fping.alive_ips(), self.alive_ips)

if __name__ == '__main__':
    unittest.main()
