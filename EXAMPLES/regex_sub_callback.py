#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

#  my $rx_code = qr/(?P<letter>[A-Z])(?P<number>\d{2,3})/i;
#  if ($foo ~= /$rx_code/) { }

rx_code = re.compile(r'(?P<letter>[A-Z])(?P<number>\d{2,3})', re.I)

codes = []
def update_code(m):  # <1>
    letter = m.group('letter').upper()
    number = int(m.group('number'))
    new_code = '{}:{:04d}'.format(letter, number)  # <2>
    codes.append(new_code)
    return new_code

s2 = rx_code.sub(update_code, s)  # <3>
print(s2)

updated_codes = ['{}:{:04d}'.format(s.upper(), int(n)) for s, n in rx_code.findall(s)]
print(updated_codes)
