!include "MUI2.nsh"

Name "Bosse on Fire"
OutFile "bosseonfire.exe"

InstallDir "$DESKTOP\Bosse On Fire"

RequestExecutionLevel user

!define MUI_ABORTWARNING

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

!insertmacro MUI_LANGUAGE "English"

Section "Dummy Section" DummySec
	SetOutPath "$INSTDIR"

	;; Files go here

	WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

  ;Language strings
  LangString DESC_DummySec ${LANG_ENGLISH} "A test section."

  ;Assign language strings to sections
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  ;  !insertmacro MUI_DESCRIPTION_TEXT ${DummySec} $(DESC_DummySec)
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_END

Section "Uninstall"
	Delete "$INSTDIR\uninstall.exe"
	RMDir "$INSTDIR"
	
SectionEnd