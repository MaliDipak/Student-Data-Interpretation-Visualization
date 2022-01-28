# This Program to insert Random Data in all six tables
import cx_Oracle
import random


def connectdatabase():
    fp = open("database.txt", 'r')
    if fp:
        c = fp.read()
        fp.close()
        return c
    else:
        print("File is not opened!")


firstname = ['Dipak', 'Atharv', 'Bhupendra',  'Rohit', 'Saurabh', 'Jayesh', 'Shivam', 'Kalpesh',
             'Atul',  'Yash', 'Ashwini', 'Rina', 'Anuja', 'Diksha', 'Khushi', 'Neha', 'Sarika', 'Puja']

g = ['Ashwini', 'Rina', 'Anuja', 'Diksha', 'Khushi', 'Neha', 'Sarika', 'Puja']

lastname = ['Mali', 'Mahajan', 'Patil', 'Garud', 'Salunke', 'Yogi', 'Koli', 'Thakur', 'Magare',
            'Nikam', 'Hire', 'Wakade', 'Tawade', 'Deshmukh', 'More', 'Lokhande', 'Chauhan', 'Mahale']

a = [18, 19, 20, 21]

address = ['Chopda', 'Jalgaon', 'Dhule', 'Nundurbar', 'Shirpur', 'Chalisgaon']

c = cx_Oracle.connect(connectdatabase())
if c != None:
    print("Connected")
    cur = c.cursor()
    branch = ['com', 'ds', 'entc', 'cevil', 'mech', 'ele']
    for j in range(6):
        for i in range(1, 51):
            rn = i
            name = random.choice(firstname)+' '+random.choice(lastname)
            prn = 20110603+i
            age = random.choice(a)
            if name.split()[0] in g:
                gen = 'F'
            else:
                gen = 'M'
            d = random.randint(1, 28)
            m = random.randint(1, 12)
            y = 2021-age
            dob = f'{str(d)}/{str(m)}/{str(y)}'
            phn = '80555*****'
            email = f'{name.split()[0]}{str(rn)}@gmail.com'
            add = random.choice(address)
            cgpa = random.uniform(2.5, 10.0)
            q = f"INSERT INTO {branch[j]} VALUES({int(rn)}, '{name}', {int(prn)}, {int(age)}, '{gen}', '{dob}', '{phn}', '{email}', '{add}',{cgpa})"
            cur.execute(q)
    c.commit()
    c.close()
else:
    print(c)
    print('Failed...')
print('Random data of 50 students has been added for each branch :)')