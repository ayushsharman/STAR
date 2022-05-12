import random
import tkinter
from tkinter import *
import datetime
from plyer.facades import notification
import pyttsx3
import os
import time
import subprocess
import webbrowser
import ctypes
from tkinter import _tkinter
import PIL as pillow
from PIL import Image
import plyer
from plyer import notification
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from time import sleep
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init()
root = Tk()

root.configure(bg="#26242f")
root.geometry('685x415')
root.resizable(FALSE, FALSE)
root.title("STAR")
star_logo = PhotoImage(file="star in black.png")
root.iconphoto(False, star_logo)

expression = ""
btn_state = False
file = None

global ques


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():

    if 'open file' in ques.get():
        speak("which file sir ")
        d = Toplevel(root)
        e = Entry(d, bg="black", fg="white", width=20)
        e.pack()

        def open_file():
            os.system(e.get())
            speak("ok sir i will open "+e.get())

        s = Button(d, bg="black", font=('arial', 18, 'bold'), fg="white", width=10,
                   activeforeground="grey", activebackground="black", text="open it", command=open_file).pack()

    elif 'shutdown' in ques.get():
        os.system("shutdown now -h")
        speak("ok sir i shutdown the computer")

    elif 'open stackoverflow' in ques.get():
        speak("ok sir i will open the stck over flow website")
        webbrowser.open("https://www.stackoverflow.com")

    elif 'open website' in ques.get():
        speak("which website sir ")
        d = Toplevel()
        e = Entry(d, bg="black", fg="white", font=(
            'arial', 18, 'bold'), width=20)
        e.pack()

        def open_web():
            webbrowser.open("https://"+e.get()+".com")
            speak("ok sir i will open "+e.get())
        s = Button(d, bg="black", fg="white", width=10, activeforeground="grey",
                   activebackground="black", text="open it", command=open_web).pack()

    elif 'open google' in ques.get():
        speak("ok sir i will open google.com")
        webbrowser.open("https://www.google.com")

    elif 'exit' in ques.get():
        exit()
        speak("good bye sir have a good day")

    elif 'quiet' in ques.get():
        speak("good bye sir have a good day")
        exit()

    elif 'hello' in ques.get():
        speak("Hey how you doing?")

    elif 'DT teacher' in ques.get():
        speak('Suniti Mam')

    else:
        speak("sorry sir i can not do this for now")


ques = Entry(root, width=20, bg="black",
             fg="white", font=('arial', 18, 'bold'))
ques.place(x=350, y=270)

submit = Button(text='Submit', fg='white', bg='#26242f',
                font=('arial', 10), command=command).place(x=450, y=307)


def info():
    speak('hello everyone i am star. student task accomplishment repository. i am created by group 2 using tkinter . i can perform certain tasks for you such as calculating numbers providing you a notepad and setting up notifications on your desktop, i can also open the websites mentioned below and if you want to open any other website just type in the text box given. you can also give me various commands through mic and i will respond acordingly. apart from that i can also shutdown your system and open your files if given the directory. now i have spoken enough and so i will let my team to ellaborate me more as else i will sound a narcissist. thank you ')


def speak_command():
    def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            speak("Recognizing...")
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            speak("Say that again please...")
            return "None"
        return query

    if __name__ == "__main__":
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)

            elif 'open youtube' in query:
                speak("ok sir opening the youtube.com")
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                speak("ok sir opening the google.com")
                webbrowser.open("https://www.google.com")

            elif 'open stackoverflow' in query:
                speak("ok sir opening the stackoverflow.com")
                webbrowser.open("https://www.stackoverflow.com")

            elif 'open BB' in query:
                speak("ok sir opening BB")
                webbrowser.open("https://cuchd.blackboard.com/ultra/course")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")

            elif 'hello' in query:
                speak("hello how are you")

            elif 'hi' in query:
                speak(
                    "hello how you doing try other amazing features of star voice assistant")

            elif 'teacher' in query:
                speak('suniti mam is your wonderful dt teacher')

            elif 'shut up' in query:
                speak('okay if thats what you want')

            elif 'what is your name' in query:
                speak('hello i am star by group 2')

            elif 'exit' in query:
                speak('okay sir exiting the STAR voice assistant have a nice day')
                exit()


mic_img = PhotoImage(file='mic.png')
mic_bg = Button(image=mic_img, command=speak_command).place(x=368, y=30)


def khtm():
    speak("Thanks for using STAR!")
    root.destroy()


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


def cuims():
    speak("ok sir i will open CUIMS")
    webbrowser.open("https://uims.cuchd.in/uims/frmAccountStudentDetails.aspx")


def bb():
    speak("ok sir i will open BB")
    webbrowser.open("https://cuchd.blackboard.com/ultra/course")


def youtube():
    speak("ok sir opening the youtube.com")
    webbrowser.open("https://www.youtube.com")


def spotify():
    speak("I see you wanna hear some music!")
    webbrowser.open("https://www.spotify.com/in-en/")


