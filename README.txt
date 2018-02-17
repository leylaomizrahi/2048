Leyla Mizrahi

ANY CODE IN STARTER WAS NOT WRITTEN BY ME. 

I have used the differance between the log 2 od the value of the tiles and divided that with the maximumtile on the board. I than added some features for the design and layout of the grid and what the grid has the potential to look like if everything was merged together. To speed up my algorithm I used the minmax algorithm together with alpha beta pruning. This did indeed speed up my algorithm Shown by the examples below. I also added a branching factor depending on the available cells on the board. If there are a lot of available cells, the game is most probably in a good state, and the search tree will be unecassarily huge due to the high number of computer mmove options. If there are more than 10 available cells, I made my maxdepth 1, if there were between 10 and 4 i made the maxdepth 2 and if there were less than 4 I made the maxdepth 3. 
I have gotten results that averaged around 2048. 

With alpha beta pruning:

depth:  3
time: 0.00160503387451  
empty tiles = 1 

depth:  3
time: 0.0642120838165
empty tiles = 3 


depth:  2
time: 0.0873191356659
empty tiles = 6 


depth:  1
time: 0.00429320335388
empty tiles = 8 

depth:  1
time: 0.00334000587463
empty tiles = 12 

Without alpha beta pruning: 

depth:  1
time: 0.0250251293182
empty tiles = 12

depth:  1
time: 0.0223860740662
empty tiles = 8 
 
depth:  2
time: 0.0330159664154
empty tiles = 6

depth:  3
time: 0.0710320472717
empty tiles = 3 

depth: 3
time: 0.0438849925995
empty tiles = 1 
