; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C271CABE-D1DE-46B3-A92B-2CFD5DE732D5}
AppName=LiteBook
AppVerName=LiteBook ver2 Beta
OutputBaseFilename=LiteBook2_Beta_Win_setup
AppPublisher=Hu Jun
AppPublisherURL=http://sites.google.com/site/litebooksite/
AppSupportURL=http://sites.google.com/site/litebooksite/
AppUpdatesURL=http://sites.google.com/site/litebooksite/
DefaultDirName={pf}\LiteBook
DefaultGroupName=LiteBook
DisableProgramGroupPage=yes
Compression=lzma
SolidCompression=yes

[Languages]
Name: "Chinese"; MessagesFile: "compiler:ChineseSim.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\litebook2.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\python26.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\unrar.dll"; DestDir: "{app}"; Flags: ignoreversion
;Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\l2_splash.gif"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\litebook2.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\litebook.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\LiteBook_Readme.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\LiteBook_WhatsNew.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\py.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\bh.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\icon\*"; DestDir: "{app}\icon"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\background\*"; DestDir: "{app}\background"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\HuJun\litebook\tobuild\LB_SVN\2.0-Dev\dist\plugin\*"; DestDir: "{app}\plugin"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "vcredist_x86.exe"; DestDir: "{tmp}"; Check: NeedInstallVC9SP1

[Icons]
Name: "{group}\LiteBook2"; Filename: "{app}\litebook2.exe"
Name: "{group}\{cm:UninstallProgram,LiteBook}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\LiteBook2"; Filename: "{app}\litebook2.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\LiteBook2"; Filename: "{app}\litebook2.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\litebook2.exe"; Description: "{cm:LaunchProgram,LiteBook}"; Flags: nowait postinstall skipifsilent
Filename: "{tmp}\vcredist_x86.exe"; Parameters: /q; WorkingDir: {tmp}; Flags: skipifdoesntexist; StatusMsg: "Installing Microsoft Visual C++ Runtime ..."; Check: NeedInstallVC9SP1

[Code]
var vc9SP1Missing: Boolean;

function NeedInstallVC9SP1(): Boolean;
begin
  Result := vc9SP1Missing;
end;

function InitializeSetup(): Boolean;
var version: Cardinal;
begin
  if RegQueryDWordValue(HKLM, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{9A25302D-30C0-39D9-BD6F-21E6EC160475}', 'Version', version) = false then begin
      if RegQueryDWordValue(HKLM, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{FF66E9F6-83E7-3A3E-AF14-8DE9A809A6A4}', 'Version', version) = false then begin
    vc9SP1Missing := true;
  end;
  end;
  result := true;
end;
