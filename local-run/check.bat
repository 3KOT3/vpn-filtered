@echo off
chcp 65001 >nul
setlocal enableextensions
set "HERE=%~dp0"
set "PYTHONIOENCODING=utf-8"
set "PY="

rem 1) встроенный Python этого окружения
set "CANDIDATE=%USERPROFILE%\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
if exist "%CANDIDATE%" set "PY=%CANDIDATE%"

rem 2) обычный Python из PATH
if not defined PY (
  where python >nul 2>nul
  if not errorlevel 1 set "PY=python"
)
if not defined PY (
  where py >nul 2>nul
  if not errorlevel 1 set "PY=py"
)

if not defined PY (
  echo.
  echo Python не найден. Установите Python 3 или укажите путь к нему вручную.
  echo.
  pause
  exit /b 1
)

echo Проверка VPN-конфигов из вашей сети
echo.
"%PY%" "%HERE%run_local.py" %*
echo.
pause
