class SubjectDataSets():

	def __init__(self):
		self.mTestingRates_L = []
		self.mPeopleTested_L = []
		self.mDeaths_L = []
		self.mConfirmed_L = []
		self.mRecovered_L = []
		self.mHospitilized_L = []
		self.mHospitilization_L = []
		self.mIncidents_L = []
		self.mMortality_L = []

	def getTestingRates_L(self):
		return self.mTestingRates_L

	def getPeopleTested_L(self):
		return self.mPeopleTested_L
	
	def getDeaths_L(self):
		return self.mDeaths_L
	
	def getConfirmed_L(self):
		return self.mConfirmed_L

	def getRecovered_L(self):
		return self.mRecovered_L
	
	def getHospitilized_L(self):
		return self.mHospitilized_L

	def getHospitilization_L(self):
		return self.mHospitilization_L

	def getIncidents_L(self):
		return self.mIncidents_L

	def getMortality_L(self):
		return self.mMortality_L




	def addTestingRates_L(self, data):
		self.mTestingRates_L.append(data)

	def addPeopleTested_L(self, data):
		self.mPeopleTested_L.append(data)
	
	def addDeaths_L(self, data):
		self.mDeaths_L.append(data)
	
	def addConfirmed_L(self, data):
		self.mConfirmed_L.append(data)

	def addRecovered_L(self, data):
		self.mRecovered_L.append(data)
	
	def addHospitilized_L(self, data):
		self.mHospitilized_L.append(data)

	def addHospitilization_L(self, data):
		self.mHospitilization_L.append(data)

	def addIncidents_L(self, data):
		self.mIncidents_L.append(data)

	def addMortality_L(self, data):
		self.mMortality_L.append(data)
