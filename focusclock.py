import time
minutes=int(input("输入专注时间:"))
seconds=minutes*60
while seconds:
  mins,secs=divmod(seconds,60)
  timer='{:02d}:{:02d}'.format(mins,secs)
  print(timer,end="\r")
  time.sleep(1)
  seconds-=1
print("时间到！")
