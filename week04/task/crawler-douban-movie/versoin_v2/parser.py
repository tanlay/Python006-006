import sys
from bs4 import BeautifulSoup


def parse(page, movie_id, num):
    soup = BeautifulSoup(page, 'html.parser')

    data = []

    itemtemp = soup.select('#comments > div.comment-item')
    if len(itemtemp)==0:
        print("资源不存在")
        print(f"movie_id-{movie_id}累计爬取 {num} 个页面")
        sys.exit(404)
    for item in itemtemp:
        user = item.select_one('h3 > span.comment-info > a').get_text(strip=True)
        rating = item.select_one('h3 > span.comment-info > span.rating')
        star = None
        if rating is not None:
            star = rating.get('class')[0][7]
        comment = item.select_one('p > span.short').get_text(strip=True)
        ctime = item.select_one('h3 > span.comment-info > span.comment-time').attrs['title']

        data.append({
            'user': user,
            'star': star,
            'ctime': ctime,
            'comment': comment,
        })
    print(f"movie_id-{movie_id}: 数据提取完成")
    return data
