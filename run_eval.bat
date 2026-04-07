@echo off
set PYTHONDONTWRITEBYTECODE=1
.\.venv\Scripts\activate.bat
deepeval test run test_evaluate_with_deepeval.py
