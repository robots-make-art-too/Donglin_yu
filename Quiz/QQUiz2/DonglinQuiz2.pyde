numRobots = 15;
robots = [0]*numRobots;
robotC = [0]*numRobots;
robotG = [0]*numRobots;
currentRobot = 5; 
def setup():
  size(1400,1080); 
  global numRobots, robots;
  robotA = GrandRobot(0, [],  'A',500, 200);
  for i in range(numRobots):
    robots[i] = GrandRobot(0, [],  'Grand',random(1400), random(900)); 
    robotC[i] = ChildRobot(0, [],  'Children',random(1000), random(700),color(0, 0, 0));    
    robotG[i] = GrandChildRobot(0, [],  'GrandChildren',random(900), random(1000),color(0, 0, 0));    
def draw():
  global numRobots, robots;
  img = loadImage("img.jpg")
  image(img, 0, 0, width, height);
  for i in range(numRobots):
   robots[i].display();
   robotC[i].display();
   robotG[i].display();  
   robots[1].gimmeFlare();
  save("classy-robot-family.png");
def mousePressed():
  global numRobots, currentRobot;
  robots[currentRobot].start(mouseX, mouseY,); 
  currentRobot += 1;
  if (currentRobot >= numRobots):
    currentRobot = 0;
  name(currentRobot);
def load(i):
  pass;
def name(i):
  global numRobots, currentRobot;
  robots[i].name = 'shh' 
  print('My name is: `%s`' %i, robots[i].name);
class GrandRobot(object):
  def __init__(self, param, params,  name, x, y):
    self.name = name;
    self.x = x;
    self.y = y;
  def start(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
  def display(self):
      strokeWeight(3);
      stroke(255, 153);
      rect(self.x-15, self.y+70, 30, 30);
      ellipse(self.x, self.y, 150, 150);
      fill(238,99,99);
      text(self.name, self.x-50, self.y-90); 
      textSize(30);
  def gimmeFlare(self):
    speedx=random(-50,50);
    speedy=random(-30,30);
    self.x += speedx;
    self.y += speedy;
class ChildRobot(GrandRobot):
  def __init__(self, param, params, name, x, y,c):
    GrandRobot.__init__(self,param, params, name, x, y);
    self.c=c;
  def display(self):
    fill(176, 48, 96);
    triangle(self.x, self.y+80, self.x+90, self.y+30, self.x-90,self.y+30);
    ellipse(self.x, self.y, 50,90);
    fill(224,255,255);
    text(self.name, self.x-50, self.y-70); 
    textSize(30);
class GrandChildRobot(ChildRobot):
  def __init__(self, param, params, name, x, y,c):
    ChildRobot.__init__(self,param, params, name, x, y,c);
    self.c=c;
  def display(self):
    ellipse(self.x, self.y+20, 60, 60);
    ellipse(self.x, self.y, 50, 50);
    fill(0,61,139);
    text(self.name, self.x-50, self.y-70); 
    textSize(30);
