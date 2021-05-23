import webbrowser
import os
import subprocess
import pyautogui
import pygetwindow as gw
import time
import mouse  

# while True:
#     if mouse.is_pressed("left"):             # 마우스 왼쪽 클릭이면
#         click += 1                             # 클릭 숫자 증가
#         print('Left-Clicked: ' + str(click))   # 메시지 출력
#         pos = mouse.get_position()       # 현재 마우스 포인터 좌표
#         print(pos)                                  
#     time.sleep(0.05)  


# 2021년 5월 16일 수요예배 
#chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
youtube_live_url = "https://studio.youtube.com/video/Q6wkIP8xXyE/livestreaming"


obs_command = 'start /d "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"'
os.system(obs_command)

#webbrowser.open_new(youtube_live_url)
# os.chdir(chrome_path)
# chrome_command = "chrome " + youtube_live_url
# os.system(chrome_command)


#time.sleep(2)
#chrome_window = gw.getWindowsWithTitle('chrome')[0]
#print(chrome_window.size)

# chrome_window.resize(974, 1047)
# chrome_window.top = 0
# chrome_window.left = 0


#chrome_window.moveTo(0,0)

# time.sleep(1)
# os.system(obs_path)

# obs_window = gw.getWindowsWithTitle('obs')[0]
# obs_window.resize(974, 1047)
# obs_window.moveTo(953,0)

# time.sleep(2)

#pyautogui.click(x=10, y=25, button='left')
 

#subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\notepad.exe"])

#pyautogui.click(x=10, y=25, button='left')
#https://pygetwindow.readthedocs.io/en/latest/

