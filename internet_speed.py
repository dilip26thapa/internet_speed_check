from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    down = str(round(sp.download()/(1024*1024), 3)) + " Mbps"
    up = str(round(sp.upload()/(1024*1024), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x650")
sp.config(bg="skyblue")
lab = Label(sp, text="Internet Speed", font=(
    "Time New Roman", 30, "bold"), bg="skyblue", fg="white")
lab.place(x=60, y=130, width=380, height=50)
lab = Label(sp, text="Download Speed: ", font=(
    "Time New Roman", 15, "bold"), bg="skyblue", fg="white")
lab.place(x=60, y=130, width=380, height=50)
lab_down = Label(sp, text="00.00 Mbps", font=(
    "Time New Roman", 15, "bold"), bg="skyblue", fg="white")
lab_down.place(x=60, y=200, width=380, height=50)
lab = Label(sp, text="Upload Speed:", font=(
    "Time New Roman", 15, "bold"), bg="skyblue", fg="white")
lab.place(x=60, y=290, width=380, height=50)
lab_up = Label(sp, text="00.00 Mbps", font=(
    "Time New Roman", 15, "bold"), bg="skyblue", fg="white")
lab_up.place(x=60, y=360, width=380, height=50)

button = Button(sp, text="Start", font=("Time New Roman", 15, "bold"),
                bg="white", fg="black", relief=RAISED, command=speedcheck)  # command=speed
button.place(x=60, y=460, width=380, height=50)
sp.mainloop()
