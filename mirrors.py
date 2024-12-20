import ipaddress

FALLBACK_URL = "https://mirror.rackspace.com/archlinux/$repo/os/$arch"

ip_addresses = {
    "jp": {
        "ipv4": [
            "123.0.0.0/8",
            "124.0.0.0/8",
            "210.0.0.0/8",
            "211.0.0.0/8",
            "220.0.0.0/8",
            "27.0.0.0/8",
            "180.0.0.0/8",
            "49.0.0.0/8",
        ],
        "ipv6": [
            "2400:0000::/4",
            "2001:200::/23",
            "2001:218::/23",
        ],
    },
    "kr": {
        "ipv4": [],
        "ipv6": [],
    },
}

countries = {
    "jp": {
        "display_name": "Japan",
        "mirrors": [
            "https://mirrors.cat.net/archlinux/$repo/os/$arch",
            "https://ftp.jaist.ac.jp/pub/Linux/ArchLinux/$repo/os/$arch",
        ],
    },
    "us": {
        "display_name": "United States",
        "mirrors": [
            "https://arlm.tyzoid.com/$repo/os/$arch",
        ],
    },
}

def get_country(ip_addr: str):
    country_code = "us"
    for country in ip_addresses.keys():
        ipv4_li = list(ipaddress.ip_network(r) for r in ip_addresses[country]["ipv4"])
        ipv6_li = list(ipaddress.ip_network(r, strict=False) for r in ip_addresses[country]["ipv6"])
        if any(ipaddress.ip_address(ip_addr) in ipnet for ipnet in ipv4_li):
            country_code = country
        elif any(ipaddress.ip_address(ip_addr) in ipnet for ipnet in ipv6_li):
            country_code = country

    if country_code == "ko":
        return countries["jp"]
    else:
        return countries[country_code]

## Japan
# 123.0.0.0/8
# 124.0.0.0/8
# 210.0.0.0/8
# 211.0.0.0/8
# 220.0.0.0/8
# 27.0.0.0/8
# 180.0.0.0/8
# 49.0.0.0/8
# 27.0.0.0/8