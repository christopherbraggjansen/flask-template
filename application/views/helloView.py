from application import app
from config import *

@app.route('/')
def index():
  return "Hello"
