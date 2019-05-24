from ctypes import *
import platform

s = ''.join(platform.architecture()[0])
print(s)
if("64bit" == s):
	dll = CDLL("music64.dll")
else:
	dll = CDLL("music32.dll")
	
def DelayMsBlockage(dly):
	dll.DelayMsBlockage(dly)
	
def SetCursorPosition(x,y):
	dll.SetCursorPosition(x,y)
	
def HideCursor():
	dll.HideCursor()
	
def ClearRec(start_x,end_x,start_y,end_y):
	dll.ClearRec(start_x,end_x,start_y,end_y)

def CLearALL():
	dll.ClearALL()
	
def SetWindowsSize(x,y):
	dll.SetWindowsSize(x,y)

def GetMusicPath():
	dll.GetMusicPath()
	
def MusicLoad():
	dll.MusicLoad()
	
def StopMusic():
	dll.StopMusic()
	
def PlayMusic():
	dll.PlayMusic

def PauseMusic():
	dll.PauseMusic()

def NextMusic():
	dll.NextMusic()
	
def PrevMusic():
	dll.PrevMusic()

def MusicShow():
	dll.MusicShow()
	
def Example():
	dll.main()