def switch():
    global btn_state
    if btn_state is True:
        # close NavBar
        for x in range(251):
            NavBar.place(x=-x, y=0)
            frame.update()
        frame.config(bg='black')
        # set button state off
        btn_state = False
    else:
        # Open NavBar
        for x in range(-250, 0):
            NavBar.place(x=x, y=0)
            frame.update()
        frame.config(bg='SystemButtonFace')
        # set button state ON
        btn_state = True


def calculator():
    speak("ok i am opening the calculator for you")

    def press(num):

        global expression
        expression = expression + str(num)
        equation.set(expression)

    def equalpress():
        try:

            global expression
            total = str(eval(expression))

            equation.set(total)
            expression = ""
        except:

            equation.set(" error ")
            expression = ""

    def clear():
        global expression
        expression = ""
        equation.set("")

    if __name__ == "__main__":

        Calculator = Toplevel(root)

        Calculator.configure(background="#26242f")

        Calculator.title("STAR Calculator")

        Calculator.geometry("270x150")

        equation = StringVar()

        expression_field = Entry(
            Calculator, bg='#26242f', fg='white', textvariable=equation)

        expression_field.grid(columnspan=4, ipadx=73)

        button1 = Button(Calculator, text=' 1 ', fg='white', bg='purple',
                         command=lambda: press(1), height=1, width=8)
        button1.grid(row=2, column=0)

        button2 = Button(Calculator, text=' 2 ', fg='white', bg='purple',
                         command=lambda: press(2), height=1, width=8)
        button2.grid(row=2, column=1)

        button3 = Button(Calculator, text=' 3 ', fg='white', bg='purple',
                         command=lambda: press(3), height=1, width=8)
        button3.grid(row=2, column=2)

        button4 = Button(Calculator, text=' 4 ', fg='white', bg='purple',
                         command=lambda: press(4), height=1, width=8)
        button4.grid(row=3, column=0)

        button5 = Button(Calculator, text=' 5 ', fg='white', bg='purple',
                         command=lambda: press(5), height=1, width=8)
        button5.grid(row=3, column=1)

        button6 = Button(Calculator, text=' 6 ', fg='white', bg='purple',
                         command=lambda: press(6), height=1, width=8)
        button6.grid(row=3, column=2)

        button7 = Button(Calculator, text=' 7 ', fg='white', bg='purple',
                         command=lambda: press(7), height=1, width=8)
        button7.grid(row=4, column=0)

        button8 = Button(Calculator, text=' 8 ', fg='white', bg='purple',
                         command=lambda: press(8), height=1, width=8)
        button8.grid(row=4, column=1)

        button9 = Button(Calculator, text=' 9 ', fg='white', bg='purple',
                         command=lambda: press(9), height=1, width=8)
        button9.grid(row=4, column=2)

        button0 = Button(Calculator, text=' 0 ', fg='white', bg='gray22',
                         command=lambda: press(0), height=1, width=8)
        button0.grid(row=5, column=0)

        plus = Button(Calculator, text=' + ', fg='white', bg='gray22',
                      command=lambda: press("+"), height=1, width=8)
        plus.grid(row=2, column=3)

        minus = Button(Calculator, text=' - ', fg='white', bg='gray22',
                       command=lambda: press("-"), height=1, width=8)
        minus.grid(row=3, column=3)

        multiply = Button(Calculator, text=' * ', fg='white', bg='gray22',
                          command=lambda: press("*"), height=1, width=8)
        multiply.grid(row=4, column=3)

        divide = Button(Calculator, text=' / ', fg='white', bg='gray22',
                        command=lambda: press("/"), height=1, width=8)
        divide.grid(row=5, column=3)

        equal = Button(Calculator, text=' = ', fg='white', bg='gray22',
                       command=equalpress, height=1, width=8)
        equal.grid(row=5, column=2)

        clear = Button(Calculator, text='Clear', fg='white', bg='gray22',
                       command=clear, height=1, width=8)
        clear.grid(row=5, column='1')

        Decimal = Button(Calculator, text='.', fg='white', bg='gray22',
                         command=lambda: press('.'), height=1, width=8)
        Decimal.grid(row=6, column=2)

        Calculator.mainloop()


def notepad():
    speak("just a second and your notepad will be opened")

    def newFile():
        global file
        notepad.title("Untitled - Notepad")
        TextArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            notepad.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                notepad.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def quitApp():
        speak('thanks for using our notepad')
        notepad.destroy()

    def cut():
        TextArea.event_generate(("<>"))

    def copy():
        TextArea.event_generate(("<>"))

    def paste():
        TextArea.event_generate(("<>"))

    def about():
        showinfo("Notepad", "Notepad by STAR")

    if __name__ == '__main__':
        notepad = Toplevel(root)
        notepad.title("Untitled - Notepad")
        notepad.wm_iconbitmap("star in black.png")
        notepad.geometry("685x400")

        TextArea = Text(notepad, fg='white', font="arial 13", bg='#26242f')
        file = None
        TextArea.pack(expand=True, fill=BOTH)

        MenuBar = Menu(notepad)

        FileMenu = Menu(MenuBar, tearoff=0)

        FileMenu.add_command(label="New", command=newFile)

        FileMenu.add_command(label="Open", command=openFile)

        FileMenu.add_command(label="Save", command=saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)

        EditMenu = Menu(MenuBar, tearoff=0)

        EditMenu.add_command(label="Cut", command=cut)
        EditMenu.add_command(label="Copy", command=copy)
        EditMenu.add_command(label="Paste", command=paste)

        MenuBar.add_cascade(label="Edit", menu=EditMenu)

        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)

        notepad.config(menu=MenuBar)

        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)

        notepad.mainloop()


