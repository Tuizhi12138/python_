import requests
import os
import re


def get_url(url):
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    respones = requests.get(url, headers=head)
    return respones.content


def get_set(url):
    set_content = get_url(url)
    url_list = []
    pattern = 'href="(http://www.win4000.com/meinv.+?)" target="_blank"'
    set_url_list = re.findall(pattern, set_content.decode())
    for i in set_url_list:
        url_list.append(i)
    return url_list


def get_book(url_list):
    pic_url_list = []
    for i in url_list:
        set_room = get_url(i)
        inter_h = re.match("(.+?).html", i)
        pattern2 = 'href="({}.+?html)"'.format(inter_h.group(1))
        picture_url = re.findall(pattern2, set_room.decode())[2:]
        for item in picture_url:
            pic_url_list.append(item)
    return pic_url_list


def get_picture(url_list):
    page_list = []
    for i in url_list:
        page = get_url(i)
        pattern = 'url="(.+?jpg)"'
        picture_url_2 = re.findall(pattern, page.decode())
        for item in picture_url_2:
            page_list.append(item)
    return page_list


def save(picture, picture_no):
    with open('{}.jpg'.format(picture_no), 'wb') as f:
        f.write(picture)
        print("正在保存第%s张图片" % picture_no)


def main(url):
    picture_no = 1
    for n in range(5):
        set_url_list = get_set(url.format(n + 1))
        pic_url_list = get_book(set_url_list)
        page_list = get_picture(pic_url_list)
        for m in page_list:
            picture = get_url(m)
            save(picture, picture_no)
            picture_no += 1
    print("complete!!!")


url = 'http://www.win4000.com/meinvtag6_{}.html'
main(url)