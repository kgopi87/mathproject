from flask import Blueprint

routes = Blueprint('Maths', __name__)

from .Authorization import *
from .Add import *
from .Div import *
from .Multi import *
from .Sub import *
