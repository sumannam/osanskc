from pptx import Presentation
from contents import *

# prs = Presentation('caption.pptx')
# title_slide_layout = prs.slide_layouts[0]
# slide = prs.slides[0]


#slide = prs.slides.add_slide(title_slide_layout)
# title = slide.shapes.title
# subtitle = slide.placeholders[1]

# title.text = "Hello,p World!"
# subtitle.text = "\n python-pptx was here!"

# prs.save('new-caption.pptx')

hymn_file = hymn_path + "hymn_list.txt"
hymn_list = open(hymn_file, 'r')


hymn_queue = []

# hymn_list.txt파일에서 찬송가 제목 끝에 '\n'이 포함되어 있음
while True:
    hymn = hymn_list.readline()

    if( hymn.find(hymn_file1) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)
    if( hymn.find(hymn_file2) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)
    if( hymn.find(hymn_file3) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)
    if( hymn.find(hymn_file4) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)
    if( hymn.find(hymn_file5) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)
    if( hymn.find(hymn_file6) == 0):
        hymn = hymn.replace("\n", "")
        hymn_queue.append(hymn)

    if not hymn:
        break

print(hymn_queue)