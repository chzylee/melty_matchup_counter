import re
import logger
from logger import Logger

MATCHUP_REGEX = re.compile('[A-Z]+_?[A-Z]*x[A-Z]+_?[A-Z]*')
SHOULD_DEBUG_LOG = False
logger = Logger(SHOULD_DEBUG_LOG)

class FilenameError(Exception):
    # Raised when something is wrong with filename being parsed.
    def __init__(self, message):
        self.message = message
        super.__init__(self.message)

# Some char names contain '_' but if char name does not,
# regex will capture a trailing _ that we do not want.
def trimMatchup(matchup):
    return matchup[:-1] if matchup.endswith('_') else matchup

def getChars(matchup):
    trimmed_matchup = trimMatchup(matchup)
    return trimmed_matchup.split('x')

def getMatchup(filename):
    logger.log(f'Matching {filename}')
    match = MATCHUP_REGEX.match(filename)
    if match == None:
        raise FilenameError(f'Failed to match matchuup regex for file {filename}')
    matchup = getChars(match.group())
    return matchup

# Given matchup has 2 names, return one that is not
# the given char_name.    
def getOpponent(matchup, char_name):
    char1 = matchup[0]
    char2 = matchup[1]
    logger.log(f'Char1 = {char1}, Char2 = {char2}, char: {char_name}')
    if char1 != char_name and char2 != char_name:
        return None
    return char2 if char1 == char_name else char1

