# PythonChallange
This is my attempt to solve the puzzel that is on http://www.pythonchallenge.com/


Level 0:
 The level 0 has me do 2^38 which is as python tell me 274877906944
 put that in url i get www.pythonchallenge.com/pc/def/274877906944.html
 
 which redirects to : www.pythonchallenge.com/pc/def/map.html
 
 Level 1:
  The level 1 has one pic nothing else
  which reads
  K -->M
  O -->Q
  E --> G
  
  so basically this seems simple cryptography and here each of the latter is 2 step ahead so
  I.E. A becomes C
  
  so
  well i think this is the level where coding begames
  
  i used  ``.maketrans`` to string to change latters
  and what i get is
  >i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
  
  so yeaa i guess i was right and now we have the ``map`` in url changin it we get ``ocr``
  
  Thus we get url