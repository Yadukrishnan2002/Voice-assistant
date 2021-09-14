import datefinder
import datetime
import winsound

def alm(cmd):
    dateandtime=datefinder.find_dates(cmd)
    for dandt in dateandtime:
        print(dandt)
    stringtime=str(dandt)
    timealone=stringtime[11:]
    print(timealone)

    hr=timealone[0:2]
    hr=int(hr)

    minu=timealone[3:5]
    minu=int(minu)

    sec=timealone[7:]
    sec=int(sec)

    print(hr,minu,sec)

    while True:
        current_hour=datetime.datetime.now().hour
        current_minute=datetime.datetime.now().minute
        if(hr==current_hour):
            if(minu==current_minute):
                print("Alarm is running")
                winsound.PlaySound('F://Projects//Virtual Assistant//alarm sound.mp3',winsound.SND_LOOP)
                #talk("Wake up.... It's time ")
            elif(current_minute>minu):
                print("Alarm is closing")
                break;



alm("set alarm at 5:31 pm")