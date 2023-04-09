
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 

# マルチスレッド関係
import logging
import threading
import time

##PyAutoGUIのモジュール
import pyautogui

count = 0

def temp(GameAuto):
    counter = 0
    item_get_count = 10
    start = time.time()
    elapsed_time = -1
    
    while 1:
        eval_mode = True
        
        ###############################################
        # 自動化のコードだよ
        #
        GameAuto.serch_click_image2(img_path='C:\Users\cococ\OneDrive\デスクトップ\mac\GameAutomation-master - コピー\img\monst\quest.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)

        



