from src.BaseUtil import BaseUtil, match

import os
import re

class IsaParser(BaseUtil):

    def __init__(self):
        super().__init__()

        self.isa_file = os.path.join(self.isa_dir, 'decoder.isa')
        self.isa_re = re.compile( \
            r'[0-9]*: (?:.*::|)(.*)\({{') # (?:.*::|) to remove "<Format>::"

    def getInstList(self):
        return match(self.isa_file, self.isa_re)


