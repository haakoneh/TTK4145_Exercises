from io import IO
from channels import INPUT, OUTPUT

class Elevator:
	def _init_(self):
		#self.moving = false
		self.direction = OUTPUT.MOTOR_STOP
		self.NUM_FLOORS = INPUT.NUM_FLOORS

		for light in OUTPUT.LIGHTS:
			if light != -1:
				io.setBit(light, 0)



		


	def setButtonLamp(self, lamp, value):
		assert(floor >= 0), "ERR_ floor < 0"
		assert(floor < self.NUM_FLOORS), "ERR_ floor > NUM_FLOORS"
		assert(button >= 0), "ERR_ button < 0"
		assert(button < self.NUM_FLOORS), "ERR_ button > NUM_FLOORS"
		io.setBit(lamp, value)

	def setMotorDirection(self, dir):
		assert(dir in MOTOR_DIRECTION), "ERR: Invalid motor direction!"
		io.writeAnalog(MOTOR, dir)

	def setFloorIndicator(self, floor):
		assert(floor >= 0), "ERR_ floor < 0"
		assert(floor < self.NUM_FLOORS), "ERR_ floor > NUM_FLOORS"

		if floor & 0x02:
			io.setBit(OUTPUT.FLOOR_IND1, 1)
		else:
			io.setBit(OUTPUT.FLOOR_IND1, 0)

		if floor & 0x01:
			io.setBit(OUTPUT.FLOOR_IND2, 1)
		else:
			io.setBit(OUTPUT.FLOOR_IND2, 0)


	def getButtonSignal(self, button, floor):
		assert(floor >= 0)
		assert(floor < NUM_FLOORS)
		if(io.readBit(OUTPUT.BUTTON_FLOORS[floor][button]))
			
	def getFloorSensorSignal(self):
		for index, sensor in enumerate(OUTPUT.SENSORS):
			if io.readBit(sensor):
				return index

		return -1
 
	def setDoorLamp(self, value):
		assert(value >= 0), "ERR: door lamp value < 0"
		assert(value < 1), "ERR: door lamp value > 1"
		io.setBit(OUTPUT.DOOROPEN, value)

	def getStopSignal():
		return io.readBit(STOP)

	def getObstructionSignal():
		return io.readBit(OBSTRUCTION)



