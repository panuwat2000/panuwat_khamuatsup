choose=[]#เลือกชนิดเครื่องดนตรี
z=[]#เก็บตัวแปรเครื่องดนตรี
n=[]#จำนวนเครื่องดนตรีที่จะยืม
t=[]#เก็บ z,n 
p=[]#เก็บ t
fdata = open('d:\\เครื่องดนตรีไทย.txt','r')
dataf = fdata.read()
f=dataf.split('.')

kdata = open('d:\\เครื่องดนตรีสากล.txt','r')
datak = kdata.read()
k=datak.split('.')

sdata = open('d:\\รายการที่เลือก.txt','a')

name=input('ชื่อ-สกุล-->')

while True:
    print('---------------------------')
    print('\nเครื่องดนตรีไทย[t]\nเครื่องดนตรีสากล[e]\nแสดงรายการ[s]\n')
    choose=input('เลือกชนิดเครื่องดนตรี->')
    choose=choose.lower()
    if choose=='t':
        print('------รายการเครื่องดนตรีไทย-------\n  ซอ[1]\n  ระนาด[2]\n  ขลุ่ย[3]\n  กรับ[4]\n  ฆ้อง[5]\n  จะเข้[6]\n  ขิม[7]\n  ออก[x]\n')
        while True:
            z=input('เลือกรายการ--->')
            n=input('จำนวน--->')
            if z=='1':
                t=('%s:%s'%(f[0],n))
                p.append(t)
            elif z=='2':
                t=('%s:%s'%(f[1],n))
                p.append(t)
            elif z=='3':
                t=('%s:%s'%(f[2],n))
                p.append(t)        
            elif z=='4':
                t=('%s:%s'%(f[3],n))
                p.append(t)
            elif z=='5':
                t=('%s:%s'%(f[4],n))
                p.append(t)
            elif z=='6':
                t=('%s:%s'%(f[5],n))
                p.append(t)
            elif z=='7':
                t=('%s:%s'%(f[6],n))
                p.append(t)
            elif z=='x' or n=='x':break
    elif choose=='e':
        print('------รายการเครื่องดนตรีสากล-------\n  กีตาร์[1]\n  ไวโอลิน[2]\n  แซ็กโซโฟน[3]\n  ฟลุท[4]\n  ทรัมเป็ท[5]\n  ทูบา[6]\n  กลอง[7]\n  ออก[x]\n')
        while True:

            z=input('เลือกรายการ--->')
            n=input('จำนวน--->')
            if z=='1':
                t=('%s:%s'%(k[0],n))
                p.append(t)
            elif z=='2':
                t=('%s:%s'%(k[1],n))
                p.append(t)
            elif z=='3':
                t=('%s:%s'%(k[2],n))
                p.append(t)        
            elif z=='4':
                t=('%s:%s'%(k[3],n))
                p.append(t)
            elif z=='5':
                t=('%s:%s'%(k[4],n))
                p.append(t)
            elif z=='6':
                t=('%s:%s'%(k[5],n))
                p.append(t)
            elif z=='7':
                t=('%s:%s'%(k[6],n))
                p.append(t)
            elif z=='x' or n=='x':break
    elif choose=='s':break
#------------------------วันที่ยืม------------------------------
from datetime import date
now=date.today().strftime('%d/%m/%Y')
#------------------------วันที่คืน------------------------------
day=now.split("/")
d=int(day[0])+7
m=int(day[1])
y=int(day[2])

if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d>31: #เดือนที่มี 31 วัน
    s=int(d-31)
    d=s
    m+=1 
elif m==12 and d>31 : #เดือนที่มี 31 วัน (เฉพาะเดือน 12)
    s=int(d-31)
    d=s
    m=1
elif (m==4 or m==6 or m==9 or m==11) and d>30: #เดือนที่มี 30 วัน
    s=int(d-30)
    d=s
    m+=1 
elif m==2 and (d>28 or d>29) : #เดือน 2
    s=int(d-28)
    d=s
    m+=1

fday=('%d/%d/%d'%(d,m,y))
#-------------------------เขียนลงไฟล์"รายการที่เลือก"--------------------------
sdata.write('ชื่อ-สกุล: %s\nวันที่ยืม: %s\nวันที่คืน: %s\n%s\n________________________________________________________________________________________________________________________________\n'%(name,now,fday,p))
#-------------------------แสดงรายการ---------------------------------
print('{0:*<40}'.format(""))
print('ชื่อ-สกุล: %s'%name)
print('วันที่ยืม: %s'%now)
print('วันที่คืน: %s'%fday)
print('{0:-<40}'.format(""))
print('{0:<12}{1:<10}{2:<10}'.format('ลำดับที่','รายการ','จำนวน'))
print('{0:-<40}'.format(""))

count=0
for x in p:
    count+=1
    print(count,end=")       ")
    b=x.split(":")
    print('{0[0]:<13}{0[1]:<6}'.format(b))
print('{0:*<40}'.format(""))
print('--------ขอบคุณค่ะ--------')