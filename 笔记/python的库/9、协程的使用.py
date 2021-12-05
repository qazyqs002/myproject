# _*_ coding:utf-8 _*_
# File:9、协程的使用.py
# Time:2021/9/27  14:58
# Author: yqs
# * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *
"""
多协程的一些使用方式
"""
import asyncio
import time
import aiohttp

l_url = [
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
    "http://ad13in.gc-zb.com/",
]


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        data = []
        try:
            async with session.get(url, data=data, timeout=1) as res:
                # print(await res.content.read())
                return await res.content.read()
        except:
            print("抓取出现错误")


async def main():
    task = []
    for i in l_url:
        g = task.append(get_html(i))
        print(g)
    await asyncio.wait(task)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

