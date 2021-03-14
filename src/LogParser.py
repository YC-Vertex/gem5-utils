from src.BaseUtil import BaseUtil, match

import os
import re

class LogParser(BaseUtil):
    
    def __init__(self, fname=''):
        super().__init__()

        self.log_file = os.path.join(self.log_dir, fname)
        self.inst_re = re.compile( \
            r'Decode: Decoded ([a-z]*) instruction: ([0-9a-z]{10})')

    def getInstTrace(self):
        return match(self.log_file, self.inst_re)

