import keyboard, win32api, time

while True:
    time.sleep(0.1)
    #if keyboard.is_pressed("w") : print("w가 눌림")
    if win32api.GetKeyState(0x01) < 0 :print("마우스왼쪽 클릭") # 마우스왼쪽 버튼
    if win32api.GetKeyState(0x02) < 0 :print("마우스오른쪽 클릭") # 마우스오른쪽 버튼

