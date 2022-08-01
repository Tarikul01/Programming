for _ in range(int(input())):
    alrmCount,hour,minute=list(map(int,input().split()))
    arr=[]
    bedTime=hour*60+minute
    setAlarm=9999999999
    for _ in range(alrmCount):
        a,b=list(map(int,input().split()))
        alarm=a*60+b
        if(alarm>=bedTime):
            setAlarm=min(alarm-bedTime,setAlarm)
        else:
            setAlarm=min(((24*60)-bedTime)+alarm,setAlarm)

    # if(bedTime<=setAlarm):
    #     sleptime = setAlarm - bedTime
    # else:
        # sleptime=((24*60)-bedTime)+setAlarm
       # sleptime=setAlarm
    print(setAlarm//60,setAlarm%60)


