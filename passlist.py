#!/usr/bin/env python
 
  
import os
      

class Generator(object):
 def __init__(self,first,last):
  self.first = first.strip()
  self.last  = last.strip()
    
 def Modify(self,text):
  for num in range(1000):
   self.Write('{}{}'.format(text.title(),num))    
   self.Write('{}{}'.format(text.upper(),num))
   self.Write('{}{}'.format(text.lower(),num))      
 
 def Generator(self):
  self.Modify(self.first)
  self.Modify(self.last)
  self.Modify('{}{}'.format(self.first,self.last))
  self.Modify('{}{}'.format(self.last,self.first)) 

  first = self.first.title()
  last  = self.last.title()
  for num in range(1000):
   self.Write('{}{}{}'.format(first,last,num))
   self.Write('{}{}{}'.format(last,first,num))  
      
 def Write(self,text):
  word = '{}\n'.format(text)
  with open('Pass.txt','a') as WriteFile:
   WriteFile.write(word)

if __name__ == '__main__':
 items = [item for item in os.listdir('.')]
 if 'Pass.txt' in items:
  os.system('rm Pass.txt')                                          
  
 
 raykoo = raw_input('first name: ')
 expert = raw_input('last name:  ')
 Generator(raykoo,expert).Generator()
