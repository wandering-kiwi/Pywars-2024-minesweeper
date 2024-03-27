
speedScale = 1
def mps(vel):
   speedScale = vel
def runMotors(TL, TR, BL, BR):
   # motor stuff here i haven't figured out yet

   # just to get some sort of a result
   print(TL, TR, BL, BR)
def moveBySpeeds(left, right, dist):
   TL = left
   TR = right
   BR = left
   BL = right
   time = dist/speedScale
   runMotors(TL, TR, BL, BR)
def move(x, y, distScale=1, maxSpeed=50):
   left = maxSpeed
   right = maxSpeed
   if x==y:
      right = 0
      return
   elif x == -y:
      left = 0
      return
   scale = (x+y)/(y-x)
   if abs(x+y)>abs(x-y):
     right = right * scale**-1
     print(x, y, scale)
   else:
      left *= scale
   dist = (x^2 + y^2)**0.5
   dist *= distScale
   moveBySpeeds(left, right, dist)