import pymysql


conn = pymysql.connect(host='localhost', user='root', password='Root@123', db='pytest', port=3311)
cur = conn.cursor()

name=input("Enter the name:")
age=int(input("enter your age:"))
mobile=int(input("Enter 10 digit number:"))
cur.execute("""insert into student (name,age,mobile) values (%s,%s,%s)""",(name,age,mobile))
conn.commit()

n=input("enter y if you want to see the data:")
if n=='y':
 cur.execute("""select name,age,mobile from student where name=%s""",name)

 for r in cur:
    print(r)
cur.close()
conn.close()

