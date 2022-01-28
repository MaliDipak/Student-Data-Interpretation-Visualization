import os
import cx_Oracle
import webbrowser
import time
import matplotlib.pyplot as plt
import itertools


def connectdatabase():
    fp = open("database.txt", 'r')
    if fp:
        c = fp.read()
        fp.close()
        return c
    else:
        print("File is not opened!")


def home():
    os.system("cls")
    print('''
 STUDENT DATA INTERPRETATION AND VISUALIZATION
    ...RC PATEL INSTITUTE OF TECHNOLOGY...
-----------------------------------------------
              [1]:Display Record
              [2]:Insert Record
              [3]:Visualize Data
              [4]:About College
              [5]:About Project
              [6]:Delete Record
              [7]:RESET
              [8]:EXIT
-----------------------------------------------''')
    ch = input('       Enter Your Choice : ')
    while(True):
        if ch == '':
            ch = 'n'
        ch = ord(ch[0])
        if(ch >= 49 and ch <= 56):
            return ch
        ch = input('      *Enter Your Choice : ')


def menu():
    os.system("cls")
    print('''
  R C Patel Institute of Technology, Shirpur
 --------------------------------------------
  Select The Branch..,
     [1]:Computer
     [2]:Data Science
     [3]:Electronics & Telecommunication
     [4]:Cevil
     [5]:Mechanical
     [6]:Electrical
     [7]:Go Back''')
    ch = input(" Enter Your Choice : ")
    n = ch
    while(True):
        if ch == '':
            ch = 'n'
        ch = ord(ch[0])
        if(ch >= 49 and ch <= 55):
            return int(n[0])
        ch = input("*Enter Your Choice : ")
        n = ch


def addrecord(c):
    oracleclassobject = cx_Oracle.connect(connectdatabase())
    os.system("cls")
    if oracleclassobject != None:
        branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']
        variable = oracleclassobject.cursor()
        print('R C PATEL INSTITUTE OF TECHNOLOGY SHIRPUR, DHULE')
        rn = input('\n Enter Roll Number            : ')
        while(rn == ''):
            rn = input('*Enter Roll Number            : ')
        record = 0
        q2 = f'SELECT * FROM {branch[c-1]}'
        variable.execute(q2)
        row = variable.fetchone()
        while row != None:
            if int(rn) == row[0]:
                record = 1
            row = variable.fetchone()
        if record == 1:
            print('''\nRoll Number' have unique constraints!, 
                    So the record is alreay exist...''')
        else:
            name = input(" Enter Student's Name         : ")
            prn = input(" Enter Student's PRN No.      : ")
            age = input(" Enter Student's Age          : ")
            gen = input(" Enter Student's Gender M/F   : ")
            dob = input(" Enter Student's Birth Date   : ")
            phn = input(" Enter Student's Phone Number : ")
            email = input(" Enter Student's E-mail Id    : ")
            add = input(" Enter Student's Address      : ")
            cgpa = float(input("Enter Student's CGPA          :"))
            if(prn == '' or age == ''):
                prn = 0
                age = 0
            q = f"INSERT INTO {branch[c-1]} VALUES({int(rn)}, '{name}', {int(prn)}, {int(age)}, '{gen}', '{dob}', '{phn}', '{email}', '{add}',{cgpa})"
            variable.execute(q)
            print('\nThe Record Is Updated Successfully!')
        oracleclassobject.commit()
        oracleclassobject.close()
    else:
        print("Failed")
    input("\nPRESS enter...")


