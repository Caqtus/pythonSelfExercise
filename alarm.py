import time
from datetime import datetime


def setAlarm():
    alarm_time = str(input(f'Enter time to set alarm. HH:MM:SS \n'))
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]


    print(f'input accepted. {alarm_time} \n')
    print(f'Setting alarm')

    while True:
        now = datetime.now()
        cur_hour = now.strftime("%H")
        cur_minute = now.strftime("%M")
        cur_seconds = now.strftime("%S")

        time_left_hh = int(alarm_hour) - int(cur_hour)

        time_left_mm = int(alarm_minute) - int(cur_minute)
        time_left_ss = int(alarm_seconds) - int(cur_seconds)


        if time_left_ss < 0:
            time_left_ss = 60 - int(-1 * time_left_ss)

        if time_left_mm < 0:
            time_left_mm = 60 - int(-1 * time_left_mm)

        if time_left_hh < 0:
            time_left_hh = 24 - int(-1 * time_left_hh)

        print('Time Left: {}:{}:{}'.format(str(time_left_hh).zfill(2), str(time_left_mm).zfill(2),
                                           str(time_left_ss).zfill(2)))
        time.sleep(1)

        # mainLoop
        if (alarm_hour == cur_hour):
            if (alarm_minute == cur_minute):
                if (alarm_seconds == cur_seconds):
                    print(f'WAKE UP')
                    break

