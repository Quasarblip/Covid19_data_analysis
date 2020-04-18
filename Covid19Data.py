import csv
import os
import math
import pandas as pd
import mpu.pd

from graphics import *
import stateData
import internationalData
import subjectDataSets
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

	#deal with horrible formating w/ date 
	if '/' in str(state.getLastUpdate()):
		date = str(state.getLastUpdate())[:3]
	else:
		date = str(state.getLastUpdate())[5:10]
#	if type(state.getLastUpdate()) == str:
#		return date, AvgValue, stdDeviation, high, highestValueState, low, lowestValueState
#	if math.isnan(state.getLastUpdate()):
#		date = 'null'
	return date, AvgValue, stdDeviation, high, highestValueState, low, lowestValueState

def FormatDataInternational(file):

	CountriesData = []

	df = pd.read_csv(file, delimiter=',')


	data = df.to_dict('records')

	for s in data:
		if s['Country_Region'] == '':
			continue
		id = internationalData.InternationalData(s['Country_Region'], 
		s['Province_State'], s['Confirmed'], s['Deaths'], s['Recovered'],
		s['Active'], s['Lat'], s['Long_'], s['Last_Update'])

		CountriesData.append(id)
		
	#throw out the garbage last line in the csv data
	CountriesData.pop(-1)

	#print("There are", statesData[0].getActive(), "Active cases in", statesData[0].getState())
	return CountriesData



def FormatData(file):

	statesData = []

	df = pd.read_csv(file, delimiter=',')


	data = df.to_dict('records')

	for s in data:
		if s['Province_State'] == '':
			continue
		sd = stateData.StateData(s['Province_State'],
		 s['Confirmed'], s['Deaths'], s['Recovered'],
		  s['Mortality_Rate'], s['Hospitalization_Rate'],
		   s['People_Hospitalized'], s['Active'], s['Incident_Rate'],
		    s['Lat'], s['Long_'], s['People_Tested'], s['Testing_Rate'], s['Last_Update'])

		statesData.append(sd)
		
	#throw out the garbage last line in the csv data
	statesData.pop(-1)

	#print("There are", statesData[0].getActive(), "Active cases in", statesData[0].getState())
	return statesData

def getDateOfMonthInternational(date):
	return date[2:]

def getDateOfMonth(date):
	return date[3:]

def getDataInternational(data, storageClass, printB):
	
	queries = ['deaths', 'confirmed', 'recovered']	
	newData = []
	for i in range(len(queries)):
		
		TransformedData = DataTesting(queries[i], data)
		if printB:
			print()
			print(queries[i] + ":")
			print(TransformedData)

		newData.append(TransformedData)
		
	storageClass.addDeaths_L(newData[0])
	storageClass.addConfirmed_L(newData[1])
	storageClass.addRecovered_L(newData[2])



def getData(data, storageClass, printB):
	 
	queries = ['testing', 'tested', 'deaths', 'confirmed',
	'recovered', 'hospitilized','hospitilizations',
	'incidents', 'mortality']
	newData = []

	for i in range(len(queries)):
		TransformedData = DataTesting(queries[i], data)
		if printB:
			print()
			print(queries[i] + ":")
			print(TransformedData)

		newData.append(TransformedData)

	storageClass.addTestingRates_L(newData[0])
	storageClass.addPeopleTested_L(newData[1])
	storageClass.addDeaths_L(newData[2])
	storageClass.addConfirmed_L(newData[3])
	storageClass.addRecovered_L(newData[4])
	storageClass.addHospitilized_L(newData[5])
	storageClass.addHospitilization_L(newData[6])
	storageClass.addIncidents_L(newData[7])
	storageClass.addMortality_L(newData[8])

	return
		

