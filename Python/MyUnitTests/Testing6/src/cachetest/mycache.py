import sys

def greet(person):
    print(f"Hi {person}.How are you?")

def myerror(issue):
    print(f"Encountered {issue}", file=sys.stderr)
