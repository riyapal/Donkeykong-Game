#!/usr/bin/python

'''Donkey Kong'''
from layout import *
from random import *
import os
import sys
import time
from threading import Thread

def getchar():


	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

class Person:
	def __init__(self, i, j):
		self.i=i
		self.j=j
		self.__score=0
		self.__flag=0
		self.__level=1
	def move(self, i, j, ch):
#prev=s[i][j]
		self.printplayer(self.i, self.j, ' ')
		if(ch=='w'or ch=='W'):
#self.__prev=s[self.i][self.j]
			if(self.CheckLadder(self.i-1, self.j) or (s[self.i][self.j-1]=='X' and s[self.i][self.j+1]=='X')):
				self.i-=1
				s[self.i+1][self.j]='H'
		elif(ch=='s' or ch=='S'):
#			self.__prev=s[self.i][self.j]
      			if(self.CheckLadder(self.i+1, self.j)):
				self.i+=1
	    
				s[self.i-1][self.j]='H'
		elif(ch=='a' or ch=='A'):
			self.__prev=s[self.i][self.j]
#if (self.i==22 and self.j==1):
#				self.__nextlevel()
			if (self.CheckWall(self.i, self.j-1) and (s[self.i+1][self.j-1]=='H' or s[self.i+1][self.j-1]=='X')):
				self.j-=1
				if(s[self.i][self.j-1]=='H'):
					s[self.i][self.j+1]='H'
		elif(ch=='d' or ch=='D'):

			self.__prev=s[self.i][self.j]
#print "check"
			if(self.CheckWall(self.i, self.j+1) and (s[self.i+1][self.j+1]=='X' or s[self.i+1][self.j+1]=='H')):
#				print "ok"
				self.j+=1
				if(s[self.i][self.j]=='H'):
#self.j+=1
					s[self.i][self.j]='H'
		self.printplayer(self.i, self.j, 'P')

	def get_x(self):
		return self.i
	def get_y(self):
		return self.j


	def printboard(self):
		for i in range(0,30):
			for j in range(0,80):
				sys.stdout.write(s[i][j])
			print 
	def printplayer(self, i, j, ch):
		if (s[i][j]=='C'):
			self.collectCoin(i,j)
		s[i][j]=ch

	def collectCoin(self,i,j):

		self.__score+=5
		self.__flag+=1

	def coinnum(self):
		return (self.__flag)




	def CheckWall(self,i,j):
		if(s[i][j]=='X'):
			return False
		else:
		 print"func"
		 return True

	def CheckLadder(self, i, j):
		if(s[i][j]!='H'):
			return False
		else:
	 	 return True

	def getscore(self):
		return (self.__score)

	def nextlevel(self):
		self.__level+=1
		self.__score+=50
		b=Board()
#	self.generatecoins()
		b.printboard()
		
#  self.generatecoins()


	def generatecoins(self):
		coins=20
		while(coins!=0):
			i=randint(0,28)
			j=randint(0,79)
			if((s[i+1][j]=='H' and s[i][j]==' ') or (s[i+1][j]=='X' and s[i][j]==' ')):
				s[i][j]='C'
				coins=coins-1
	
	def move_right(self, c, prev):
		l=list(s[self.pos_x])
		l[self.pos_y]=prev
		prev=l[self.pos_y+1]
		l[self.pos_y+1]=c
		s[self.pos_x]="".join(l)
		self.pos_y+=1
		if c=='D':
			return prev

	def move_left(self, c, prev):
                l=list(s[self.pos_x])
                l[self.pos_y]=prev
                prev=l[self.pos_y+1]
                l[self.pos_y-1]=c
                s[self.pos_x]="".join(l)
                self.pos_y-=1
                if c=='D':
		    return prev


class Player(Person):
	def __init__(self, i, j):
		self.i=i
		self.j=j
		self.__score=0
		self.__level=1
	def move(self, i, j, ch):
