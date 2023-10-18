import random
import sys
import DNSStarter as dns
import socket
import re

UDP_IP = "google-public-dns-a.google.com"
UDP_PORT = 53

# domains from command line arguments exit with an error if otherwise
if len(sys.argv) < 2:
    sys.exit("Invalid Arguments: Please specify domain names")

for domain in sys.argv[1:]:
    domain_regex = re.compile(
        r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+$'
    )

    if not domain_regex.match(domain):
        sys.exit(f"Invalid Domain: {domain}")


# convert list of integers to dotted decimal notation
def dotted(d: list) -> str:
    return '.'.join(map(str, d))


# convert list of integers to IPv6 address
def parse_ipv6(ipv6: list) -> str:
    return socket.inet_ntop(socket.AF_INET6, bytes(ipv6))


# lookup function to send DNS queries and print responses
def lookup(qtype: int, domains: list) -> None:
    for domain in domains:
        # create a DNS question for each domain
        question = dns.DNSQuestion(
            name=domain.split('.'),
            qtype=qtype,
            qclass=1
        )
        # create a DNS header for each domain
        header = dns.DNSHeader(
            ident=random.randint(0, 65535),
            rd=1,
            qdcount=1,
            ancount=0,
            arcount=0,
            nscount=0,
            opcode=0,
            index=0,
            rcode=0,
            z=0,
            aa=0,
            qr=0,
            ra=0,
            tc=0
        )

        # create DNS Datagram for each domain
        datagram = dns.DNSDatagram(
            header=header,
            questions=[question],
            answers=[],
        )

        # Write datagram
        serialised = dns.write_datagram(datagram)

        # Send datagram using UDP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(serialised, (UDP_IP, UDP_PORT))

        response, _ = sock.recvfrom(1024)

        # Read datagram response as DNSDatagram
        deserialised: dns.DNSDatagram = dns.read_datagram(response)

        # Print response
        for answer in deserialised.answers:
            if answer.type == 1:
                print(f"{domain} has an IPv4 address of {dotted(answer.rdata)}")
            elif answer.type == 5:
                cname = answer.cname_as_array_list(deserialised)
                print(f"{domain} is an alias for {dotted(cname)}")
            elif answer.type == 28:
                print(f"{domain} has an IPv6 address of {parse_ipv6(answer.rdata)}")
            else:
                print(f"{domain} unimplemented support for type: {answer.type}")

        # Close socket
        sock.close()


# lookup A records
print("Returning A record addresses")
lookup(1, sys.argv[1:])
# lookup AAAA records
print("Returning AAAA record addresses")
lookup(28, sys.argv[1:])
