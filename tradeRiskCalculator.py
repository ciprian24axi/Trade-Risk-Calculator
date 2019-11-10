from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Trade Risk Calculator")
window.geometry("800x200")
window.grid_columnconfigure((0,1), weight = 1)

entryPrice = Label(window, text="Please insert the entry price: ", font=("Arial Bold", 16))
entryPrice.grid(column = 0, row = 0)
entryPricetxt = Entry(window, width=10)
entryPricetxt.grid(column=1, row=0)

stopPrice = Label(window, text="Please insert the stop lose price:", font=("Arial Bold", 16))
stopPrice.grid(column = 0, row = 1)
stopPricetxt = Entry(window, width=10)
stopPricetxt.grid(column=1, row=1)

riskLevel = Label(window, text="Chose a risk level", font=("Arial Bold", 16))
riskLevel.grid(column = 0, row = 2)
riskLevelcombo = ttk.Combobox(window, width = 2, state='readonly')
riskLevelcombo['values']= (1,2,3,4,5)
riskLevelcombo.current(0)
riskLevelcombo.grid(column = 1, row =2)

answerUp = Label(window, text="", font=("Arial Bold", 16))
answerUp.grid(column = 0, columnspan = 3, row = 6)

answer = Label(window, text="", font=("Arial Bold", 16))
answer.grid(column = 0, columnspan = 3, row = 7)

answerDown = Label(window, text="", font=("Arial Bold", 16))
answerDown.grid(column = 0, columnspan = 3, row = 8)

def calculate():
    riskLevelUp = float(riskLevelcombo.get()) + 1
    riskLevelDown = float(riskLevelcombo.get()) - 1
    lossDistance = float(entryPricetxt.get()) - float(stopPricetxt.get())
    if lossDistance > 0:
        exitPrice = lossDistance * float(riskLevelcombo.get()) + float(entryPricetxt.get())
        exitPriceUp = lossDistance * float(riskLevelUp) + float(entryPricetxt.get())
        exitPriceDown= lossDistance * float(riskLevelDown) + float(entryPricetxt.get())
        # print('For a reduced risk, respectively a risk level of {}, please exit position at {}'.format(riskLevelDown, exitPriceDown))
        # print('For a increased risk, respectively a risk level of {}, please exit position {}'.format(riskLevelUp, exitPriceUp))
    elif lossDistance < 0:
        exitPrice = float(entryPricetxt.get()) + lossDistance * float(riskLevelcombo.get())
        exitPriceUp = lossDistance * float(riskLevelUp) + float(entryPricetxt.get())
        exitPriceDown= lossDistance * float(riskLevelDown) + float(entryPricetxt.get())
        # print('For a reduced risk, respectively a risk level of {}, please exit position at {}'.format(riskLevelDown, exitPriceDown))
        # print('For a increased risk, respectively a risk level of {}, please exit position {}'.format(riskLevelUp, exitPriceUp))
    elif lossDistance == 0:
        answer.configure(text = "The entry price can't be same with the entry price when you open the position")
    if lossDistance != 0:
        answerUp.configure(text = 'Feel risky today??? exit position at {}'.format(str(exitPriceUp)[0:6]), fg = "red")
        answer.configure(text = 'For a risk level of {}, please exit position at {}'.format(riskLevelcombo.get(), str(exitPrice)[0:6]), fg="green")
        answerDown.configure(text = 'Wanna play safe??? exit position at {}'.format(str(exitPriceDown)[0:6]), fg="blue")
        
btn = Button(window, text="Calculate", command=calculate)
btn.grid(column=0, columnspan = 3, row=5)



window.mainloop()
   