
import autobday as ab
import tkinter as tk
import webbrowser as web

class Application(tk.Frame):



    def __init__(self, master=None, birthdays=None):
        super().__init__(master)
        self.master = master
        self.pack()

        if birthdays == None:
            self.nobday()
        else:
            web.open('')
            self.bday(birthdays)



    def nobday(self):

        self.label = tk.Label(self)
        self.label["text"] = "There are no birthdays today!"
        self.label.pack(side="top", pady=4,padx=10)

        self.quit = tk.Button(self, text="Close", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom",padx=10,pady=4)

    def bday(self,birthdays):
        n = len(birthdays)
#Label to say what is happenning.
        self.toplabel = tk.Label(self)
        self.toplabel['text'] = 'Birthdays Today:'
        self.toplabel.grid(row=1,column=1,padx=10,pady=4)
#Code to list names in labels.
        for i in range(n):
            tk.Label(self, text=birthdays[i]).grid(row=i+1,column=2,columnspan=2,padx=10,pady=4)
#Label asking to send msgs.
        self.bottomlabel = tk.Label(self)
        self.bottomlabel['text'] = 'Send Messages?'
        self.bottomlabel.grid(row = n+1, column=1)
#Button that sends msgs.
        self.ok = tk.Button(self,fg='green',command=self.updater)
        self.ok['text'] = 'Yes'
        self.ok.grid(row=n+1,column=2,padx=10,pady=4)

#Button that does not send msgs.
        self.no = tk.Button(self,fg='red',command=self.master.destroy)
        self.no['text']='Close'
        self.no.grid(row=n+1,column=3,padx=10,pady=4)


    def confirms(self,ticks):


        for i in range(ticks):
            tk.Label(self,text='sent',fg='green').grid(row=i+1,column=4,padx=10,pady=4)




    def updater(self):
        date = ab.today()
        collection = ab.birthdaycheck(date)  # Gathering tuple of birthday dates
        c = 0

        if collection != []:
            for birthday in collection:

                if birthday[2] == '' and birthday[4] == '0':
                    ab.sendmsg(birthday[1])
                elif birthday[2] != '' and birthday[4] == '0':
                    ab.sendmsg(birthday[1], msg=birthday[2])
                c += 1

            self.confirms(c)

            indeces = []
            for birthday in collection:
                indeces.append(birthday[3])
            ab.complete(indeces)
            ab.filedel()





def namegather():
    date = ab.today()
    bdaystoday = ab.birthdaycheck(date)
    names=[]
    for k in range(len(bdaystoday)):
        names.append(bdaystoday[k][0])
    return names


def fullapp():
    names = namegather()

    root = tk.Tk()
    root.title('AUTO BDAY')
    if names == []:
        names = None

    app = Application(master=root, birthdays=names)
    app.mainloop()




fullapp()
