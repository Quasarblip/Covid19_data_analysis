import csv
import os
import math
import pandas as pd
import mpu.pd

import stateData
import GraphingCalculator


#os.chdir('C:\\school\\Math\\FinalCovid19\\')

#Data keaping
	
	


def DataTesting(option, data):
	total = 0.0
	totalStdDeviation = 0.0
	count = 0
	high = 0.0
	highestValueState = ""
	lowestValueState = ""
	low = 100000000
	get = ""

	for state in data:
		count += 1
		#print(count)

		if option == 'testing':
			get = state.getTestingRate()
			if	get == "":
				continue
			elif math.isnan(state.getTestingRate()):
				continue

		if option == 'tested':
			get = state.getPeopleTested()
			if	get == "":
				continue
			elif math.isnan(state.getPeopleTested()):
				continue

		if option == 'deaths':
			get = state.getDeaths()
			if	get == "":
				continue
			if math.isnan(state.getDeaths()):
				continue

		if option == 'confirmed':
			get = state.getConfirmed()
			if	get == "":
				continue
			if math.isnan(state.getConfirmed()):
				continue	
		
		if option == 'recovered':
			get = state.getRecovered()
			if	get == "":
				continue
			if math.isnan(state.getRecovered()):
				continue

		if option == 'hospitilized':
			get = state.getPeopleHospitilized()
			if	get == "":
				continue
			if math.isnan(state.getPeopleHospitilized()):
				continue
		
		if option == 'hospitilizations':
			get = state.getHospitilizationRate()
			if	get == "":
				continue
			if math.isnan(state.getHospitilizationRate()):
				continue

		if option == 'incidents':
			get = state.getIncidentRate()
			if get == "":
				continue
			if math.isnan(state.getIncidentRate()):
				continue
		
		if option == 'mortality':
			get = state.getMortality()
			if get == "":
				continue
			if math.isnan(state.getMortality()):
				continue	
		

		NowValue = float(get)
	
		#capture high and low
		if NowValue > high:
			high = NowValue
		elif NowValue < low:
			low = NowValue
		
		total += NowValue
		totalStdDeviation += NowValue * NowValue

	for state in data:

		#need to refresh the state value in get
		if option == 'testing':
			get = state.getTestingRate()
		if option == 'tested':
			get = state.getPeopleTested()
		if option == 'deaths':
			get = state.getDeaths()
		if option == 'confirmed':
			get = state.getConfirmed()
		if option == 'recovered':
			get = state.getRecovered()
		if option == 'hospitilized':
			get = state.getPeopleHospitilized()
		if option == 'hospitilizations':
			get = state.getHospitilizationRate()
		if option == 'incidents':
			get = state.getIncidentRate()
		if option == 'mortality':
			get = state.getMortality()



		if float(get) == high:
			highestValueState = state.getState()
		if float(get) == low:
			lowestValueState = state.getState()

	AvgValue = total / float(count)
	stdDeviation = math.sqrt(total/count)
	date = state.getLastUpdate()[5:10]

	return date, AvgValue, stdDeviation, high, highestValueState, low, lowestValueState


def DataMortalityRate(data):
	total = 0.0
	totalStdDeviation = 0.0
	count = 0
	high = 0.0
	highestMortalityRateState = ""
	lowestMortalityRateState = ""
	#100 percent mortality rate is not plausible... lets hope.
	low = 100.0
	
	for state in data:
		count += 1
		#print(count)

		if	state.getMortality() == "":
			continue
		elif math.isnan(state.getMortality()):
			continue
		
		NowMortalityRate = float(state.getMortality())
		#print(NowMortalityRate)
	
		#capture high and low
		if NowMortalityRate > high:
			high = NowMortalityRate
		elif NowMortalityRate < low:
			low = NowMortalityRate
		
		total += NowMortalityRate
		totalStdDeviation += NowMortalityRate * NowMortalityRate

	for state in data:
		if state.getMortality() == high:
			highestMortalityRateState = state.getState()
		if state.getMortality() == low:
			lowestMortalityRateState = state.getState()

	AvgMortality = total / float(count)
	stdDeviation = math.sqrt(total/count)

	#print(AvgMortality, 'is the average mortality rate among states')
	#print(stdDeviation, "is the standard deviation")
	
	#print(high, "is the highest value")
	#print(low, "is the lowest value")
	
	return AvgMortality, stdDeviation, high, highestMortalityRateState, low, lowestMortalityRateState







