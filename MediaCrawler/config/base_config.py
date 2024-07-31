'''
Author: Interest 1368534721@qq.com
Date: 2024-04-24 15:56:04
LastEditors: Interest 1368534721@qq.com
LastEditTime: 2024-05-08 21:22:31
FilePath: \MediaCrawler\config\base_config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 基础配置
PLATFORM = "wb"
KEYWORDS = "北奥开幕式"
LOGIN_TYPE = "cookie"  # qrcode or phone or cookie
COOKIES = "SINAGLOBAL=2576677668574.29.1714458772777; UOR=,,cn.bing.com; ULV=1715133377433:4:3:2:3809458481519.5366.1715133377430:1715002187172; XSRF-TOKEN=EiRsXWoz6VZJSrLGvANe89DZ; Hm_lvt_d67baafd318097a18e70ee8d8d1de57a=1715002187,1715038761,1715133289,1715158188; SUB=_2A25LPww8DeRhGeFN4lQW-CrMyDWIHXVoNQH0rDV8PUNbmtAGLXnwkW9NQ7tTPjDaRYZWvwCg8L6f56_CdiIlVbLo; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhiuP1uu7AXBPyruanLFey_5NHD95QNe0.cS0nXehe4Ws4Dqcjci--Ri-zfi-zfi--fiK.0i-2fi--fi-2Xi-2Ni--ciKL2iKn7i--fiKLFiKLFi--ciK.ci-z4; ALF=02_1717766508; WBPSESS=Dt2hbAUaXfkVprjyrAZT_HZsYQHr-okI1A1vgOMcQNBO9yZtBkbgfGa8zE2Wt5RrCyz-Hn3FUKyiDL5rT-pS0j-j2s8Al8w-WGuTqLtCyxz50xA2hlN4fRG6nR59QxGOEaRn-Sf5z0qqhIJLqXn5pikbB5d5vFivI-Eb-gu0RYoksBRuDxApbWVc6giiVOEHS0iUHY14UYuk8fGRVpdAbQ==; Hm_lpvt_d67baafd318097a18e70ee8d8d1de57a=1715174511"
# 具体值参见media_platform.xxx.field下的枚举值，展示只支持小红书
SORT_TYPE = "popularity_descending"
CRAWLER_TYPE = "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 1

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器），设置False会打开一个浏览器（小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码）
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json
SAVE_DATA_OPTION = "csv"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 1000000000

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 4

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认不开启爬评论
ENABLE_GET_COMMENTS = True

# 是否开启爬二级评论模式, 默认不开启爬二级评论, 目前仅支持 xhs
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 指定小红书需要爬虫的笔记ID列表
XHS_SPECIFIED_ID_LIST = [
    "6422c2750000000027000d88",
    "64ca1b73000000000b028dd2",
    "630d5b85000000001203ab41",
    # ........................
]

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    #     "7280854932641664319",
    #     "7202432992642387233"
    #     # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = [
    "3xf8enb8dbj6uig",
    "3x6zz972bchmvqe"
]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    # "4982041758140155",
    # ........................
]

# 指定小红书创作者ID列表
XHS_CREATOR_ID_LIST = [
    "63e36c9a000000002703502b",
    # ........................
]
