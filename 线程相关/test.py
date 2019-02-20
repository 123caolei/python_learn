#!/usr/bin/env python

stack = []

def pushit():
    stack.append(raw_input('input').strip())

def popit():
    if len (stack)==0:
        print 'cannot rm from a null stack'
    else:
        print'removed [' ,`stack.pop()`, ']'
def viewstack():
        print stack

CMDs={'u':pushit,'o':popit,'v':viewstack}



while True:
    while True:
        try:
            pr =''
            choice=raw_input(pr).strip()[0].lower()
        except(EOFError,KeyboardInterrupt,IndexError):
             choice = 'q'
        print '\nyoupicked:[%s]' % choice
        if choice not in 'uovp':
            print 'retry'
        else:
            break
    if choice == 'q':
        break
        CMDs[choice]()

