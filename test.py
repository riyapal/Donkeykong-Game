from donkeykong import *
from layout import *
import os
import sys

p=Player(28,1)

class Test_Player:

	
	def test_move(self):
#		p.printplayer(p.i, p.j, 'w')
		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		p.printplayer(p.i, p.j, 'w')
#		if(ch=='w'or ch=='W'):

		if(Player.CheckLadder(p,p.i-1, p.j) or (s[p.i][p.j-1]=='X' and s[p.i][p.j+1]=='X')):
			p.i-=1
			new_x=Player.get_x(p)
			new_y=Person.get_y(p)
			assert new_x == pos_x-1
			assert new_y == pos_y
		else:
			new_x = Player.get_x(p)
			new_y = Player.get_y(p)
			assert new_x == pos_x
			assert new_y == pos_y
		

		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		p.printplayer(p.i, p.j, 's')
		#if(ch=='s' or ch=='S'):

		if(Player.CheckLadder(p,p.i+1, p.j)):
				
			p.i+=1
			new_x=Player.get_x(p)
			new_y=Player.get_y(p)
			assert new_x == pos_x+1
			assert new-y == pos_y

		else:
			new_x = Player.get_x(p)
			new_y = Player.get_y(p)
			assert new_x == pos_x
			assert new_y == pos_y


		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		p.printplayer(p.i, p.j, 'a')
		#elif(ch=='a' or ch=='A'):
		if(Player.CheckWall(p,p.i, p.j-1) and (s[p.i-1][p.j-1]=='X' or s[p.i-1][p.j-1]=='H')):
			p.j-=1
			new_x=Player.get_x(p)
			new_y=Player.get_y(p)

			assert new_x == pos_x
			assert new_x == pos_y-1
		else:
			new_x = Player.get_x(p)
			new_y = Player.get_y(p)
			assert new_x == pos_x
			assert new_y == pos_y

		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		p.printplayer(p.i, p.j, 'd')
#elif(ch=='d' or ch=='D'):
		if(Player.CheckWall(p,p.i, p.j+1)):
			p.j+=1
			new_x = Player.get_x(p)
			new_y = Player.get_y(p)

			assert new_x == pos_x
			assert new_y == pos_y+1
                else:

			new_x = Player.get_x(p)
			new_y = Player.get_y(p)
			assert new_x == pos_x
			assert new_y == pos_y

	def test_CheckWall(self):
		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		value = Player.CheckWall(p,pos_x,pos_y)
		if(s[pos_x][pos_y]=='X'):
			assert value == False
		else:
		 	assert value == True

	def test_CheckLadder(self):
		pos_x=Player.get_x(p)
		pos_y=Player.get_y(p)
		v = Player.CheckLadder(p, pos_x, pos_y)
		if(s[pos_x][pos_y]!='H'):
			assert v == False
		else:
		 	assert v == True


	def test_generatecoins(self):
		coins=0
		Player.generatecoins(p)
		i=1
		j=1
		while(i<29):
		       while(j<79):
			       if (s[i][j]=='C'):
				       coins+=1
			       j+=1
#		       assert coins == 1
#
		       i+=1
		       j=1
		assert coins == 20

