import mysql.connector
import datetime

def getresult(REG_NO,DOB,YEAR):
    mydb = mysql.connector.connect(host="localhost",user="root",password="2002",database="result")
    mycursor = mydb.cursor()
    DOB=convert(DOB)
    sql="SELECT * FROM "+YEAR+'_year'+" WHERE Register_Number="+str(REG_NO)+" AND Dob="+"'"+DOB+"'"
    #print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for i in myresult:
        if i:
            myresult=i
    return list(myresult)

def getcolumn(YEAR):
    mydb = mysql.connector.connect(host="localhost",user="root",password="2002",database="result")
    mycursor = mydb.cursor()
    sql="SHOW COLUMNS FROM "+YEAR+'_year'   #print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycol=[]
    for i in myresult:
        mycol.append(i[0])
    return mycol
    #return sql



def convert(dob1):
    k=dob1.split('/')
    d1 = datetime.datetime(int(k[2]),int(k[1]),int(k[0]))
    return d1.strftime('X%d/X%m/%Y').replace('X0','X').replace('X','')

"""
year=1
result=getresult(101,'8/10/2002',str(year)+'_year')
column=getcolumn(str(year)+'_year')
print("-"*30)
for i in range(0,len(column)):
    print(column[i]," "*(15-len(str(column[i]))),result[i])
    print("-"*30)
"""
