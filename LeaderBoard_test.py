#! /usr/bin/env python

from LeaderBoard import LeaderBoard
leader_board = LeaderBoard()
leader_board.add_score(1,50)
leader_board.add_score(2,80)
leader_board.add_score(2,70)
leader_board.add_score(2,60)
leader_board.add_score(3,90)
leader_board.add_score(3,85)
leader_board.top(3)
leader_board.top(2)
leader_board.top(1)
leader_board.reset(3)
leader_board.top(3)

