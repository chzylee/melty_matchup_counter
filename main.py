import os
from os import listdir
from os.path import isfile, join
import filename_utilities

def countOpponents(filenameList, char_name):
    opponent_counts = {}
    
    for filename in filenameList:
        matchup = filename_utilities.getMatchup(filename)
        opponent_char = filename_utilities.getOpponent(matchup, char_name)
        # None suggests neither char is one we are interested in, so we skip.
        if opponent_char != None:
            count = opponent_counts.get(opponent_char)
            if count == None:
                opponent_counts[opponent_char] = 1
            else:
                opponent_counts[opponent_char] += 1
            
    return opponent_counts

def printOpponentCounts(count_dict):
    for opp, count in count_dict.items():
        print(f'{opp}: {count}')

def countMatchupsPlayed():
    print('Please enter path to replay directory:')
    replay_dir_path = str(input())
    print('Please enter name of the char you play as it appears in replay filename:')
    char_name = str(input()).upper()
    
    filenames = [filename for filename in os.listdir(replay_dir_path) if isfile(join(replay_dir_path, filename))]
    
    opponent_count_dict = countOpponents(filenames, char_name)
    # source: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_counts = dict(sorted(opponent_count_dict.items(), key=lambda item: item[1]))
    
    printOpponentCounts(sorted_counts)
    
countMatchupsPlayed()