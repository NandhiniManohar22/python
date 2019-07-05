total_minutes=int(input())
hours=total_minutes//60
minutes=total_minutes%60
time="{} {}".format(hours,minutes)
print(time)