def view():
    oracleclassobject = cx_Oracle.connect(connectdatabase())
    branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']
    c = menu()
    if c == 7:
        return
    else:
        vari = oracleclassobject.cursor()
        os.system("cls")
        print('''
  R C PATEL INSTITUTE OF TECHNOLOGY, SHIRPUR, DHULE
 ---------------------------------------------------
        [1]:Display records of all students
        [2]:Display record of single student
        [3]:Go Back''')

        n = input(" Enter Your Choice : ")
        counter1 = True
        while(counter1):
            if n == '':
                n = 'n'
            n = ord(n[0])
            if(n >= 49 and n <= 51):
                counter1 = False
            else:
                n = input("*Enter Your Choice : ")

        if n == 50:
            os.system("cls")
            print('''
 R C PATEL INSTITUTE OF TECHNOLOGY, SHIRPUR, DHULE
---------------------------------------------------''')
            rn = int(input("\nEnter Student's Roll Number  : "))
            record = 0
            q2 = f'SELECT * FROM {branch[c-1]} WHERE RN = {rn}'
            vari.execute(q2)
            row = vari.fetchone()
            if row != None:
                print("    # Student's Name         :", row[1])
                print("    # Student's PRN No.      :", row[2])
                print("    # Student's Age          :", row[3])
                print("    # Student's Gender M/F   :", row[4])
                print("    # Student's Birth Date   :", row[5])
                print("    # Student's Phone Number :", row[6])
                print("    # Student's E-mail Id    :", row[7])
                print("    # Student's Address      :", row[8])
                print(f"    # Student's CGPA         : {row[9]:.2f}")
                record = 1
            if record == 0:
                print('''\n  Record is not found, 
                    please check and try again!''')
        elif n == 49:
            os.system("cls")
            print('''
 R C PATEL INSTITUTE OF TECHNOLOGY, SHIRPUR, DHULE''')

            q2 = f'SELECT * FROM {branch[c-1]}'
            vari.execute(q2)
            row = vari.fetchall()
            print('-------------+------+------------------------------')
            print(" Roll Number | CGPA |  Student's Name")
            print('-------------+------+------------------------------')
            for i in range(len(row)):
                if row[i][0] < 10:
                    print(
                        f'     0{row[i][0]}      | {row[i][9]:.2f} |   {row[i][1]}')
                else:
                    print(
                        f'     {row[i][0]}      | {row[i][9]:.2f} |   {row[i][1]}')
            if len(row) == 0:
                print('\n               No Entries!')
        elif n == 51:
            return
            oracleclassobject.commit()
            oracleclassobject.close()
    oracleclassobject.commit()
    oracleclassobject.close()
    input("\nPRESS enter...")


def aboutclg():
    os.system("cls")
    print('''******************************************************************************************
                       STUDENT DATA INTERPRETATION AND VISUALIZATION
                        ...RC PATEL INSTITUTE OF TECHNOLOGY...''')
    print('''
    About RCPIT
        R. C. Patel Institute of Technology was set up as a part of the self-powered
    plans of Shirpur Education Society in 2001 with the objective to erect a truly 
    world class institute in the rural part where students from the vicinity would 
    be benefited from the services that matched global standards. RCPIT was conceived 
    by visionary leader, Hon. Shri. Amrishbhai R. Patel, former cabinet minister for 
    School Education, sports and Youth Welfare for Maharashtra State. The institute 
    has grown at a remarkable pace and has gone on to become an institute of repute 
    within the country. It is spread on lush green land providing an ambience congenial 
    to the pursuit of high quality technical education. 
        Every single detail of the institute has been implemented at par with global 
    standards in accordance to the norms of AICTE, New Delhi. The strength of RCPIT 
    lies in its state of art Laboratories, IIT virtual Classrooms & Laboratories, Digital 
    Library, and an advanced workshop.''')
    ch = input("\n# Visit Our Website (y/n): ")
    if(ch == 'y'):
        webbrowser.open_new_tab('https://www.rcpit.ac.in/')
    else:
        return


