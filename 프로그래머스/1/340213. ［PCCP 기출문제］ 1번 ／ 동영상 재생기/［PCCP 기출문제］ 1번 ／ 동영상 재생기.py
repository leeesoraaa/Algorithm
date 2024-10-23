from datetime import timedelta
import pandas as pd

# mm:ss 를 timedelta 형식으로 변환 함수
def mmss_to_td(mmss):
    td = {}
    for val, name in mmss:
        mm, ss = map(int, val.split(':'))
        td[name + '_td'] = timedelta(minutes=mm, seconds=ss)
    return td

# timedelta 를 mm:ss 형식으로 변환 함수
def td_to_mmss(pos_td):
    total_seconds = int(pos_td.total_seconds())
    mm, ss = divmod(total_seconds, 60)
    return f"{mm:02}:{ss:02}"

# 오프닝 건너뛰기 함수
def opening(td):
    if td['op_start_td'] <= td['pos_td'] <= td['op_end_td']:
        td['pos_td'] = td['op_end_td']
    return td

# 10초 건너뛰기 함수
def next(td):
    if (td['video_len_td'] - td['pos_td']) <= timedelta(seconds=10):
        td['pos_td'] = td['video_len_td']
    else:
        td['pos_td'] = td['pos_td'] + timedelta(seconds=10)
        opening(td)
    return td

# 10초 전 되돌리기 함수
def prev(td):
    if td['pos_td'] <= timedelta(seconds=10):
        td['pos_td'] = timedelta(seconds=0)
    else:
        td['pos_td'] = td['pos_td'] - timedelta(seconds=10)
        opening(td)
    return td

# main
def solution(video_len, pos, op_start, op_end, commands):
    mmss_list = [(video_len, "video_len"), (pos, "pos"),
                 (op_start, "op_start"),(op_end, "op_end")]
    td = mmss_to_td(mmss_list)
    for c in commands:
        opening(td)
        if c == "prev":
            td = prev(td)
        elif c == "next":
            td = next(td)

    answer = td_to_mmss(td['pos_td'])
    return answer