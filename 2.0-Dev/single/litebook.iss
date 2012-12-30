; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C271CABE-D1DE-46B3-A92B-2CFD5DE732D5}
AppName=LiteBook v3
AppVerName=LiteBook v3.0 beta2
OutputBaseFilename=LiteBook_v3.0b2_Win_setup
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
Name: "Chinese"; MessagesFile: "compiler:ChineseSimp-12-5.1.11.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\litebook.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\python27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\unrar.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\mainlist.txt"; DestDir: "{app}"; Flags: ignoreversion
;Source: "D:\hujun\litebook\tobuild\svn3\single\dist\l2_splash.gif"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\litebook.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\litebook.ico"; DestDir: "{app}"; Flags: ignoreversion
;Source: "D:\hujun\litebook\tobuild\svn3\single\dist\LiteBook_Readme.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\defaultconfig.ini"; DestDir: "{app}"; Flags: ignoreversion
;Source: "D:\hujun\litebook\tobuild\svn3\single\dist\LiteBook_WhatsNew.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\py.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\bh.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\icon\*"; DestDir: "{app}\icon"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\kadp\*"; DestDir: "{app}\kadp"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\jieba\*"; DestDir: "{app}\jieba"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\UnRAR2\*"; DestDir: "{app}\UnRAR2"; Flags: ignoreversion recursesubdirs createallsubdirs
;Source: "D:\hujun\litebook\tobuild\svn3\single\dist\helpdoc\*"; DestDir: "{app}\helpdoc"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\background\*"; DestDir: "{app}\background"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\plugin\*"; DestDir: "{app}\plugin"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\hujun\litebook\tobuild\svn3\single\dist\templates\*"; DestDir: "{app}\templates"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "vcredist_x86.exe"; DestDir: "{tmp}"; Check: NeedInstallVC9SP1

[Icons]
Name: "{group}\LiteBook"; Filename: "{app}\litebook.exe"
Name: "{group}\�ָ���ȱʡ��������"; Filename: "{app}\litebook.exe"; IconFilename: "{app}\litebook.exe"; Parameters: " -reset"
Name: "{group}\{cm:UninstallProgram,LiteBook}"; Filename: "{uninstallexe}";
Name: "{commondesktop}\LiteBook"; Filename: "{app}\litebook.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\LiteBook"; Filename: "{app}\litebook.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\litebook.exe"; Description: "{cm:LaunchProgram,LiteBook}"; Flags: nowait postinstall skipifsilent
Filename: "{tmp}\vcredist_x86.exe"; Parameters: /q; WorkingDir: {tmp}; Flags: skipifdoesntexist; StatusMsg: "Installing Microsoft Visual C++ Runtime ..."; Check: NeedInstallVC9SP1

[Registry]
;�����Ҽ��˵���
Root: HKLM; Subkey: "Software\CLASSES\*\shell\�� LiteBook �Ķ�"; Flags: uninsdeletekey
Root: HKLM; Subkey: "Software\CLASSES\*\shell\�� LiteBook �Ķ�\command"; ValueType: String; ValueData: "{app}\litebook.exe %1"; Flags: uninsdeletekey


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