def reset():

    def database():
        fp = open("database.txt", 'w')
        if fp:
            print('''   -----------------------------------------------''')
            print("\n    To Connect with Database,")
            username = input("          *Enter User-name      : ")
            password = input("          *Enter Password       : ")
            database = input("          *Enter Database Name  : ")
            d = username + '/' + password + '@localhost' + '/' + database
            fp.write(d)
            fp.close()
        else:
            print("File is not opened!")

    def connectdatabase():
        fp = open("database.txt", 'r')
        if fp:
            c = fp.read()
            fp.close()
            return c
        else:
            print("File is not opened!")

    def checkTableExists(con, tablename):
        # This function is check whther table is exists or not
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM {}".format(tablename))
            return True
        except cx_Oracle.DatabaseError as e:
            x = e.args[0]
            if x.code == 942:  # Only catch ORA-00942: table or view does not exist error
                return False
            else:
                raise e
        finally:
            cur.close()

    def droptables(c):
        # This function is Drop all branch tables
        if c != None:
            cur = c.cursor()
            branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']
            for i in range(6):
                if checkTableExists(c, branch[i]):
                    q = f'DROP TABLE {branch[i]}'
                    cur.execute(q)
            c.commit()
            c.close()
        else:
            print(c)
            print('Failed...')

    def createtables(c):
        # This function create tables for all branches
        if c != None:
            cur = c.cursor()
            branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']
            #q2 = f'drop table {branch[i]}'
            for i in range(6):
                q = f'create table {branch[i]}(rn number primary key, name varchar(25), prn number, age number,gen varchar(1), dob varchar(11), phn varchar(10),email varchar(30), addr varchar(30), cgpa float)'
                cur.execute(q)
            c.commit()
            c.close()
        else:
            print(c)
            print('Failed...')

    loop = True
    os.system("cls")
    print('''
        STUDENT DATA INTERPRETATION AND VISUALIZATION
    -----------------------------------------------
            [1]:RESET
            [2]:Go Back
    -----------------------------------------------''')
    ch = input('      Enter you choice : ')
    if ch == "":
        ch = 'n'
    while(ch[0] != '1' and ch[0] != '2'):
        ch = input('     *Enter you choice : ')
        if ch == "":
            ch = 'n'
    if ch == '1':
        database()
        upi = connectdatabase()
        droptables(cx_Oracle.connect(upi))
        createtables(cx_Oracle.connect(upi))
        print("All RESET Successfully!:)")
        input('PRESS enter...')
        loop = False
    elif ch == '2':
        return


def aboutCommunity():
    os.system("cls")
    print('''**********************************************************************************************************
                                STUDENT DATA INTERPRETATION AND VISUALIZATION
                                ...RC PATEL INSTITUTE OF TECHNOLOGY...
                                            Semester Project-I''')
    print('''
        STUDENT DATA INTERPRETATION AND VISUALIZATION
            Schools and Universities are the foundation of knowledge and an educational 
        body on which students rely upon. Therefore, they need to maintain a proper 
        database of its students to keep all the updated records and easily share 
        information with students.
            Student data interpretation and visualization is a program which can be used to keep 
        track about the student activity like grades, performance, blood type, name, roll-no etc. The 
        student data interpretation and visualization(SDIV) is used for maintaining the records of the 
        students regarding the admission and examination part. This application is mainly designed for 
        maintaining the details of the student to help the colleges in maintaining their details with great 
        ease. 
            This will reduce the pen paper work in maintaining the details of the students of the college. 
        Through the use of this application, it will help to reduce this problem and information of any 
        student can be obtained just in one mouse click. It can be very useful to manage the records just 
        by single click we can access the data about a particular student. 
        This type of data interpretation is widely used in colleges to maintain the records and it can be 
        useful while dealing with large amount of data. Below is a list of tracking pieces you might have 
        on your information management system: 

            • Health information 
            • Gender 
            • Grades 
            • Name 
            • Age 
            • Roll-no 
            • And Many More 

        Keywords: Helps to keep track of student, reduces paper work, used data structure to store and 
        retrieve data with database management system. 

        This is simple Console based application that help in handling data.
        ''')
    input("\n\n# PRESS enter...")


