
def timeToElapse(data):
    if data['periodType'] == 'days':
        return 2**(data['timeToElapse']//3)

    elif data['periodType'] == 'weeks':
         return 2**(data['timeToElapse']*7//3)

    elif data['periodType'] == 'months':
        return 2**(data['timeToElapse']*30//3)



def estimator(data):
    data = dict(data)
    impact = {}
    severeImpact = {}

#challengeOne
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50

    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * timeToElapse(data)
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * timeToElapse(data)

#challengeTwo
#Severe impact
    severeCasesByRequestedTime = float((15/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['severeCasesByRequestedTime'] =  severeCasesByRequestedTime
    bedsByRequestedTime = float((35/100) * data['totalHospitalBeds'])
    severeImpact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - severeCasesByRequestedTime
#Impact
    impact['severeCasesByRequestedTime'] = float((15/100) * impact['infectionsByRequestedTime'])
    impact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - impact['severeCasesByRequestedTime']






#Output
    data = {'data': data,
            'impact': impact,
            'severeImpact': severeImpact}

    return data
