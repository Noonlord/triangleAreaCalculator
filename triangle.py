import line
class triangle:
	def __init__(self, dot1, dot2, dot3):
		self.dot1 = dot1
		self.dot2 = dot2
		self.dot3 = dot3
		self.line1 = line.line(dot1, dot2)
		self.line2 = line.line(dot1, dot3)
		self.line3 = line.line(dot2, dot3)
		self.lines = [self.line1, self.line2, self.line3]
		if self.line1.slope is not None:
			self.baseLine = self.line1
			self.tip = self.dot3
		else:
			self.baseLine = self.line2
			self.tip = self.dot2
		self.height = abs((self.baseLine.slope*self.tip.x - self.tip.y + self.baseLine.intercept)) / (self.baseLine.slope ** 2 + 1) ** 0.5
		self.area = self.height * self.baseLine.length * 0.5
