import pywhatkit 
import pandas as pd


sheet_id='1PkLVfsREfabArci-yW7WIMGkYmemHnN2H3pQySe6nB8'

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

for i in df:
    pywhatkit.sendwhatmsg("+91"+i,"Hello",3,15,1,True,3)