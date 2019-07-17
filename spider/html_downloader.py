import requests

# 功能：获取对应网址的网页
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers_pc = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
        # headers_mobile={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
        #                 "Accept":"text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8"}
        response = requests.get(url,headers=headers_pc,timeout=10)
        if response.status_code != 200:
            return None
        return response.content