# DNS Resolver

System Integrations Assignment 1 - Chakkarin Laksanakesim D21125387

DNSResolver.py is an implementation of a working DNS resolver. The resolver operates like
the nslookup. The user is able to specify a domain name as a command line argument.
The resolver will then query the DNS server for the IP address of the domain name.
Returning IPv4 and IPv6 addresses if they exist as A or AAAA records respectively.
Along with the CNAME record if it exists.

Written in Python 3.9

DNS Server specified in DNSResolver.py is
```
UDP_IP = "google-public-dns-a.google.com"
UDP_PORT = 53
```

## Usage
```
python3 DNSResolver.py <domain name>
```

## Example
```
python3 DNSResolver.py google.com github.com support.dnsimple.com
```

## Output
```
google.com has an IPv4 address of 74.125.193.139
google.com has an IPv4 address of 74.125.193.113
google.com has an IPv4 address of 74.125.193.101
google.com has an IPv4 address of 74.125.193.138
google.com has an IPv4 address of 74.125.193.102
google.com has an IPv4 address of 74.125.193.100
github.com has an IPv4 address of 140.82.121.3
support.dnsimple.com is an alias for dnsimple-support.netlify.app
support.dnsimple.com has an IPv4 address of 18.192.94.96
support.dnsimple.com has an IPv4 address of 35.156.224.161
google.com has an IPv6 address of 2a00:1450:400b:c01::8a
google.com has an IPv6 address of 2a00:1450:400b:c01::71
google.com has an IPv6 address of 2a00:1450:400b:c01::64
google.com has an IPv6 address of 2a00:1450:400b:c01::66
support.dnsimple.com is an alias for dnsimple-support.netlify.app
support.dnsimple.com has an IPv6 address of 2a05:d014:58f:6200::64
support.dnsimple.com has an IPv6 address of 2a05:d014:275:cb02::c8
```

## Marking Criteria

- [x] It should accept domains passed to it by the user in the form of a command line argument
- [x] It should send valid DNS requests via the network to look up the given domain
- [x] It should receive and parse the returned DNS response to extract IP addresses and canonical
names and display this information in human-readable form to the user
- [x] Ideally, the resolver should have support for both IPv4 and IPv6. This means that the
resolver will actually make two requests per lookup: one for the A QTYPE and another for
the AAAA QTYPE.
- [x] The output should be presented in human-readable form, meaning:
- - [x] IPv4 addresses should be displayed as four unsigned decimal numbers separated by dots
- - [x] IPv6 addresses should be displayed as eight 4-digit hexadecimal numbers separated by
colons, with a long run of zeros in the address being replaced with a double colon
- - [x] Canonical names should be displayed as domains, i.e. as a sequence of characters
separated by dots