def notifier():
    speak("okay i am opening notifier make sure to input the time in seconds")
    desktop_notifier = Toplevel(root)
    desktop_notifier.title("Desktop Notifier")
    desktop_notifier.geometry("350x250")
    desktop_notifier.resizable(False, False)
    desktop_notifier.config(background='#26242f')

    Time_val = Label(desktop_notifier, text="TIME", font='Helvetica 20 bold',
                     bg='#26242f', fg='white').place(x=10, y=20)
    Notification = Label(desktop_notifier, text="MESSAGE", font='Helvetica 20 bold',
                         bg='#26242f', fg='white').place(x=10, y=80)
    Remarks = Label(desktop_notifier, text="REMARKS", font='Helvetica 20 bold',
                    bg='#26242f', fg='white').place(x=10, y=140)

    timevalue = IntVar()
    Notificationvalue = StringVar()
    Remarksvalue = StringVar()

    timeentry = Entry(desktop_notifier, textvariable=timevalue,
                      width=20, font='arial 10').place(x=170, y=30)
    Notificationentry = Entry(
        desktop_notifier, textvariable=Notificationvalue, width=20, font='arial 10').place(x=170, y=90)
    Remarksentry = Entry(
        desktop_notifier, textvariable=Remarksvalue, width=20, font='arial 10').place(x=170, y=150)

    def getvalue():
        speak('the notification is set now you need to close the window')
        desktop_notifier.destroy()

    quit = Button(desktop_notifier, text='Submit', font='poppins 15 bold', bg='purple', fg='white',
                  command=getvalue).place(x=130, y=200)

    desktop_notifier.mainloop()

    if __name__ == '__main__':
        while True:
            notification.notify(
                title=f"{Notificationvalue.get()}",
                message=f"{Remarksvalue.get()}",
                app_icon="star in black.ico",
                timeout=5
            )
            time.sleep(timevalue.get())


frame = Frame(root, bg='black')
frame.pack(side='top', fill='x')

navbar_icon = PhotoImage(file='nav.png')
navbar_btn = Button(frame, image=navbar_icon, bd=2, command=switch)
navbar_btn.grid(row=1, column=1)

NavBar = Frame(root, bg='black', height=1000, width=250)
NavBar.place(x=-250, y=0)


o1 = Button(NavBar, text='CALCULATOR', font='poppins 18 bold', bg='black', fg='white', activebackground='gray',
            activeforeground='white', bd=0, command=calculator).place(x=25, y=60)
o2 = Button(NavBar, text='NOTEPAD', font='poppins 18 bold', bg='black', fg='white', activebackground='gray',
            activeforeground='white', bd=0, command=notepad).place(x=25, y=120)
o3 = Button(NavBar, text='NOTIFIER', font='poppins 18 bold', bg='black', fg='white', activebackground='gray',
            activeforeground='white', bd=0, command=notifier).place(x=25, y=180)
o4 = Button(NavBar, text='EXIT', font='poppins 18 bold', bg='black', fg='white', activebackground='gray',
            activeforeground='white', bd=0, command=khtm).place(x=25, y=240)
close_icon = PhotoImage(file='cross.png')
close_btn = Button(NavBar, image=close_icon, bd=1, command=switch)
close_btn.place(x=180, y=5)


f2 = Frame(bg="black", borderwidth=3)
b1_label = Button(f2, text="CUIMS", bg="#9940bf", fg="white",
                  font="poppins 19 bold", relief="solid", command=cuims)
b1_label.pack(anchor="ne", side="left", fill="x")

b2_label = Button(f2, text="BLACKBOARD", bg="#9940bf", fg="white",
                  font="poppins 19 bold", relief="solid", command=bb)
b2_label.pack(anchor="ne", side="left", fill="x")

b3_label = Button(f2, text="YOUTUBE", bg="#9940bf", fg="white",
                  font="poppins 19 bold", relief="solid", command=youtube)
b3_label.pack(anchor="ne", side="left", fill="x")

b4_label = Button(f2, text="SPOTIFY", bg="#9940bf", fg="white",
                  font="poppins 19 bold", relief="solid", command=spotify)
b4_label.pack(anchor="ne", side="left", fill="x")

f2.pack(side="bottom", anchor="nw", fill="x")

clock = Label(f2, text="click me 4!", bg="#9940bf", fg="white",
              font="poppins 19 bold", relief="solid")
clock.pack(anchor="nw", side="left", fill="both")


Menu_bar = Menu(root)
Help_Menu = Menu(Menu_bar, tearoff=0)
Help_Menu.add_command(label="About STAR", command=info)
Menu_bar.add_cascade(label="STAR Info", font='poppins', menu=Help_Menu)

root.config(menu=Menu_bar)

tick()


root.mainloop()
