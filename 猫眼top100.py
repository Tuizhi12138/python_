import re
import requests
import os


def get_content(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    respones = requests.get(url, headers=header)
    return respones.content.decode()


def parse(res):
    pattern = re.compile(
        '<dd>.+?board-index-(\d{1,3}).+?title="(.+?)" class.+?<img data-src="(.+?)@.+?(主演：.+?)\n.+?(上映时间.+?)</p>.+?class="integer">(\d\.)<.+?class="fraction">(\d)<.+?</dd>',
        re.S)
    content = re.findall(pattern, res)
    return content


def save_to_csv(content):
    with open('猫眼100.txt', 'w') as f:
        for line in content:
            f.write('\t'.join(line).replace('.\t', '.', 1))
            f.write('\n')


def main():
    sum1 = []
    for i in range(0, 10):
        url = 'https://maoyan.com/board/4?offset={}'.format(i * 10)
        respone = get_content(url)
        content = parse(respone)
        for n in content:
            sum1.append(n)
    save_to_csv(sum1)


main()