# Python program to convert data from data.txt file which is
# from U of M Aurora website to JSON. The output json file will have 
# only available courses by webscraping from U of M CS website 
#



import json
import yaml
import os

# the file to be converted
filename = 'data.txt'

#dictYear = ['Comp 1000 Courses', "Comp 2000 Courses", "Comp 3000 Courses", "Comp 4000 Courses"]
dictYear = {}
i = 0
for file in os.listdir("webscrap-course\\"):
    if file.endswith(".json"):
        with open("webscrap-course\\"+file) as json_file: 
            dictYear[i] = json.load(json_file)
            i += 1

dictProg = {}
i = 0
for file in os.listdir("webscrap-program\\"):
    if file.endswith(".json"):
        with open("webscrap-program\\"+file) as json_file: 
            dictProg[i] = json.load(json_file)
            i += 1

# resultant dictionary
dict1 = []
# fields in the sample file
fields = ['dept', 'coursenumber', 'title', 'descfull', 'lab', 'desc',
          'prerequisitefull', 'prerequisite', 'credit', 'name', 
          'year', 'honours', 'major', 'id']


def descriptionFunction(description):
    # fields[0] dept /1 coursenumber /2 title/3 desc-full/ 4 lab/ 5 desc/ 6 prerequisite-full/ 
    # 7 prerequisite/ 8 credit/ 9 name/ 10 year/ 11 honours/ 12 major/ 13 id
    prereqTest = description.strip().split("Prerequisite: ")
    prereqsssTest = description.strip().split("Prerequisites: ")
    if len(prereqTest) > 1:
        dict2[fields[5]] = prereqTest[0]
        prereq = prereqTest[1].strip().split(".")
        dict2[fields[6]] = prereqTest[1]

        # select only prerequisite course names
        split_line = prereq[0].strip().split()
        prerequisiteList = []

        split_and = prereq[0].strip().split(" and ")

        if len(split_and) > 1:
            for andSplit in split_and:
                andsplit_space = andSplit.strip().split()
                for word in andsplit_space:
                    if word.lower() in ['comp', 'math', 'stat']:
                        index = andsplit_space.index(word)
                        id = andsplit_space[index+1].strip().split("(")
                        name = word+id[0].strip(';.,')
                        if name not in ['COMP2190']:
                            prerequisiteList.append(name)
                            dict2[fields[7]]= prerequisiteList 
                        break
        else:
            for word in split_line:
                if word.lower() in ['comp', 'math', 'stat']:
                    index = split_line.index(word)
                    id = split_line[index+1].strip().split("(")
                    name = word+id[0].strip(';.,')
                    if name not in ['COMP2190']:
                            prerequisiteList.append(name)
                            dict2[fields[7]]= prerequisiteList 
                    break

    elif len(prereqsssTest) > 1:
        dict2[fields[5]] = prereqsssTest[0]
        prereq = prereqsssTest[1].strip().split(".")
        dict2[fields[6]] = prereqsssTest[1]

        # select only prerequisite course names
        split_line = prereq[0].strip().split()
        prerequisiteList = []

        split_and = prereq[0].strip().split(" and ")

        if len(split_and) > 1:
            for andSplit in split_and:
                andsplit_space = andSplit.strip().split()
                for word in andsplit_space:
                    if word.lower() in ['comp', 'math', 'stat']:
                        index = andsplit_space.index(word)
                        id = andsplit_space[index+1].strip().split("(")
                        name = word+id[0].strip(';.,')
                        if name not in ['COMP2190']:
                            prerequisiteList.append(name)
                            dict2[fields[7]]= prerequisiteList 
                        break
        else:
            for word in split_line:
                if word.lower() in ['comp', 'math', 'stat']:
                    index = split_line.index(word)
                    id = split_line[index+1].strip().split("(")
                    name = word+id[0].strip(';.,')
                    if name not in ['COMP2190']:
                        prerequisiteList.append(name)
                        dict2[fields[7]]= prerequisiteList 
                    break

    else:
        dict2[fields[5]] = description
        dict2[fields[6]] = None
        dict2[fields[7]] = None


def yearFunction(linenumber, coursecount):
    dict2[fields[9]] = name[0]+" "+name[1]
    dict2[fields[13]] = name[0]+name[1]
    dict2[fields[0]] = name[0]
    dict2[fields[1]] = name[1]
    dict2[fields[2]] = courseTitle[1]

    dict2[fields[11]] = False
    dict2[fields[12]] = False
    #Honours | fields[11] = honours fields[12] = major
    for sub in dictProg[0]: 
        if sub['name'] == name[0]+" "+name[1]:
            dict2[fields[11]] = True
            break
    #Major | fields[11] = honours fields[12] = major
    for sub in dictProg[1]: 
        if sub['name'] == name[0]+" "+name[1]:
            dict2[fields[12]] = True
            break

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
    dict1.append(dict2)


with open(filename, encoding="utf8") as fh:

    # count variable for course id creation
    coursecount = 1
    linenumber = 1
    while True:
        line = fh.readline()
        print(line)
        #line = fh.readline().replace("''", "&#39;")
        linenumber += 1
        courseTitle = line.strip().split(" - ", 2)
        if len(courseTitle) > 1:
            
            name = courseTitle[0].strip().split()
            if name[0] == 'COMP':
                dict2 = {}
                yearTest = name[1]
                if yearTest[0] == '1':
                    for sub in dictYear[0]: 
                        if sub['name'] == courseTitle[0]: 
                            dict2[fields[10]] = 1000
                            yearFunction(linenumber, coursecount)
                            coursecount += 1
                            break
                elif yearTest[0] == '2':
                    for sub in dictYear[1]: 
                        if sub['name'] == courseTitle[0]: 
                            dict2[fields[10]] = 2000
                            yearFunction(linenumber, coursecount)
                            coursecount += 1
                            break
                elif yearTest[0] == '3':
                    for sub in dictYear[2]: 
                        if sub['name'] == courseTitle[0]: 
                            dict2[fields[10]] = 3000
                            yearFunction(linenumber, coursecount)
                            coursecount += 1
                            break
                elif yearTest[0] == '4':
                    for sub in dictYear[3]: 
                        if sub['name'] == courseTitle[0]: 
                            dict2[fields[10]] = 4000
                            yearFunction(linenumber, coursecount)
                            coursecount += 1
                            break
                else:
                    dict2[fields[10]] = 7000

        if not line:
            break


# creating json file
out_file = open("courses.yml", "w")
yaml.dump(dict1, out_file, default_flow_style=False)
out_file.close()
