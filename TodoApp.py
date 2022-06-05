from playsound import playsound
from gtts import gTTS
from datetime import datetime,date
from plyer import notification
import time


def usage():
    print(''' Usage:-
    $ todo ls                # Show remaining todos
    $ todo del NUMBER        # Delete a todo
    $ todo add 'todo item    # Add a new todo
    $ todo done NUMBER       # Complete a todo
    $ todo help              # Show Usage
    $ todo report            # Statistics 
    $ press q to quit and ok if you are done in your job ''')

def playaudio(audio):
    playsound(audio)

def ctoa(text) :
    audio= gTTS(text)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")

def main():

    print("enter 'q' to quit and 'ok' if you are done filling your works:")
    a=input(" -> Enter your request: ")
    b=[]
    top=0
    count=0
    today=date.today()
    d1=today.strftime("%d/%m/%Y")
    msg=''

    while(a!='q'):

        if a=='todo' or a=='help':
            usage()

        else:
            main=a.split()
            if  main[1]=='add':
                if main[0]=='todo':
                    for i in range(2,len(main)):
                        msg=msg+' '+main[i]    
                    b.append(msg)
                    del(main[2:])
                    print(f"Added todo : {msg}")
                    msg=''                   
                else:
                    print("Error : 'add' should be followed after 'todo' command ")
            elif main[1]=='done':
                if len(main)!=2:
                    if int(main[2])>len(b):
                        print(f"Marked {int(main[2])} as done")
                    elif main[2]==None:
                        print("Marked as done ")
                    else:
                        pos=int(main[2])
                        b.remove(b[pos-1])
                        print(f"Marked todo # {pos} as done ")
                        for i in range(pos,(len(b)-1)):
                            b[pos-1]=b[pos]    
                        count+=1
                else:
                    print("marked the todo as done")        

            elif main[1]=='ls':
                if len(b)==0:
                    print(" There are no remaining todos")
                else:
                    top=len(b)
                    for i in range(-1,-(top+1),-1):
                        print(f" [{top}]{b[i]} ")
                        top-=1
                
            elif main[1]=='del':
                if main[2]==None:
                    print(" del doesn't have enough arguements")
                elif int(main[2])>len(b):
                    print(f" deleted todo {int(main[2])}")
                else:
                    pos=int(main[2])
                    b.remove(b[pos-1])
                    print(f" Deleted todo #{pos}")
                    for i in range(pos,(len(b)-1)):
                        b[pos-1]=b[pos]
                    count+=1
                top=len(b)    
            elif main[1]=='report':
                if len(b)==0:
                    ctoa("your works has been finished!")
                    
                else:    
                    print(f"{d1} Pending: {len(b)} Completed : {count} ")
            else:
                usage()
        a=input( "-> Enter your request: ")   
        if a=='ok':
            return b

def combine(b):

    msg=''
    for i in b:
        msg=  msg +'\n' + i
    year=int(input("enter the year:"))
    mon=int(input("enter the month:"))
    day=int(input("enter the day:"))
    hrs=int(input("enter the hrs:"))
    minu=int(input("enter the min:"))
    dt1=datetime(year,mon,day,hrs,minu)
    a=1

    while a==1:
        if date.today() == dt1.date():
            if datetime.now().time() > dt1.time() :
                a=0
    else:
        try:
            ctoa("list of works you need to do!")
            notification.notify(
                title="List Of Works You Need To Do!",
                message=msg,
                timeout=30
            )

        except:
            notification.notify(
                title="List of works you Need to do!",
                message=msg,
                timeout=30
            )
                
    msg=''

if __name__ == "__main__" :

    b= main()
    combine(b)    