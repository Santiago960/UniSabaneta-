@echo off
title Instalador Sistema Universitario UniSabaneta
color 0B

echo ==========================================
echo       INSTALADOR UNISABANETA
echo ==========================================
echo.

echo Creando carpeta del sistema...
mkdir "C:\ProgramaIA" 2>nul

echo.
echo Copiando archivos del proyecto...
xcopy "%~dp0*" "C:\ProgramaIA\" /E /H /C /I /Y

echo.
echo Creando acceso directo en el escritorio...

powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut([Environment]::GetFolderPath('Desktop') + '\UniSabaneta.lnk'); $s.TargetPath='https://unisabaneta.onrender.com'; $s.IconLocation='C:\Windows\System32\shell32.dll,44'; $s.Save()"

echo.
echo ==========================================
echo Instalacion completada correctamente
echo ==========================================
echo.
echo Programa instalado.
echo Acceso directo creado en escritorio.
echo.

pause