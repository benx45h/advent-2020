huh.py is the actual code for part 2. script.py covers part 1.  
script2.py was an early part 2 attempt that tried to bruteforce things C-style.  

script2.c and script.c were attempts to bruteforce things C-style in actual C for extra speed when script2.py was too slow.  

huh.py is fast because internally, python uses a hash table for dicts.  

Thanks to Scott Smith for the hash table speed tip- I would never have figured that out. After all, what could be faster than going through an array?
