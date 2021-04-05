from django.shortcuts import render


def parcing_news(request):
    # parcing
    from lxml import html
    import requests
    url = 'https://news.sportbox.ru/'
    response = requests.get(url)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        news = tree.xpath('//*[@id="b-actualy"]/div[1]/div[1]/div[*]/a/text()')
        news_ = []
        for new in news:
            new = new.replace('\n', '').strip()
            if new:
                news_.append(new)
        news_data = {'news': news_}
    else:
        news_data = {'news': 'there is no news'}
    # end parcing
    return render(request, 'news_page.html', news_data)