#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created by jianbing on 2017-09-21
"""
import requests
import bs4
import time
import json
import os


class Spider:
    def __init__(self):
        self._record_file = "record.txt"

    def _get_book_record(self, book_name):
        if not os.path.exists(self._record_file):
            with open(self._record_file, 'w', encoding='utf-8') as f:
                f.write("{}")

        with open(self._record_file, "r", encoding="utf-8") as f:
            r = json.loads(f.read())
            if book_name not in r:
                return 0
            else:
                return r[book_name]

    def _update_book_record(self, book_name, num):
        with open(self._record_file, "r+", encoding="utf-8") as f:
            r = json.loads(f.read())
            r[book_name] = num
            f.seek(0)
            f.write(json.dumps(r, ensure_ascii=False, indent=4))

    def _parse_url(self, url):
        return requests.get(url).content.decode('utf-8')

    def download(self, url):
        print("开始新任务，url是{}".format(url))
        content = self._parse_url(url)
        soup = bs4.BeautifulSoup(content, 'lxml')
        book_name = soup.find("h1").text

        sections = [i.find("a")["href"] for i in soup.find_all("dd")]
        print("书名：{}".format(book_name))
        print("当前总共{}章节".format(len(sections)))

        record = self._get_book_record(book_name)
        print("读取本地记录，已经累计下载{}章节".format(record))

        sections = sections[record:]
        if not sections:
            print("没有更新\n")
        else:
            for section in sections:
                content = self._parse_url("http://www.xxbiquge.com{}".format(section))
                soup = bs4.BeautifulSoup(content, 'lxml')

                title = soup.find(class_="bookname").find("h1").text
                content = soup.find(id="content").text
                content = [i.strip() for i in content.split("\xa0\xa0\xa0\xa0")]
                print(title)
                with open("{}.txt".format(book_name), "a+", encoding="utf-8") as f:
                    f.write("\n\n")
                    f.write(title)
                    f.write("\n")
                    f.write("\n".join(content))

                time.sleep(0.3)

            self._update_book_record(book_name, len(sections) + record)
            print("成功下载{}章节\n".format(len(sections)))


if __name__ == '__main__':
    s = Spider()
    s.download("http://www.xxbiquge.com/69_69372/")  # 武道宗师
