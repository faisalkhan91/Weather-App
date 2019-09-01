#!/usr/local/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/31/2019                                             #
#############################################################################################

# Importing system module

import tkinter
import tkinter.messagebox
import urllib.request
import json


def winddir(deg):
    if deg < 22.5 or deg > 337.5:
        return "N"
    elif deg >= 22.5 and deg < 67.5:
        return "NE"
    elif deg >= 67.5 and deg < 112.5:
        return "E"
    elif deg >= 112.5 and deg < 157.5:
        return "SE"
    elif deg >= 157.5 and deg < 202.5:
        return "S"
    elif deg >= 202.5 and deg < 247.5:
        return "SW"
    elif deg >= 247.5 and deg < 292.5:
        return "W"
    elif deg >= 292.5 and deg < 337.5:
        return "NW"


def callback():
    if len(zipvar.get()) == 5 and zipvar.get().isdigit():

        if unitvar.get() == 1:
            url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipvar.get() + \
                  ",us&mode=json&units=metric&APPID=b0d45b8cc18faf92d77e9825fd5aae74"
        else:
            url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipvar.get() + \
                  ",us&mode=json&units=imperial&APPID=b0d45b8cc18faf92d77e9825fd5aae74"

        try:
            urlobject = urllib.request.urlopen(url)
        except Exception as e:
            tkinter.messagebox.showerror("Server connection",
                                         "Error - unable to connect to server. Exception is " + str(e) + ". Try again.")
            return

        if urlobject.getcode() != 200:
            tkinter.messagebox.showerror("Response code",
                                         "Error - server return code is: " + urlobject.getcode() + " Try again.")
        else:
            response = urlobject.read()
            response = response.decode("utf-8")

            respdict = json.loads(response)
            outstring = "Current weather conditions for " + respdict["name"] + "\n"
            if unitvar.get() == 1:
                outstring += "Temperature = " + str(respdict["main"]["temp"]) + " degrees C\n"
            else:
                outstring += "Temperature = " + str(respdict["main"]["temp"]) + " degrees F\n"

            outstring += "Humidity = " + str(respdict["main"]["humidity"]) + "%\n"
            outstring += "Skies are " + respdict["weather"][0]["description"] + "\n"
            if unitvar.get() == 1:
                outstring += "The wind is blowing at " + str(respdict["wind"]["speed"]) + "m/s from the " + winddir(
                    respdict["wind"]["deg"])
            else:
                outstring += "The wind is blowing at " + str(respdict["wind"]["speed"]) + "mph from the " + winddir(
                    respdict["wind"]["deg"])
            outvar.set(outstring)
    else:
        tkinter.messagebox.showerror("Zipcode validation", "Error - invalid zip code entered. Try again.")


root = tkinter.Tk()
root.title("The Weather Reporter")
root.lift()
root.minsize(500, 500)
root.configure(width=500, height=500, bg="blue")

labelinstructions = tkinter.Label(root,
                                  text="Welcome to the weather reporter. Please enter a zipcode below and hit the "
                                       "button to get a weather report for your city.",
                                  bg="pink")
labelinstructions.grid(row=0, column=0, columnspan=4, sticky="nsew")

labelzip = tkinter.Label(root, text="Zipcode:", bg="orange")
labelzip.grid(row=1, column=0, sticky="nsew")

zipvar = tkinter.StringVar()
zipbox = tkinter.Entry(root, textvariable=zipvar, bg="green")
zipbox.grid(row=1, column=1, sticky="nsew")

unitvar = tkinter.IntVar()
unitvar.set(0)
unitcheck = tkinter.Checkbutton(root, text="Metric", variable=unitvar)
unitcheck.grid(row=1, column=2, sticky="nsew")

doit = tkinter.Button(root, text="Get Weather Report", bg="purple", command=callback)
doit.grid(row=1, column=3, sticky="nsew")

outvar = tkinter.StringVar()
outvar.set("")
outbox = tkinter.Message(root, textvariable=outvar, bg="yellow", width=400)
outbox.grid(row=2, column=0, columnspan=4, sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=3)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.mainloop()

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
