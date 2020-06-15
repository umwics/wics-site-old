# Python program to convert data from data.txt file which is
# from U of M Aurora website to JSON.


import json


# the file to be converted
filename = 'data.txt'

# resultant dictionary
dict1 = {}
dict3 = {}
# fields in the sample file
fields = ['dept', 'id', 'title', 'desc-full', 'lab', 'desc',
          'prerequisite-full', 'prerequisite', 'credit', 'name', 'year']


def descriptionFunction(description):
    prereqTest = description.strip().split("Prerequisite: ")
    prereqsssTest = description.strip().split("Prerequisites: ")
    if len(prereqTest) > 1:
        dict2[fields[5]] = prereqTest[0]
        prereq = prereqTest[1].strip().split(".")
        dict2[fields[6]] = prereqTest[1]
        precomptest = prereq[0].strip().split("OMP ")
        if len(precomptest) > 1:
            precomptest2 = precomptest[1].strip().split()
            results = precomptest2[0].strip().split("(")
            result = results[0].strip(';, .')
            dict2[fields[7]] = "COMP "+result
        else:
            dict2[fields[7]] = None
    elif len(prereqsssTest) > 1:
        dict2[fields[5]] = prereqsssTest[0]
        prereq = prereqsssTest[1].strip().split(".")
        dict2[fields[6]] = prereqsssTest[1]
        precomptest = prereq[0].strip().split("OMP ")
        if len(precomptest) > 1:
            precomptest2 = precomptest[1].strip().split()
            results = precomptest2[0].strip().split("(")
            result = results[0].strip(';, .')
            dict2[fields[7]] = "COMP "+result
        else:
            dict2[fields[7]] = None
    else:
        dict2[fields[5]] = description
        dict2[fields[6]] = None
        dict2[fields[7]] = None


def yearFunction(linenumber, coursecount):
    dict2[fields[9]] = name[0]+" "+name[1]
    dict2[fields[0]] = name[0]
    dict2[fields[1]] = name[1]
    dict2[fields[2]] = courseTitle[1]

    line = fh.readline()
    dict2[fields[3]] = line
    linenumber += 1
    description0 = line.strip().split(" Required) ", 2)
    description00 = line.strip().split(" required) ", 2)
    if line == '\n':
        dict2[fields[3]] = None
        dict2[fields[4]] = False
        dict2[fields[5]] = None
        dict2[fields[6]] = None
        dict2[fields[7]] = None
    elif len(description0) > 1:
        dict2[fields[4]] = True
        descriptionFunction(description0[1])
    elif len(description00) > 1:
        dict2[fields[4]] = True
        descriptionFunction(description00[1])
    else:
        dict2[fields[4]] = False
        descriptionFunction(line)

    fh.readline()
    linenumber += 1

    line = fh.readline()
    linenumber += 1
    credit = line.strip().split("Credit", 2)
    if len(credit) > 1:
        dict2[fields[8]] = credit[0].strip()
    dict1[coursecount] = dict2
    

with open(filename, encoding="utf8") as fh:

    # count variable for course id creation
    coursecount = 1
    linenumber = 1
    while True:
        line = fh.readline()
        linenumber += 1
        courseTitle = line.strip().split(" - ", 2)
        if len(courseTitle) > 1:
            name = courseTitle[0].strip().split()
            if name[0] == 'COMP':
                dict2 = {}
                yearTest = name[1]
                if yearTest[0] == '1':
                    dict2[fields[10]] = 1000
                    yearFunction(linenumber, coursecount)
                    coursecount += 1
                elif yearTest[0] == '2':
                    dict2[fields[10]] = 2000
                    yearFunction(linenumber, coursecount)
                    coursecount += 1
                elif yearTest[0] == '3':
                    dict2[fields[10]] = 3000
                    yearFunction(linenumber, coursecount)
                    coursecount += 1
                elif yearTest[0] == '4':
                    dict2[fields[10]] = 4000
                    yearFunction(linenumber, coursecount)
                    coursecount += 1
                else:
                    dict2[fields[10]] = 7000
        else:
            university = line.strip().split(", ", 2)
            if university[0] == 'Université de Saint-Boniface':
                coursecount -= 1

        if not line:
            break


# creating json file
out_file = open("courses-all.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()
