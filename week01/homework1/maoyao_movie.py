import requests
from bs4 import BeautifulSoup as bs
import lxml.etree

if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/84.0.4147.89 Safari/537.36'
    cookie = '__mta=252622518.1595650195812.1595650202534.1595650884308.3; uuid_n_v=v1; ' \
             'uuid=B0909650CE2C11EABD387F49F1B53159B760D7CF43214F26B039F96593647545; _' \
             'csrf=48f3ebd78d079cf79ced7fbd829b0323ea8af58ac3c256ee988e37aa31918e10; _' \
             'lxsdk_cuid=1738429c1525e-06576d1272145c-b7a1334-e1000-1738429c153c8; _' \
             'lxsdk=B0909650CE2C11EABD387F49F1B53159B760D7CF43214F26B039F96593647545; ' \
             'mojo-uuid=8952e68678cf4ee891028379421fab65; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595650196,1595650203,' \
             '1595652263; mojo-session-id={"id":"ebf7be98b783391b74c05d36a024d9a2","time":1595654602344}; ' \
             'mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595654602; __' \
             'mta=252622518.1595650195812.1595650884308.1595654602500.4; _lxsdk_s=173846cfa9b-82b-4ab-fd6%7C%7C3'
    header = {'user-agent': user_agent, 'cookie': cookie}
    my_url = "https://maoyan.com/films?showType=3"
    response = requests.get(url=my_url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    movie_list = bs_info.find('dl', attrs={'class':'movie-list'})
    count = 10
    movies = []
    for movie in movie_list.find_all('dd'):
        print("#################################")
        movie_content = movie.find('a')
        movie_link = movie.find('a').get('href')
        movie_name = movie.find('div', attrs={'class':'channel-detail movie-item-title'})['title']
        print(movie_name)
        print(movie_link)

        movie_link = 'https://maoyan.com' + movie_link
        response = requests.get(url=movie_link, headers=header)
        selector = lxml.etree.HTML(response.text)
        movie_type = selector.xpath("//div[@class='movie-brief-container']//a/text()")
        print(movie_type)
        plan_date = selector.xpath("//div[@class='movie-brief-container']//ul/li[3]/text()")
        print(plan_date)
        movie = {'name' : movie_name, 'type': movie_type, 'date': plan_date}
        movies.append(movie)

        count -= 1
        if count == 0:
            break

    print(movies)

    # write to the file
    import pandas as pd
    movie = pd.DataFrame(data=movies)
    movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)

