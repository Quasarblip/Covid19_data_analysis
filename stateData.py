class StateData():

	def __init__(self, state, confirmed, deaths, 
	recovered, mortality, hospitilizationRate, 
	peopleHospitilized, active, incidentRate, lat, 
	long_, peopleTested, testingRate, LastUpdate):
		
		self.mState = state
		self.mConfirmed = confirmed
		self.mDeaths = deaths
		self.mRecovered = recovered
		self.mMortality = mortality
		self.mPeopleTested = peopleTested
		self.mTestingRate = testingRate
		self.mRateHospitilization = hospitilizationRate
		self.mPeopleHospitilized = peopleHospitilized
		self.mActive = active
		self.mIncidentRate = incidentRate
		self.mLat = lat
		self.mLong = long_
		self.mLastUpdate = LastUpdate

	def getState(self):
		return self.mState

	def getLastUpdate(self):
		return self.mLastUpdate

	def getConfirmed(self):
		return self.mConfirmed

	def getDeaths(self):
		return self.mDeaths

	def getRecovered(self):
		return self.mRecovered

	def getMortality(self):
		return self.mMortality

	def getHospitilizationRate(self):
		return self.mRateHospitilization

	def getPeopleHospitilized(self):
		return self.mPeopleHospitilized

	def getActive(self):
		return self.mActive

	def getIncidentRate(self):
		return self.mIncidentRate
	
	def getLat(self):
		return self.mLat
	
	def getLong(self):
		return self.mLong

	def getPeopleTested(self):
		return self.mPeopleTested

	def getTestingRate(self):
		return self.mTestingRate

	
