from flask import Flask, request, redirect
import requests

from mirrors import get_country, FALLBACK_URL

ARCHIVE_URL = "https://archive.laniakeaos.com"

app = Flask(__name__)

def make_redirect_url(base_url: str, repo: str, arch: str="x86_64") -> str:
    return base_url.replace('$repo', repo).replace('$arch', arch)


def get_country_and_print(ip_addr: str):
    country = get_country(ip_addr)
    print(f"{ip_addr} - {country['display_name']}")

    return country


@app.route("/ping")
def ping():
    return ""


@app.route("/laniakea/core/x86_64/<path:path>")
def catch_core(path):
    repo = "core"
    arch = "x86_64"

    success = False

    redirect_url = f"{ARCHIVE_URL}/laniakea/{repo}/{arch}/{path}"
    res = requests.head(redirect_url)
    status = res.status_code
    if status == 200:
        return redirect(redirect_url)
    else:
        country = get_country_and_print(request.remote_addr)

        for mirror in country["mirrors"]:
            redirect_url = make_redirect_url(mirror, repo, arch) + f"/{path}"
            res = requests.head(redirect_url)
            status = res.status_code
            if status == 200:
                success = True
                break

        if success is True:
            return redirect(redirect_url)
        else:
            redirect_url = make_redirect_url(FALLBACK_URL, repo, arch) + f"/{path}"
            return redirect(redirect_url)


@app.route("/laniakea/extra/x86_64/<path:path>")
def catch_extra(path):
    repo = "extra"
    arch = "x86_64"

    success = False

    redirect_url = f"{ARCHIVE_URL}/{repo}/{arch}/{path}"
    res = requests.head(redirect_url)
    status = res.status_code
    if status == 200:
        return redirect(redirect_url)
    else:
        country = get_country_and_print(request.remote_addr)

        for mirror in country["mirrors"]:
            redirect_url = make_redirect_url(mirror, repo, arch) + f"/{path}"
            res = requests.head(redirect_url)
            status = res.status_code
            if status == 200:
                success = True
                break

        if success is True:
            return redirect(redirect_url)
        else:
            redirect_url = make_redirect_url(FALLBACK_URL, repo, arch) + f"/{path}"
            return redirect(redirect_url)
