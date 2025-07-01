@echo off
set PYTHONPATH=.
venv\Scripts\pytest tests/ --disable-warnings -v
pause 