def timeToElapse(data):
    if data['periodType'] == 'days':
        return 2**(data['timeToElapse']//3)
    elif data['periodType'] == 'weeks':
        return 2**(data['timeToElapse']*7//3)
    elif data['periodType'] == 'months':
        return 2**(data[timeToElapse]*30//3)

def estimator(data):
    data = input(data)
    impact = {}
    severeImpact = {}

    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50

    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * timeToElapse(data)
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * timeToElapse(data)





  return data
