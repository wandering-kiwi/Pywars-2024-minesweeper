from flask import Flask, render_template
from robotControls import *
mps(0.2)
class Pos:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def copy(self):
      return Pos(self.x, self.y)
   def dist(self, pos2):
      return Pos(self.x - pos2.x, self.y - pos2.y)
   def __repr__(self):
      return f"<Pos a:{self.a} b:{self.b}>"
   def __str__(self):
      return f"x:{self.x} y:{self.y}"

app = Flask(__name__)
currPos = Pos(0, 0)
prevPos = Pos(0, 0)
@app.route('/')
def start():
   return render_template('index.html', s=3, x=0, y=0)
@app.route('/<size>/<x>/<y>')
def button_test(size, x, y):
   global currPos
   prevPos = currPos.copy()
   currPos = Pos(int(x), -int(y))
   dist = currPos.dist(prevPos)
   move(dist.x, dist.y, distScale=40, maxSpeed=78)
   return render_template('index.html', s=size, x=x, y=y)
if __name__=='__main__':
   app.run(debug=True, port=80, host='0.0.0.0')