#  The file holds the information about authentication key

from .Generator import Token
from .ReadWrite import Readwrite as rw


class Auth:

    def gettoken(self):
        strsavedToken = Token.token_generator(50)
        savedToken = rw.read(self)
        savedToken.append(strsavedToken)
        rw.write(self, savedToken)
        return strsavedToken

    def checktoken(self, token):
        savedToken = rw.read(self)
        if token in savedToken:
            return True
        else:
            return False
