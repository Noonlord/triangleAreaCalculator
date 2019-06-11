class line():
	def __init__(self, dot1, dot2):
		if dot1.x > dot2.x:
			self.dotRight = dot1
			self.dotLeft = dot2
		else:
			self.dotLeft = dot2
			self.dotRight = dot1
		if self.dotRight.x - self.dotLeft.x is not 0:
			self.slope = (self.dotRight.y - self.dotLeft.y) / (self.dotRight.x - self.dotLeft.x)
		else:
			self.slope = None
		self.length = ((self.dotRight.x - self.dotLeft.x)**2 +  (self.dotRight.y - self.dotLeft.y)**2) ** 0.5
		if self.slope is not None:
			self.intercept = self.dotLeft.y - self.slope*self.dotLeft.x 
