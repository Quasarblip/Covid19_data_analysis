class InternationalData():

	def __init__(self, country, state, confirmed, deaths, 
	recovered, active, lat, long_, LastUpdate):
		
		self.mCountry = country
		self.mState = state
		self.mConfirmed = confirmed
		self.mDeaths = deaths
		self.mRecovered = recovered
		self.mActive = active
		self.mLat = lat
		self.mLong = long_
		self.mLastUpdate = LastUpdate

	def getCountry(self):
		return self.mCountry

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

	def getActive(self):
		return self.mActive
	
	def getLat(self):
		return self.mLat
	
	def getLong(self):
		return self.mLong


