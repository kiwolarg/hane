Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\SDWKLOH\AppData\Roaming\Spotify\Spotify.exe"
WScript.sleep 500
CreateObject("WScript.Shell").Run("spotify:user:spotify:playlist:37i9dQZF1DWT1y71ZcMPe5")
WScript.sleep 3000
WshShell.SendKeys " "

