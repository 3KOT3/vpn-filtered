@echo off
rem Тихая версия check.bat для Планировщика заданий: без паузы, с записью в лог.
chcp 65001 >nul
setlocal enableextensions
set "HERE=%~dp0"
set "PYTHONIOENCODING=utf-8"
set "PY=%USERPROFILE%\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"

if not exist "%PY%" (
  where python >nul 2>nul
  if not errorlevel 1 set "PY=python"
)

"%PY%" "%HERE%run_local.py" >> "%HERE%last-run.log" 2>&1
