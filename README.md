# myping

## Introduction

This is a simple implement and modification by using the OS ping in python script.

You can use `myping` to send *ICMP* or *ICMPv6 ECHO-REQUEST*. It means that the address you ping can be IPv4, IPv6 or a domain name.

`myping 2001:48a8:68fe::52`

`myping 8.8.8.8`

`myping google.com`

If there is both an IPv4 and IPv6 address in this domain name, `myping` would use IPv6 first. You can also use option `-4` to specify that you prefer ICMPv4.

`myping -4 google.com`

## Environment

I develop and run this python script on FreeBSD 10.2 and Ubuntu 16.04.

Python version : 3.5.1

## Setup

`source setup.sh`

This command is just add `myping` to alias temportary.
