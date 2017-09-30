import pandas as pd

def arrayOfTagsToString(at):
    tags=''
    for tag in at:
        tags+=tag
    return tags

def splitByTimeTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "part-time-job" in arrOfItsTag:
                arrOfItsTimeTag.append("part-time-job")
            if "full-time-job" in arrOfItsTag:
                arrOfItsTimeTag.append("full-time-job")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')

def splitByPayPeriodTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "hourly-wage" in arrOfItsTag:
                arrOfItsTimeTag.append("hourly-wage")
            if "salary" in arrOfItsTag:
                arrOfItsTimeTag.append("salary")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')

def splitByEducationTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "associate-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("associate-needed")
            if "bs-degree-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("bs-degree-needed")
            if "ms-or-phd-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("ms-or-phd-needed")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')

def splitByLicenceTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "licence-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("licence-needed")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')

def splitByExperienceTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "1-year-experience-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("1-year-experience-needed")
            if "2-4-years-experience-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("2-4-years-experience-needed")
            if "5-plus-years-experience-needed" in arrOfItsTag:
                arrOfItsTimeTag.append("5-plus-years-experience-needed")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')

def splitBySupervisingTags(dic):
    timeTagDictionary = {'tags': {}, 'description': {}}
    dicTagObj = dic['tags']
    for index, val in dicTagObj.iteritems():
        timeTagDictionary['description'][str(index)]=(dic['description'][index])
        arrOfItsTimeTag = []
        if type(val) is str:
            arrOfItsTag = val.split(' ')
            if "supervising-job" in arrOfItsTag:
                arrOfItsTimeTag.append("supervising-job")
        timeTagDictionary['tags'][str(index)]=arrOfItsTimeTag
    for index, tagArr in timeTagDictionary['tags'].iteritems():
        timeTagDictionary['tags'][str(index)]=arrayOfTagsToString(tagArr)
    return pd.DataFrame.from_dict(timeTagDictionary,orient='columns')