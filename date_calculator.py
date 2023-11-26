def isleap (x):
    return (x%4==0 and x%100!=0 or x%400==0)

def dopp(): 
    leap_list=[31,29,31,30,31,30,31,31,30,31,30,31]

    not_leap_list=[31,28,31,30,31,30,31,31,30,31,30,31]

    m_index=mm-1
    m_bf=m_index-1
    d_bf=0
    d_af=0

    if m_bf>0:
        if isleap (yy):
            i=0
            while i <= m_bf:
                d_bf+=leap_list[i]
                i+=1
        else:
            i=0
            while i <= m_bf:
                d_bf+=not_leap_list[i]
                i+=1 
    if isleap(yy1):
        i=mm1
        mo=leap_list[i-1]
        while i<= 11:
            d_af+=leap_list[i]
            i+=1
    else:
        i=mm1
        mo=not_leap_list[i-1]
        while i <= 11:
            d_af+=not_leap_list[i]
            i+=1
    dd2=mo-(dd1-1)
    d3=dd-1
    day_chop=d_bf+d_af+d3+dd2
    
    j=yy
    sum_year=0
    while j <= yy1:
        if isleap(j):
            sum_year+=366
        else:
            sum_year+=365
        j+=1
    total_days=sum_year-day_chop
    return(total_days)

dob =input("dob in ddmmyyyy format: ")
dd = int(dob[:2])
mm = int(dob[2:4])
yy= int(dob[4:])

tod= input("today's date in ddmmyyyy format: ")
dd1 = int(tod[:2])
mm1 = int(tod[2:4])
yy1= int(tod[4:])

print("days since birthday",dopp())


