Dim Msg, Style, Title, Response
Msg = "Voulez-vous accèder aux paramètres avant de lancer l'application ?"
Style = vbYesNo
Title = "LOLI Launcher"
Response = MsgBox(Msg, Style, Title)
If Response = vbYes Then
    Set WshShell = WScript.CreateObject("WScript.Shell")
    WshShell.Run "C:\Users\Toinot\Downloads\projet_loli\settings.exe"
Else    ' User chose No.
    Set WshShell = WScript.CreateObject("WScript.Shell")
    WshShell.Run "C:\Users\Toinot\Downloads\projet_loli\main.exe"
End If