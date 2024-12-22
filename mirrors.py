import ipaddress

from ipwhois import IPWhois


ip_data = {}


FALLBACK_URL = "https://mirror.rackspace.com/archlinux/$repo/os/$arch"


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

    try:
        country_code = ip_data.get(ip_addr, None)

        if country_code is None:
            whois = IPWhois(ip_addr)
            result = whois.lookup_rdap()
            country_code: str = result.get("asn_country_code", "us")
            country_code = country_code.lower()
            # Store.
            ip_data[ip_addr] = country_code
    except:
        country_code = "us"

    if country_code == "ko":
        return countries["jp"]
    else:
        return countries[country_code]
