import os

import sys
import shutil

#주일 낮예배 순서 저장(content.py)
from contents import *




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

target_ppt_path = createTargetFolder()
copyFiles(target_ppt_path)

