# An IP address is a numerical label assigned to each device
# (e.g., computer, printer) participating in a computer network
# that uses the Internet Protocol for communication.
# There are two versions of the Internet protocol,
# and thus two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example

# For inputString = "172.16.254.1", true;

# For inputString = "172.316.254.1", false.
# 316 is not in range [0, 255].

# For inputString = ".254.255.0", false.
# There is no first number.

import ipaddress


def solution(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True
# ---------------------------------------------


def solution(inputString):
    segments = inputString.split('.')
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit() or not 0 <= int(segment) < 256 or (segment[0] == '0' and len(segment) > 1):
            return False
    return True
