## 피지컬 컴퓨팅 연습 ##

import modi_plus as modi
import time as ti
 
bundle = modi.MODI()  # 모든 모듈 가져오기

try:
    while True:
        button = bundle.buttons[0]  # 버튼과 연결
        led = bundle.leds[0]    # LED와 연결

        if button.clicked:
            led.turn_on()  # LED 켜기
            ti.sleep(1)  # 1초 대기

            print("버튼을 클릭하여 LED를 켰습니다.")

        else:
            led.turn_off() # LED 끄기
            ti.sleep(1)  # 1초 대기

            print("버튼을 클릭하지 않아 LED를 껐습니다.")

        ti.sleep(0.1)  # 0.1초 대기

# 입력이 제대로 되지 않은 경우
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")