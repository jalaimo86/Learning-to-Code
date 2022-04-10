#!/bin/python3

import dns.resolver
import dns.zone

ns_servers = []
def dns_zone_xfer(address):
    ns_answer = dns.resolver.query(address, 'NS')
    for server in ns_answer:
        print('[*] Found NS: {}'.format(server))
        ip_answer = dns.resolver.resolve(server.target, 'A')
        for ip in ip_answer:
            print("[*] IP for {} is {}".format(server, ip))
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip),address))
                for host in zone:
                    print("[*] Found Host: {}".format(host))
            except Exception as e:
                print("[*] NS {} refused zone transfer!".format(server))
                continue
def main():
    addr = input('what is the domain?')
    address = str(addr)
    dns_zone_xfer(address)
    
main()
    

