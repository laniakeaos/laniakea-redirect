import ipaddress

from ipwhois import IPWhois

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
        whois = IPWhois(ip_addr)
        result = whois.lookup_rdap()
        country_code: str = result.get("asn_country_code", "us")
        country_code = country_code.lower()
    except:
        pass

    if country_code == "ko":
        return countries["jp"]
    else:
        return countries[country_code]