#prev=s[i][j]
		self.printplayer(self.i, self.j, ' ')
		if(ch=='w'or ch=='W'):
#self.__prev=s[self.i][self.j]
			if(self.CheckLadder(self.i-1, self.j) or (s[self.i][self.j-1]=='X' and s[self.i][self.j+1]=='X')):
				self.i-=1
				s[self.i+1][self.j]='H'
		elif(ch=='s' or ch=='S'):
#			self.__prev=s[self.i][self.j]
      			if(self.CheckLadder(self.i+1, self.j)):
				self.i+=1
	    
				s[self.i-1][self.j]='H'
		elif(ch=='a' or ch=='A'):
			self.__prev=s[self.i][self.j]
			if(self.CheckWall(self.i, self.j-1) and (s[self.i-1][j-1]=='X' or s[self.i-1][j-1]=='H')):
				self.j-=1
				if(s[self.i][self.j-1]=='H'):
					s[self.i][self.j+1]='H'
		elif(ch=='d' or ch=='D'):

			self.__prev=s[self.i][self.j]
#print "check"
			if(self.CheckWall(self.i, self.j+1)):
#				print "ok"
				self.j+=1
				if(s[self.i][self.j]=='H'):
#self.j+=1
					s[self.i][self.j]='H'
		self.printplayer(self.i, self.j, 'P')



	
	def printplayer(self, i, j, ch):
		if (s[i][j]=='C'):
			self.collectCoin(i,j)
		s[i][j]=ch

	def collectCoin(self,i,j):																	self.__score+=5
																		
	def CheckWall(self,i,j):
		if(s[i][j]=='X'):
			return False
		else:
		 print"func"
		 return True
class Donkey(Person):
	print "la"
	def __init__(self, i, j):
		self.i=i
		self.j=j
	def Checkwall(self, di):
		if (s[self.i][self.i]=='X' or s[self.i][self.i]==' '):
			return "right"
		elif (s[self.i][self.i]=='X' or s[self.i][self.i]==' '):
		 	return "left"
		else:
		 lis = ["right", "left"]
		 return(lis[randint(0,1)])

def f1():
	print "hi"	
	global p,b,d
	pr=' '
	di=''
	while(1):
		print "blah"
		d_x=d.get_x()
		d_y=d.get_y()	
		
		di = d.CheckWall(di)
		if di == "right":
			pr=d.move_right('D',pr)
			print "he"
		else:
			pr=d.move_left('D',pr)
			print "lol"
		os.system('clear')
#	board.printboard()
		#b.layout(p)
		time.sleep(0.3)

class Board:
#	def __init__(self)

	def printboard(self):
		for i in range(0,30):
			for j in range(0,80):
				sys.stdout.write(s[i][j])
			print

def main():
	global d
	x=28
	y=1
  	player=Player(x,y)
	person=Person(x,y)
  	person.printplayer(28,1, 'P')
	board=Board()
#	board.generatecoins()
#board.printboard()
#board.printplayer(i, j, 'P')
	os.system("clear")
#	player=Player(i,j)
#getchar()
	person.generatecoins()
	board.printboard()
#	if s[5][1] == ' ':
#		y = 78
#	else:
#		y = 1
#	
	d=Donkey(4,1)
#	r = 1
#person.generatecoins()
	
	while(1):
		print "Enter move:",
		ch=getchar()
#		ch=raw_input()
		if (ch=='q' or ch=='Q'):
			break
#else:
	 	person.move(x, y, ch)
		print "f"
		os.system("clear")
		board.printboard()
#	print "again"
		print "Score:"
		print person.getscore()
		print "Number of coins collected:"
		print person.coinnum()
#		print "Level"
#		print person.nextlevel()
		print "Lives:3"
	print ""
	print "Game over!"
	print person.getscore()
if __name__ == "__main__":
	main()

t1=Thread(target=f1)
t1.start()
