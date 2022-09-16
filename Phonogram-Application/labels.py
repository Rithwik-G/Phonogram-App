from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk


pelName = Label(root, 
	text = "PEL Learning Centers",
	font = (font, 32),
	bg=bg)
spalding = Label(root,
	text = "Spalding",
	font = (font, 40),
	bg=bg)
subText = Label(root,
	text = "Writing Road to Reading",
	font = (font, 30),
	bg=bg)

login = Label(root,
	text = "Login",
	font = (font, 30),
	bg=bg)

email = Label(root,
	text = "Email:",
	font = (font, 25),
	bg=bg)

password = Label(root,
	text = "Password:",
	font = (font, 25),
	bg=bg)


email_en = Entry(root, width=15)
password_en = Entry(root, show="•", width=15)

forgot_pswd = Label(root,
	text = "If you forget your password,\nplease contact your PEL Instructor",
	font = (font, 25),
	bg=bg)

pel_logo = Image.open("Logo Pel Learning Centers.jpg")
pel_logo.thumbnail((100, 100), Image.ANTIALIAS)
pel_logoimg = ImageTk.PhotoImage(pel_logo)
pel_logo = Label(root, image= pel_logoimg, bg=bg)