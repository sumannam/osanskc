import os

import sys
import shutil

hymn_path = "E:\\git\\osanskc\\"
today_ppt_path = "E:\\OneDrive\\1. 예배\\예배 PPT\\2021\\21.05.31"

# 예배 PPT
ppt_origin_path = "E:\\OneDrive\\1. 예배\\예배 PPT\\ogrinal_ppt"
worship_ppt_file1 = "1. 주일낮예배.pptx"
worship_ppt_file2 = "1-1. 자막.pptx"
worship_ppt_file3 = "2. 주일오후예배.pptx"
worship_ppt_file4 = "2-1. 자막.pptx"

# 주보 찬송가들
hymn_ppt_path = "E:\\OneDrive\\1. 예배\\새 찬송가\\새찬송가"
hymn_file1 = "001"
hymn_file2 = "438"
hymn_file3 = "536"
hymn_file4 = "384"
hymn_file5 = "569"
hymn_file6 = "635"

#교도문
versicle_ppt_path = "E:\\OneDrive\\1. 예배\\새 찬송가\\새 교독문"
versicle_file = "095"


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 예배 폴더 생성
def createTargetFolder():
    createFolder(today_ppt_path)
    target_ppt_path = today_ppt_path + "\\ppt"
    createFolder(target_ppt_path)
    return target_ppt_path


def copyFiles(target_ppt_path):
    # 예배 PPT 파일 생성
    shutil.copy(ppt_origin_path + "\\" + worship_ppt_file1, today_ppt_path + "\\" + worship_ppt_file1)
    shutil.copy(ppt_origin_path + "\\" + worship_ppt_file2, today_ppt_path + "\\" + worship_ppt_file2)
    shutil.copy(ppt_origin_path + "\\" + worship_ppt_file3, today_ppt_path + "\\" + worship_ppt_file3)
    shutil.copy(ppt_origin_path + "\\" + worship_ppt_file4, today_ppt_path + "\\" + worship_ppt_file4)

    hymn_file_ppt1 = hymn_file1 + ".ppt"
    hymn_file_ppt2 = hymn_file2 + ".ppt"
    hymn_file_ppt3 = hymn_file3 + ".ppt"
    hymn_file_ppt4 = hymn_file4 + ".ppt"
    hymn_file_ppt5 = hymn_file5 + ".ppt"
    hymn_file_ppt6 = hymn_file6 + ".ppt"

    # 찬송가 파일 복사
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt1, target_ppt_path + "\\" + hymn_file_ppt1)
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt2, target_ppt_path + "\\" + hymn_file_ppt2)
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt3, target_ppt_path + "\\" + hymn_file_ppt3)
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt4, target_ppt_path + "\\" + hymn_file_ppt4)
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt5, target_ppt_path + "\\" + hymn_file_ppt5)
    shutil.copy(hymn_ppt_path + "\\" + hymn_file_ppt6, target_ppt_path + "\\" + hymn_file_ppt6)

    # 교독문 파일 복사
    versicle_file_pptx = versicle_file + ".pptx"
    shutil.copy(versicle_ppt_path + "\\" + versicle_file_pptx, target_ppt_path + "\\" + versicle_file_pptx)

# target_ppt_path = createTargetFolder()
# copyFiles(target_ppt_path)

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