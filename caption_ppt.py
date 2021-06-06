from pptx import Presentation
import queue
from contents import *

hymn_file = hymn_path + "hymn_list.txt"
hymn_list = open(hymn_file, 'r')

hymn_queue = queue.Queue()

def createHymnList():
    # hymn_list.txt파일에서 찬송가 제목 끝에 '\n'이 포함되어 있음
    while True:
        hymn = hymn_list.readline()

        if( hymn.find(hymn_file1) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)
        if( hymn.find(hymn_file2) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)
        if( hymn.find(hymn_file3) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)
        if( hymn.find(hymn_file4) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)
        if( hymn.find(hymn_file5) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)
        if( hymn.find(hymn_file6) == 0):
            hymn = hymn.replace("\n", "")
            hymn_queue.put(hymn)

        if not hymn:
            break


def makeHymnString(hymn_str):
    length = len(hymn_str)

    if(hymn_str[0:2] == "00"):
        hymn_title = hymn_str[2:3] + "장 " + hymn_str[4:length]
    elif(hymn_str[0] == "0"):
        hymn_title = hymn_str[1:3] + "장 " + hymn_str[4:length]
    else:
        hymn_title = hymn_str[0:3] + "장 " + hymn_str[4:length]
    
    return hymn_title


createHymnList()
# print()
# print(makeHymnString(hymn_queue.get()))
# print(makeHymnString(hymn_queue.get()))
# print(makeHymnString(hymn_queue.get()))
# print(makeHymnString(hymn_queue.get()))


# 파일 열기
prs = Presentation('caption.pptx')


# Slide  1: 축복합니다. 환영합니다.

# Slide  2: 준비찬양 장

# Slide  3:  1. 묵도

# # Slide  4:  2. 찬송1
title_slide_layout = prs.slide_layouts[3]
slide = prs.slides[3]
subtitle = slide.placeholders[1]
subtitle.text = " (찬송) " + makeHymnString(hymn_queue.get())

# # Slide  5:  2. 찬송2
title_slide_layout = prs.slide_layouts[4]
slide = prs.slides[4]
subtitle = slide.placeholders[1]
subtitle.text = " (찬송) " + makeHymnString(hymn_queue.get())

# Slide  6:  3. 성시교독
# Slide  7:  4. 신앙고백
# Slide  8:  5. 찬송
# Slide  9:  6. 기도
# Slide 10:  7. 성경봉독
# Slide 11:  8. 찬송
# Slide 12:  9. 설교
# Slide 12: 10. 설교
# Slide 13: 11. 헌금
# Slide 14: 11. 헌금기도
# Slide 14: 12. 교회소식
# Slide 15: 13. 찬송
# Slide 17: 14. 축도
# Slide 18: 주님이 함께 하십니다.

prs.save('new-caption.pptx')



# while True:
#     if(hymn_queue.qsize() == 0):
#         break

#     print(hymn_queue.get())