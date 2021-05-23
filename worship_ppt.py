import os

import sys
import shutil


today_ppt_path = "E:\\OneDrive\\1. 예배\\예배 PPT\\2021\\21.05.24"

# 예배 PPT
ppt_origin_path = "E:\\OneDrive\\1. 예배\\예배 PPT\\ogrinal_ppt"
worship_ppt_file1 = "1. 주일낮예배.pptx"
worship_ppt_file2 = "1-1. 자막.pptx"
worship_ppt_file3 = "2. 주일오후예배.pptx"
worship_ppt_file4 = "2-1. 자막.pptx"

# 주보 찬송가들
hymn_ppt_path = "E:\\OneDrive\\1. 예배\\새 찬송가\\새찬송가"
hymn_file1 = "001.ppt"
hymn_file2 = "438.ppt"
hymn_file3 = "536.ppt"
hymn_file4 = "384.ppt"
hymn_file5 = "569.ppt"
hymn_file6 = "635.ppt"

#교도문
versicle_ppt_path = "E:\\OneDrive\\1. 예배\\새 찬송가\\새 교독문"
versicle_file = "095.pptx"


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)



# 예배 폴더 생성
createFolder(today_ppt_path)
target_ppt_path = today_ppt_path + "\\ppt"
createFolder(target_ppt_path)


# 예배 PPT 파일 생성
shutil.copy(ppt_origin_path + "\\" + worship_ppt_file1, today_ppt_path + "\\" + worship_ppt_file1)
shutil.copy(ppt_origin_path + "\\" + worship_ppt_file2, today_ppt_path + "\\" + worship_ppt_file2)
shutil.copy(ppt_origin_path + "\\" + worship_ppt_file3, today_ppt_path + "\\" + worship_ppt_file3)
shutil.copy(ppt_origin_path + "\\" + worship_ppt_file4, today_ppt_path + "\\" + worship_ppt_file4)


# 찬송가 파일 복사
shutil.copy(hymn_ppt_path + "\\" + hymn_file1, target_ppt_path + "\\" + hymn_file1)
shutil.copy(hymn_ppt_path + "\\" + hymn_file2, target_ppt_path + "\\" + hymn_file2)
shutil.copy(hymn_ppt_path + "\\" + hymn_file3, target_ppt_path + "\\" + hymn_file3)
shutil.copy(hymn_ppt_path + "\\" + hymn_file4, target_ppt_path + "\\" + hymn_file4)
shutil.copy(hymn_ppt_path + "\\" + hymn_file5, target_ppt_path + "\\" + hymn_file5)
shutil.copy(hymn_ppt_path + "\\" + hymn_file6, target_ppt_path + "\\" + hymn_file6)


# 교독문 파일 복사
shutil.copy(versicle_ppt_path + "\\" + versicle_file, target_ppt_path + "\\" + versicle_file)