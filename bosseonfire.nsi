; NSIS Installation script for Bosse on fire
; Written/copied by Jonne Mickelin 2009

;------------------------
; Modern UI
!include "MUI2.nsh"

;------------------------
; Scrotum
Name "Bosse on Fire"
OutFile "bosseonfire-installer.exe"

InstallDir "$PROGRAMFILES\Bosse On Fire"

RequestExecutionLevel user

;------------------------
; Interface settings
!define MUI_ABORTWARNING

;------------------------
; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE     "LICENSE.txt"
;!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

;------------------------
; Supported languages
!insertmacro MUI_LANGUAGE "English"

;------------------------
; Installation
Section "Dummy Section" DummySec
	SetOutPath "$INSTDIR"

	;; Files go here
	File *.pyd
	File /r data
  File /r songs
	File library.zip
	File MSVCR71.dll
	File python25.dll
	File tcl84.dll
	File tk84.dll
	File w9xpopen.exe
	File main.exe
	File /r tcl
	File avbin.dll

	WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

;------------------------
; Descriptions
  ;Language strings
  LangString DESC_DummySec ${LANG_ENGLISH} "A test section."

  ;Assign language strings to sections
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  ;  !insertmacro MUI_DESCRIPTION_TEXT ${DummySec} $(DESC_DummySec)
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_END

;------------------------
; Uninstallation
Section "Uninstall"
	Delete "$INSTDIR\uninstall.exe"
	RMDir /r "$INSTDIR" ; Unsafe if someone installs it in a folder with other files. I'll list all files explicitly soon.
	
SectionEnd