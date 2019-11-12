import re
import time

update_time = time.time()
data_list = []


def refresh_console(start):
    global update_time
    global data_list
    if time.time()-update_time < 0.5:
        return
    update_time = time.time()
    i = 0
    # print(data_list)

    while i < len(data_list):
        # 只更新未曾打印过的lyrics
        if (data_list[i][0] <= start) and (data_list[i][2] == 0):
            data_list[i][2] = 1
            print(data_list[i][1])
        i += 1


# match the minute and second and lyrics text
def match_time(txt, start):
    p = re.compile("\[([\d]{1,2}):([\d]{1,2})[.\d]{1,}\](.*\n)")
    # print("更新歌词库:")
    match_list = p.findall(txt)
    global data_list
    data_list.clear()
    for el in match_list:
        data_list.append([int(el[0]) * 60 + int(el[1]), el[2], 0])
    refresh_console(0)
