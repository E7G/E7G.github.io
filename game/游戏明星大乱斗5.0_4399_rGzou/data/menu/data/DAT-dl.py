import requests

cookies = {
    '_gprp_c': '""',
    '_4399stats_vid': '15915064163767753',
    'UM_distinctid': '181f77372ca10d-04a40856b097fa-4e4c0f20-1aeaa0-181f77372cb33b',
    'Puser': '2502710498',
    'Qnick': '',
    'Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7': '1657723235',
    'home4399': 'yes',
    'Hm_lvt_334aca66d28b3b338a76075366b2b9e8': '1657713947,1657717712,1659348126',
    'USESSIONID': 'f25fcfd3-1740-45d9-b35f-131ff3b08038',
    'phlogact': 'l136163',
    'Uauth': '4399|1|202281|dev4399.|1659348166685|db94486c858fda54a4a14102688b02da',
    'Pauth': '3827955277|2502710498|t3ce7n18384537b36f95897dde3bee3a|1659348166|10002|c0690702cd227ee92b033f56ac7020ff|0',
    'ck_accname': '2502710498',
    'Xauth': '160008c081b3ee0cd5c2075240a310dc',
    'ptusertype': 'dev4399.4399_login',
    'Pnick': '0',
    'Hm_lpvt_334aca66d28b3b338a76075366b2b9e8': '1659349222',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': '*/*',
    'X-Requested-With': 'ShockwaveFlash/32.0.0.465',
    'Referer': 'http://sda.4399.com/4399swf/upload_swf/ftp14/yzg/20140909/1/game.htm?title=%E6%B8%B8%E6%88%8F%E6%98%8E%E6%98%9F%E5%A4%A7%E4%B9%B1%E6%96%975.0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gprp_c=""; _4399stats_vid=15915064163767753; UM_distinctid=181f77372ca10d-04a40856b097fa-4e4c0f20-1aeaa0-181f77372cb33b; Puser=2502710498; Qnick=; Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7=1657723235; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1657713947,1657717712,1659348126; USESSIONID=f25fcfd3-1740-45d9-b35f-131ff3b08038; phlogact=l136163; Uauth=4399|1|202281|dev4399.|1659348166685|db94486c858fda54a4a14102688b02da; Pauth=3827955277|2502710498|t3ce7n18384537b36f95897dde3bee3a|1659348166|10002|c0690702cd227ee92b033f56ac7020ff|0; ck_accname=2502710498; Xauth=160008c081b3ee0cd5c2075240a310dc; ptusertype=dev4399.4399_login; Pnick=0; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1659349222',
}

for i in range(100,201):
    name="DAT"+str(i)+".ssf"
    print("正在下载："+name)
    response = requests.get('http://sda.4399.com/4399swf/upload_swf/ftp14/yzg/20140909/1/data/menu/data/'+name, cookies=cookies, headers=headers, verify=False)
    open(name,"wb").write(response.content)
    print(name+" 下载完成")
