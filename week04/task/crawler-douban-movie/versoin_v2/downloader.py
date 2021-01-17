import requests


def download(url):
    HEADERS = {
    	'Cookie': 'bid=ifR0DONqaXQ; _ga=GA1.2.389224859.1609230217; ll="108307"; __gads=ID=8b3edf27554ae7e8-2294075e5ec500c7:T=1609230410:RT=1609230410:S=ALNI_Ma2NDnKlflP5WVxO-lSwxEwrfQAnA; __yadk_uid=Tu8ApgwemIRRqts56TJd3tVFoA6sB30C; _vwo_uuid_v2=D54DBAB22FDE80AE09F2E29ED113FF125|a60904c65bfbb2f939157e30b7dff308; push_doumail_num=0; push_noty_num=0; douban-fav-remind=1; viewed="35005327"; gr_user_id=c4585f58-6ab4-4100-8f0c-3a29252ce01d; ct=y; __utmz=30149280.1610529286.20.4.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1610529288.19.3.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610807219%2C%22https%3A%2F%2Fsearch.douban.com%2Fmovie%2Fsubject_search%3Fsearch_text%3D%25E6%25A5%259A%25E9%2597%25A8%26cat%3D1002%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.389224859.1609230217.1610787136.1610807219.27; __utmb=30149280.0.10.1610807219; __utmc=30149280; __utma=223695111.1111821169.1609230217.1610787136.1610807219.26; __utmb=223695111.0.10.1610807219; __utmc=223695111; dbcl2="148486800:Emj2Kjdgcnc"; ck=8bX_; _pk_id.100001.4cf6=cb1c80ef810695a8.1609230217.26.1610807232.1610789583.',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=HEADERS, timeout=5)
        print(f'正在抓取: {url}')
        res.raise_for_status()
        return res.text
    except Exception:
        return  "抓取失败"