def viz():
    os.system("cls")
    print('''******************************************************************************************
                       STUDENT DATA INTERPRETATION AND VISUALIZATION
                        ...RC PATEL INSTITUTE OF TECHNOLOGY...''')

    oracleclassobject = cx_Oracle.connect(connectdatabase())

    def Average(lst):
        arr = list(itertools.chain(*lst))
        n = len(arr)
        if n == 0:
            return (0)
        return sum(arr) / n

    if oracleclassobject != None:
        q = f"select cgpa from ds"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        ds = variable.fetchall()

        q = f"select cgpa from com"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        com = variable.fetchall()

        q = f"select cgpa from entc"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        entc = variable.fetchall()

        q = f"select cgpa from cevil"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        cevil = variable.fetchall()

        q = f"select cgpa from mech"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        mech = variable.fetchall()

        q = f"select cgpa from ele"
        variable = oracleclassobject.cursor()
        variable.execute(q)
        ele = variable.fetchall()

        oracleclassobject.commit()
        oracleclassobject.close()
    else:
        print("Failed")

    avgds = Average(ds)
    avgcom = Average(com)
    avgmech = Average(mech)
    avgcevil = Average(cevil)
    avgentc = Average(entc)
    avgele = Average(ele)

    x = ['COM', 'DS', 'MECH', 'CIVIL', 'E&TC', 'ELE']
    y = [avgcom, avgds, avgmech, avgcevil, avgentc, avgele]
    plt.xlabel('Engineering Branches')
    plt.ylabel('Progress')
    plt.title("Student's Progress Graph")
    plt.grid(color='violet', linestyle='dashdot', linewidth=0.5)
    plt.plot(x, y, linestyle='dashed', marker='o', markersize=9,
             markerfacecolor='white', markeredgecolor='black', color='red')
    plt.show()

    input("\n\n\t\t***Student's Progress Graph, press enter...")


def delrecord(c):
    oracleclassobject = cx_Oracle.connect(connectdatabase())
    branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']

    os.system("cls")
    print('R C PATEL INSTITUTE OF TECHNOLOGY SHIRPUR, DHULE')
    print('--------------------------------------------------')
    rn = int(input("\nEnter Student's Roll Number  : "))
    vari = oracleclassobject.cursor()
    record = 0
    q2 = f'SELECT * FROM {branch[c-1]} WHERE RN = {rn}'
    vari.execute(q2)
    row = vari.fetchone()
    if row != None:
        print("    # Student's Name         :", row[1])
        print("    # Student's PRN No.      :", row[2])
        print("    # Student's Age          :", row[3])
        print("    # Student's Gender M/F   :", row[4])
        print("    # Student's Birth Date   :", row[5])
        print("    # Student's Phone Number :", row[6])
        print("    # Student's E-mail Id    :", row[7])
        print("    # Student's Address      :", row[8])
        print(f"    # Student's CGPA         : {row[9]:.2f}")
        record = 1
        z = input(
            '\n\n*Are you sure you want to permanently delete this record?(y/n): ')
        if z[0] == 'y':
            q3 = f'DELETE FROM {branch[c-1]} WHERE RN = {rn}'
            vari.execute(q3)
            print('\nRecord is successfully deleted...,')
        else:
            print('\nRecord is not successfully deleted, try again...,')
    if record == 0:
        print('''\n  Record is not found, 
            please check and try again!''')
    oracleclassobject.commit()
    oracleclassobject.close()
    input("\nPRESS enter...")


if __name__ == "__main__":
    counter = True
    os.system("cls")
    while(counter):
        ch = home()
        if(ch == 50):
            b = menu()
            print(b)
            if b == 7:
                pass
            elif b >= 1 and b <= 6:
                addrecord(b)
        elif(ch == 54):
            b = menu()
            if b == 7:
                pass
            elif b >= 1 and b <= 6:
                delrecord(b)
        elif(ch == 55):
            reset()
        elif(ch == 49):
            view()
        elif(ch == 52):
            aboutclg()
        elif(ch == 53):
            aboutCommunity()
        elif(ch == 51):
            viz()
        elif(ch == 56):
            counter = False
    print('\nClosing the system.', end='')
    for i in range(30):
        print('.', end='')
        time.sleep(0.02)
