import os
import stdiomask
from tabulate import tabulate as t
import mysql.connector as s
def clear():
    abcd=os.system('cls')
    return abcd

a=s.connect(user="root",password="vivek")
c=a.cursor()
c.execute('''create database if not exists cricket''')
c.execute('''use cricket''')
c.execute('''create table if not exists batsman
(Player_ID varchar(20),
 Name varchar(20),
 Jersey_no varchar(20),
 Batting_type varchar(20),
 No_of_innings_batted varchar(20),
 Runs varchar(20),
 Best_score varchar(20),
 50s varchar(20),
 100s varchar(20));''')
c.execute('''create table if not exists bowler
(Player_ID varchar(20),
 Name varchar(20),
 Jersey_no varchar(20),
 Bowling_type varchar(50),
 No_of_innings_bowled varchar(20),
 Wickets varchar(20),
 Best_spell varchar(20),
 No_of_5fer varchar(20));''')

def about():
    print('''
            STARS XI CRICKET CLUB (SCC)
                       Since 2000
    Founder : Krishnamachari Srikkanth (Former Indian Cricketer) 
    Head Coach : Krishnamachari Srikkanth (Former Indian Cricketer)
    Coaches:
        V. B. Chandrasekhar (FIC)
        Lakshman Sivaramakrishnan (FIC)
        Hemang Badani  (FIC)
        Subramanian Badrinath (FIC)
        Lakshmipathy Balaji (FIC)
        
    Trophies won
    Ranji Trophy : 2
    Vijay Hazare Trophy : 5
    Syed Mushtaq Ali Trophy : 1
    Irani Trophy : 1
    
    Players went to indian cricket team from Stars XI :
        Abhinav Mukund (2011)
        Ravichandran Ashwin (2011)
        Vijay Shankar (2019)
        Washington Sundar (2021)
        T Natarajan (2021)  ''')
    x=input()

