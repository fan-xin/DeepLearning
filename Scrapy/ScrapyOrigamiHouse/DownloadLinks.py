import requestsimport refrom urllib.parse import urljoinimport csvimport chardetimport urllibdef caiji(url):    response = urllib.request.urlopen('https://www.origamihouse.jp/book/original/house.html')    print(response.read().decode('Shift_JIS'))    # 准备要保存的文件    file = open('result.csv', 'w', encoding='utf-8', newline='')    cw = csv.writer(file)    cw.writerow(['URL', 'Anchor'])    resp = requests.get(url)    encoding = chardet.detect(resp.content)["encoding"]    # print(encoding)    resp.encoding = encoding    link_list = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', resp.text, re.S|re.I)    for link in link_list:        a = urljoin(url, link[0]), link[1]        print(a)        cw.writerow(a)    file.close()if __name__ == '__main__':    url = 'https://www.origamihouse.jp/book/original/house.html'  # 要采集的URL    caiji(url) 