import requests
import os
import re

#set work-dir
os.chdir('C:\\Users\\Tuizhi\\Desktop\\tupian')
os.mkdir('tmaq')

#从合集开始，逐层爬取全部图片，eg为华晨宇合集
head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
picture_no = 1
for i1 in range(1, 5):
    url1 = 'http://www.win4000.com/mt/hcy_{}.html'.format(i1)
    re1 = requests.get(url1, headers=head)
    pattern1 = '"_blank" href="(.+?)"'
    set_url_list = re.findall(pattern, re1.content.decode())
    for i2 in set_url_list:
        set_room = requests.get(i2, headers=head)
        inter_h = re.match("(.+?).html", i2)
        pattern2 = 'href="({}.+?html)"'.format(inter_h.group(1))
        picture_url = re.findall(pattern2, set_room.content.decode())[2:]
        for i3 in picture_url:
            response3 = requests.get(i3, headers=head)
            picture_url_2 = re.findall(patern, response3.content.decode())
            for i4 in picture_url_2:
                picture = requests.get(i4, headers=head)
                with open('{}.jpg'.format(picture_no), 'wb') as f:
                    f.write(picture.content)
                    picture_no += 1
                    print("正在保存第%s张图片" % picture_no)

print("complete!!!")