def insert():
    b=input("Enter table to which values to be inserted (batsman/bowler):")
    if b.lower()=="batsman":
        zx=input("Enter Player ID:")
        d=input("Enter name of batsman:")
        e=input("Enter jersey no:")
        f=input("Enter batting type:")
        g=input("Enter no of innings batted:")
        h=input("Enter runs:")
        i=input("Enter best score:")
        j=input("Enter 50s:")
        k=input("Enter 100s:")
        c.execute('''insert into batsman values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(zx,d,e,f,g,h,i,j,k))
    if b.lower()=="bowler":
        zx=input("Enter Player ID:")
        d=input("Enter name of bowler:")
        e=input("Enter jersey no:")
        f=input("Enter bowling type:")
        g=input("Enter no of innings bowled:")
        h=input("Enter wickets:")
        j=input("Enter best spell:")
        k=input("Enter no of 5fer:")
        c.execute('''insert into bowler values (%s,%s,%s,%s,%s,%s,%s,%s)''',(zx,d,e,f,g,h,j,k))
    print("Player successfully added in the club")
    x=input()
    a.commit()

def display():
    l=input("Enter table to be displayed (batsman/bowler):")
    c.execute("select * from "+l)
    row=c.fetchall()
    if l.lower()=="batsman":
        an=["Player_ID","Name","Jersey_no","Batting_type","No_of_innings_batted","Runs","Best_score","50s","100s"]
        ac=[r for r in row]
        print(t(ac,an,tablefmt="grid"))
    elif l.lower()=="bowler":
        an=["Player_ID","Name","Jersey_no","Bowling_type","No_of_innings_bowled","Wickets","Best_spell","No_of_5fer"]
        ac=[r for r in row]
        print(t(ac,an,tablefmt="grid"))
    x=input()
             
def update():
    p=input("Enter table to be updated (batsman/bowler):")
    if p.lower()=='batsman':
              z=input("Enter Player_ID of player whose details to be updated:")
              q=input("Enter runs scored:" )
              c.execute('''select * from batsman;''')
              row=c.fetchall()
              c.execute('''update batsman set no_of_innings_batted=no_of_innings_batted+1 where name=(%s)''',(z,))
              if q[-1] == '*':
                     c.execute('''update batsman set runs=runs+(%s) where player_id=(%s)''',(int(q[:-1]),z))
              else:
                     c.execute('''update batsman set runs=runs+(%s) where player_id=(%s)''',(int(q),z))
              for r in row:
                  if r[0]==z:
                      if int(q[:q.find("*")])>int(r[6][:r[6].find("*")]):
                          c.execute('''update batsman set best_score=(%s) where player_id=(%s)''',(q,z))
                      if int(q[:q.find("*")])==int(r[6][:r[6].find("*")]):
                          if len(str(q))>len(str(r[6])):
                                             c.execute('''update batsman set best_score=(%s) where player_id=(%s)''',(q,z))                
                      if int(q[:q.find("*")])>=50 and int(q[:q.find("*")])<100:
                          c.execute('''update batsman set 50s=50s+1 where player_id=(%s)''',(z,))
                      if int(q[:q.find("*")])>=100:
                          c.execute('''update batsman set 100s=100s+1 where player_id=(%s)''',(z,))
    if p.lower()=='bowler':
              z=input("Enter Player_ID of player whose details to be updated:")
              q=input("Enter bowling spell:")
              c.execute('''select * from bowler;''')
              row=c.fetchall()
              c.execute('''update bowler set no_of_innings_bowled=no_of_innings_bowled+1 where player_id=(%s)''',(z,))
              c.execute('''update bowler set wickets=wickets+(%s) where player_id=(%s)''',(int(q[0]),z))
              for r in row:
                     if r[0]==z:
                            if int(q[0])>int(r[6][:1]):
                                   c.execute('''update bowler set best_spell=(%s) where player_id=(%s)''',(q,z))
                            if int(q[0])==int(r[6][:1]):
                                    if int(q[2:])<int(r[6][2:]):
                                            c.execute('''update bowler set best_spell=(%s) where player_id=(%s)''',(q,z))
                            if int(q[0])>=5:
                                            c.execute('''update bowler set No_of_5fer=No_of_5fer+1 where player_id=(%s)''',(z,))
    print("Player details successfully updated")
    x=input()
    a.commit()

def allrounder():
    c.execute('''select b.player_id,b.name,b.jersey_no,b.runs,b.best_score,b.50s,b.100s,d.wickets,d.best_spell,d.No_of_5fer from batsman b,bowler d where b.player_id=d.player_id;''')
    row=c.fetchall()
    an=["Player_ID","Name","Jersey_no","Runs","Best score","50s","100s","Wickets","Best_spell","No_of_5fer"]
    ac=[r for r in row]
    print(t(ac,an,tablefmt="grid"))
    x=input()

def best():
    L=[]
    l=[]
    q=['batsman','bowler']
    for x in q:
        c.execute('''select * from '''+x+''';''')
        d=c.fetchall()
        for r in d:
            z=(int(r[5]))/(int(r[4]))
            L.append(z)
        a=max(L)
        e=L.index(a)
        print("The best " +x+ " is:",d[e][0],d[e][1])
    x=input()
   
def delete():
    p=input("enter row of which table to be deleted:")
    z=input("enter Player_ID of player whose details to be deleted:")
    if p=='batsman':
        c.execute("delete from batsman where player_id = (%s);",(z,))
    if p=='bowler':
        c.execute("delete from bowler where Player_id = (%s);",(z,))
    print("Player successfully deleted from the club")
    x=input()
    a.commit()

def search():
    z=input("Enter name of the table(batsman/bowler):")
    b=input("Enter Player_ID of player to be searched :")
    if z.lower()=='batsman': 
        c.execute('''select * from batsman where Player_ID=(%s);''',(b,))
        row=c.fetchall()
        an=["Player_ID","Name","Jersey_no","Batting_type","No_of_innings_batted","Runs","Best_score","50s","100s"]
        ac=[r for r in row]
        print(t(ac,an,tablefmt="grid"))
    if z.lower()=='bowler': 
        c.execute('''select * from bowler where Name=(%s);''',(b,))
        row=c.fetchall()
        an=["Player_ID","Name","Jersey_no","Bowling_type","No_of_innings_bowled","Wickets","Best_spell","No_of_5fer"]
        ac=[r for r in row]
        print(ac,an,tablefmt="grid")
    x=input()

admin={"Naveen":"12223","Rakesh":"12224","Ronak":"12225"}      
while True:
    clear()
    print('''  MAIN MENU
            1. Login as admin
            2. View records
            3. Exit''')
    w=int(input("Enter choice:"))
    if w==1:
           o=input("Enter the username:")
           j=stdiomask.getpass("Enter the password:")
           if not((o,j) in admin.items()):
                  print("Invalid username & password")
           if (o,j) in admin.items():
              while True:
                  clear()
                  print('''
                                  MENU
                  1.About Stars XI Cricket Club (SCC)
                  2.Insert
                  3.Display
                  4.Update
                  5.Display all rounder
                  6.Display best batsman and bowler
                  7.Search player
                  8.Delete
                  9.Exit''')
                  ch=int(input("Enter choice:"))
                  if ch==1:
                      about()
                  elif ch==2:
                      insert()
                  elif ch==3:
                      display()
                  elif ch==4:
                      update()
                  elif ch==5:
                      allrounder()
                  elif ch==6:
                      best()
                  elif ch==7:
                      search()
                  elif ch==8:
                      delete()
                  elif ch==9:
                      break
                  else:
                      print("Invalid input")
    if w==2:
        while True:
            clear()
            print('''
                                 MENU
              1.About Stars XI Cricket Club (SCC)
              2.Display
              3.Display all rounder
              4.Display best batsman and bowler
              5.Search player
              6.Exit''')
            ch=int(input("Enter choice:"))
            if ch==1:
                about()
            elif ch==2:
                display()
            elif ch==3:
                allrounder()
            elif ch==4:
                best()
            elif ch==5:
                  search()
            elif ch==6:
                break
            else:
                print("Invalid input")
    if w==3:
        break