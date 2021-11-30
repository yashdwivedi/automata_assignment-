class Turing_Machine:
  def __init__(self,state,change_h,tp_li):
      self.state = state
      self.change_h = change_h
      self.tp_li = tp_li
  
  def getState(self):
      return self.state
  
  def getHead(self):
      return self.change_h
  
  def getList(self):
      return self.tp_li
  def updateMachine(self, cha_arr):  
    if (self.state == 'q1'):
        if (self.tp_li[self.change_h] != 0):
            char_read = self.tp_li[self.change_h]
            char_index = cha_arr.index(char_read)
            self.state = ''.join(['p',str(char_index)])
            self.tp_li[self.change_h] = 0
            self.change_h += 1
        else:
            self.state = 'qy'
            self.tp_li[self.change_h] = 0
            self.change_h += 1

    elif (self.state.startswith('p')):
        if (self.tp_li[self.change_h]!=0):
            self.state = self.state
            self.tp_li[self.change_h] = self.tp_li[self.change_h]
            self.change_h += 1
        else:
            self.state = ''.join(['r',self.state[1:]])
            self.tp_li[self.change_h] = 0
            self.change_h -= 1
                
    elif (self.state.startswith('r')):
        char_read = cha_arr[int(self.state[1:])]
        if (self.tp_li[self.change_h] != char_read and self.tp_li[self.change_h] != 0):
            self.state = 'qn'
            self.tp_li[self.change_h] = self.tp_li[self.change_h]
            self.change_h -= 1
        else:
            self.state = 'q2'
            self.tp_li[self.change_h] = 0
            self.change_h -= 1
            
    elif (self.state == 'q2'):
        if (self.tp_li[self.change_h] != 0):
            self.state = 'q2'
            self.tp_li[self.change_h] = self.tp_li[self.change_h]
            self.change_h -= 1
        else:
            self.state = 'q1'
            self.tp_li[self.change_h] = 0
            self.change_h += 1

import string
import sys
def check_palindrome(initial_string):
    cha_arr = list(string.ascii_lowercase)
    cha_arr.append(' ') 
    initial_list = list(initial_string)
    initial_list.append(0)

    i_change_h = 0
    i_state = 'q1' 
    i_tp_li = initial_list

    runMachine = Turing_Machine(i_state,i_change_h,i_tp_li)
    ctr=0
    while runMachine.getState() != 'qy' and runMachine.getState() != 'qn' and ctr < 1000:
        runMachine.updateMachine(cha_arr)
        ctr += 1
    if (runMachine.getState() == 'qy'):
        print(initial_string,'is a palindrome')
    else:
        print(initial_string,'is NOT a palindrome!')

check_palindrome("aaaa")