def graphData(data, graphtitle, color):


	date = 0
	avgerage_value = 1
	standard_deviation = 2
	high_ = 3
	highest_value_state = 4
	low_ = 5
	lowest_value_state = 6

	title = ""
	X = []
	Y = []
	XHigh = 0
	XLow = 0
	YHigh = 0
	YLow = 100000000


	for i in range(len(data)):
		print(data[i][date])
		if len(data[i][date]) == 5:
			x = float(getDateOfMonth(data[i][date]))
		if len(data[i][date]) == 3:
			x = float(getDateOfMonthInternational(data[i][date]))
		y = float(data[i][avgerage_value])

		print('x:',x)
		print('y:',y)
		
		if i == 0:
			#all dates should be added in order for this to be correct
			XLow = x
		if y > YHigh:
			YHigh = y
		if y < YLow:
			YLow = y
		if x > XHigh:
			XHigh = x
		
		X.append( x )
		Y.append( y )

	print('x low:', XLow)
	print('x high:', XHigh)

	print('y low:', YLow)
	print('y high:', YHigh)

	GraphingCalculator.CalculateGraph(X, Y, XLow, XHigh, YLow, YHigh, color, title)

def main():
	PrintInt =True
	PrintState = False
	
	#lists of data objects (international or state)
	us_April = 	subjectDataSets.SubjectDataSets()
	int_April = subjectDataSets.SubjectDataSets()

	###############
	#INTERNATIONAL#
	###############

	data_04_01_20 = FormatDataInternational('04-01-2020.csv')
	getDataInternational(data_04_01_20, int_April, PrintInt)	

	data_04_02_20 = FormatDataInternational('04-02-2020.csv')
	getDataInternational(data_04_02_20, int_April, PrintInt)	

	data_04_03_20 = FormatDataInternational('04-03-2020.csv')
	getDataInternational(data_04_03_20, int_April, PrintInt)	

	data_04_04_20 = FormatDataInternational('04-04-2020.csv')
	getDataInternational(data_04_04_20, int_April, PrintInt)	

	data_04_05_20 = FormatDataInternational('04-05-2020.csv')
	getDataInternational(data_04_05_20, int_April, PrintInt)	

	data_04_06_20 = FormatDataInternational('04-06-2020.csv')
	getDataInternational(data_04_06_20, int_April, PrintInt)	

	data_04_07_20 = FormatDataInternational('04-07-2020.csv')
	getDataInternational(data_04_07_20, int_April, PrintInt)	

	data_04_08_20 = FormatDataInternational('04-08-2020.csv')
	getDataInternational(data_04_08_20, int_April, PrintInt)	

	data_04_09_20 = FormatDataInternational('04-09-2020.csv')
	getDataInternational(data_04_09_20, int_April, PrintInt)	

	data_04_10_20 = FormatDataInternational('04-10-2020.csv')
	getDataInternational(data_04_10_20, int_April, PrintInt)	

	data_04_11_20 = FormatDataInternational('04-11-2020.csv')
	getDataInternational(data_04_11_20, int_April, PrintInt)	

	########
	#STATES#
	########

	data_04_12_20 = FormatData('04-12-2020.csv') 
	getData(data_04_12_20, us_April, PrintState)	

	data_04_13_20 = FormatData('04-13-2020.csv') 
	getData(data_04_13_20, us_April, PrintState)	

	data_04_14_20 = FormatData('04-14-2020.csv') 
	getData(data_04_14_20, us_April, PrintState)	


	data_04_15_20 = FormatData('04-15-2020.csv')
	getData(data_04_15_20, us_April, PrintState)	

	data_04_16_20 = FormatData('04-16-2020.csv')
	getData(data_04_16_20, us_April, PrintState )
	

	#query stored data

	#INTERNATIONAL
	AprilDeathsDataInternational = int_April.getDeaths_L()

	#STATES
	AprilMortalityDataUS = us_April.getMortality_L()
	AprilDeathsDataUS = us_April.getDeaths_L()

	#graphData(AprilDeathsDataUS, "US deaths April", 'black')
	graphData(AprilDeathsDataInternational, "International deaths april", 'red')

if __name__ == "__main__":
	main()