def FormatData(file):

	statesData = []

	df = pd.read_csv(file, delimiter=',')


	data = df.to_dict('records')

	for s in data:
		sd = stateData.StateData(s['Province_State'],
		 s['Confirmed'], s['Deaths'], s['Recovered'],
		  s['Mortality_Rate'], s['Hospitalization_Rate'],
		   s['People_Hospitalized'], s['Active'], s['Incident_Rate'],
		    s['Lat'], s['Long_'], s['People_Tested'], s['Testing_Rate'], s['Last_Update'])

		statesData.append(sd)
	
	#throw out the garbage last lien in the csv data
	statesData.pop(-1)

	#print("There are", statesData[0].getActive(), "Active cases in", statesData[0].getState())
	return statesData







def main():

	#list of state objects 
	data_04_13_20 = FormatData('04-13-2020.csv') #get a list of state objects
	
	print("testing Rates: ")
	print(DataTesting('testing', data_04_13_20))
	#TestingRateData_04_13_20 = DataTesting('testing', data_04_13_20)

	print("people tested: ")
	print(DataTesting('tested', data_04_13_20))
	#PeopleTestedData_04_13_20 = DataTesting('testing', data_04_13_20)

	print("Deaths: ")
	print(DataTesting('deaths', data_04_13_20))
	#DeathsData_04_13_20 = DataTesting('deaths', data_04_13_20)
	
	print("Confirmed: ")
	print(DataTesting('confirmed', data_04_13_20))
	#ConfirmedData_04_13_20 = DataTesting('deaths', data_04_13_20)

	print("recovered: ")
	print(DataTesting('recovered', data_04_13_20))
	#RecoveredData_04_13_20 = DataTesting('deaths', data_04_13_20)

	print("Hospitilized: ")
	print(DataTesting('hospitilized', data_04_13_20))
	#HospitilizedData_04_13_20 = DataTesting('deaths', data_04_13_20)

	print("Hospitilization: ")
	print(DataTesting('hospitilizations', data_04_13_20))
	#HostpitilizationsData_04_13_20 = DataTesting('deaths', data_04_13_20)

	print("Incidents: ")
	print(DataTesting('incidents', data_04_13_20))
	#IncidentsData_04_13_20 = DataTesting('deaths', data_04_13_20)

	print("Mortality: ")
	print(DataTesting('mortality', data_04_13_20))
	#MortalityData_04_13_20 = DataTesting('deaths', data_04_13_20)



	data_04_14_20 = FormatData('04-14-2020.csv') #get a list of state objects

	print("testing Rates: ")
	print(DataTesting('testing', data_04_14_20))
	#TestingRateData_04_14_20 = DataTesting('testing', data_04_14_20)

	print("people tested: ")
	print(DataTesting('tested', data_04_14_20))
	#PeopleTestedData_04_14_20 = DataTesting('testing', data_04_14_20)

	print("Deaths: ")
	print(DataTesting('deaths', data_04_14_20))
	#DeathsData_04_14_20 = DataTesting('deaths', data_04_14_20)
	
	print("Confirmed: ")
	print(DataTesting('confirmed', data_04_14_20))
	#ConfirmedData_04_14_20 = DataTesting('deaths', data_04_14_20)

	print("recovered: ")
	print(DataTesting('recovered', data_04_14_20))
	#RecoveredData_04_14_20 = DataTesting('deaths', data_04_14_20)

	print("Hospitilized: ")
	print(DataTesting('hospitilized', data_04_14_20))
	#HospitilizedData_04_14_20 = DataTesting('deaths', data_04_14_20)

	print("Hospitilization: ")
	print(DataTesting('hospitilizations', data_04_14_20))
	#HostpitilizationsData_04_14_20 = DataTesting('deaths', data_04_14_20)

	print("Incidents: ")
	print(DataTesting('incidents', data_04_14_20))
	#IncidentsData_04_14_20 = DataTesting('deaths', data_04_14_20)

	print("Mortality: ")
	print(DataTesting('mortality', data_04_14_20))
	#MortalityData_04_14_20 = DataTesting('deaths', data_04_14_20)



if __name__ == "__main__":
	main()

