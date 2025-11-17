#!/usr/bin/env python3
# hello.py - Simple Python starter script
"""
A tiny starter script for learning Python.
Run: python hello.py
"""

def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}! Welcome to Python."

def main():
    name = input("What's your name? ").strip() or "friend"
    print(greet(name))

if __name__ == "__main__":
    main()