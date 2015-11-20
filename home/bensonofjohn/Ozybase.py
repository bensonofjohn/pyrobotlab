import random
leftPort = "COM5"
rightPort = "COM4"

ozy = Runtime.createAndStart("ozy", "InMoov")

webgui = Runtime.createAndStart("webgui","WebGui")
ozyBrain = Runtime.createAndStart("ozyBrain", "ProgramAB")

ozyBrain.startSession("D:\MyRobotLab\ProgramAB", "Ben", "Ozy2")
htmlfilter =  Runtime.createAndStart("htmlfilter", "HtmlFilter") 
# create a Speech service
ozy.startMouth()
ozyBrain.addTextListener(htmlfilter)
htmlfilter.addTextListener(ozy.mouth)

#Servo position variables
headX = 90
headY = 80
leftWrist = 80
leftThumb = 0
leftIndex = 0
leftMiddle = 0
leftRing = 0
leftPinky = 0
rightWrist = 80
rightThumb = 0
rightIndex = 0
rightMiddle = 0
rightRing = 0
rightPinky = 0

#Start Head
ozy.startHead(leftPort)
#Set default positions
##############
# tweaking default settings of jaw
#i01.head.jaw.map(0,180,10,35)
#ozy.mouthControl.setmouth(65,90)
ozy.head.jaw.setMinMax(93,146)
ozy.head.jaw.setRest(93)
# tweaking default settings of eyes
ozy.head.eyeY.setMinMax(0,180)
ozy.head.eyeY.map(0,180,80,100)
ozy.head.eyeY.setRest(85)
ozy.head.eyeX.setMinMax(0,180)
ozy.head.eyeX.map(0,180,70,100)
ozy.head.eyeX.setRest(85)
ozy.head.neck.setMinMax(0,180)
ozy.head.neck.map(0,180,15,155)
ozy.head.neck.setRest(70)
ozy.head.rothead.setMinMax(0,180)
ozy.head.rothead.map(0,180,30,150)
ozy.head.rothead.setRest(86)

##############
ozy.startLeftHand(leftPort)
# tweaking default settings of left hand
ozy.leftHand.thumb.setMinMax(0,180)
ozy.leftHand.index.setMinMax(0,180)
ozy.leftHand.majeure.setMinMax(0,180)
ozy.leftHand.ringFinger.setMinMax(0,180)
ozy.leftHand.pinky.setMinMax(0,180)
#ozy.leftHand.thumb.map(0,180,45,140)
#ozy.leftHand.index.map(0,180,40,140)
#ozy.leftHand.majeure.map(0,180,30,176)
#ozy.leftHand.ringFinger.map(0,180,25,175)
#ozy.leftHand.pinky.map(0,180,15,112)
################
ozy.startLeftArm(leftPort)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)
################
ozy.startRightHand(rightPort)
# tweaking defaults settings of right hand
ozy.rightHand.thumb.setMinMax(0,180)
ozy.rightHand.index.setMinMax(0,180)
ozy.rightHand.majeure.setMinMax(0,180)
ozy.rightHand.ringFinger.setMinMax(0,180)
ozy.rightHand.pinky.setMinMax(0,180)
#ozy.rightHand.thumb.map(0,180,55,135)
#i01.rightHand.index.map(0,180,35,140)
#i01.rightHand.majeure.map(0,180,8,120)
#i01.rightHand.ringFinger.map(0,180,40,125)
#i01.rightHand.pinky.map(0,180,10,110)
#################
ozy.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

#Opening movements

def openLeftHand():
	print("Opening left hand")
	
	global leftWrist
	global leftThumb
	global leftIndex
	global leftMiddle
	global leftRing
	global leftPinky
	global leftWrist
	leftThumb = 0
	leftIndex = 0
	leftMiddle = 0
	leftRing = 0
	leftPinky = 0
	ozy.moveHand("left",leftThumb,leftIndex,leftMiddle,leftRing,leftPinky,leftWrist)

def openRightHand():
	print("Moving right hand")
	
	global rightWrist
	global rightThumb
	global rightIndex
	global rightMiddle
	global rightRing
	global rightPinky
	global rightWrist
	rightThumb = 0
	rightIndex = 0
	rightMiddle = 0
	rightRing = 0
	rightPinky = 0
	ozy.moveHand("right",rightThumb,rightIndex,rightMiddle,rightRing,rightPinky,rightWrist)

def openMouth():
	print("Closing mouth")

def openBothHands():
	print("Closing both hands")

#Closing movements

def closeLeftHand():
	print("Closing left hand")
	
	global leftWrist
	global leftThumb
	global leftIndex
	global leftMiddle
	global leftRing
	global leftPinky
	global leftWrist
	leftThumb = 180
	leftIndex = 180
	leftMiddle = 180
	leftRing = 180
	leftPinky = 180
	ozy.moveHand("left",leftThumb,leftIndex,leftMiddle,leftRing,leftPinky,leftWrist)

def closeRightHand():
	print("Closing right hand")
	
	global rightWrist
	global rightThumb
	global rightIndex
	global rightMiddle
	global rightRing
	global rightPinky
	global rightWrist
	rightThumb = 180
	rightIndex = 180
	rightMiddle = 180
	rightRing = 180
	rightPinky = 180
	ozy.moveHand("right",rightThumb,rightIndex,rightMiddle,rightRing,rightPinky,rightWrist)

def closeMouth():
	print("Closing mouth")

def closeBothHands():
	print("Closing both hands")

#Eye movements

def lookUp():
	print("Looking up")

def lookDown():
	print("Looking down")

def lookLeft():
	print("Looking left")

def lookRight():
	print("Looking right")

def lookMiddle():
	print("Looking the middle")

def thinkingEyes():
	print("I'm Thinking eyes expression")

def brotherEyes():
	print("Oh Brother eyes expression")

def embaressedEyes():
	print("Embaressed eyes expression")

#Head movements

def raiseHead():
	global headX
	global headY
	headY = 140
	ozy.moveHead(headY,headX)
	print("Raise head")

def levelHead():
	global headX
	global headY
	headY = 70
	ozy.moveHead(headY,headX)
	print("Level head")

def lowerHead():
	global headX
	global headY
	headY = 0
	ozy.moveHead(headY,headX)
	print("Lower head")

def turnHeadLeft():
	global headX
	global headY
	headX = 180
	ozy.moveHead(headY,headX)
	print("Turning head left")

def turnHeadRight():
	global headX
	global headY
	headX = 0
	ozy.moveHead(headY,headX)
	print("Turning head right")

def centreHead():
	print("Centre head")

#Waist movements

def bendLeft():
	print("Bending left")

def bendRight():
	print("Bending right")

def straightenUp():
	print("Straightening up")
