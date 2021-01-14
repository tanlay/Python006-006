import requests


def download(url):
    HEADERS = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=HEADERS, timeout=5)
        print(f'正在抓取: {url}')
        res.raise_for_status()
        return res.text
    except Exception:
        return  "抓取失败"
