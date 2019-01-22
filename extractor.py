#!/usr/bin/python3
import sys
import os
import re
import json


def main(args):

    endSection = '''
                    }
                ],''' + ''' ''' + '''
                '''     # first possible format of end section

    endSection2 = ''': -Infinity
                    }
                ],''' + ''' ''' + '''
                '''     # second possible format of end section

    endSection3 = '''
                    }
                ]
            }
        },''' + ''' ''' + '''
        {
            '''     # third possible format of end section

    endSection4 = ''': -Infinity
                    }
                ]
            }
        },''' + ''' ''' + '''
        {
            '''     # fourth possible format of end section


    extractEducation = "                "   # extracted education section

    extractExperience = "                "  # extracted experience section

    # The program takes in 3 argument
    #   1st: [program_name].py
    #   2nd: <MDB_inputFileName>
    if (len(args) != 2):
        print("incorrect number of commandline arguments")
        print("./extractor.py <inputFileName>")
        sys.exit(0)

    # Checks if the input file exists
    if not os.path.isfile(args[1]):
        print("input file does not exist")
        sys.exit(0)

    # Read the input file
    with open(args[1], 'r') as mdbFile:
        mdbRawStr = mdbFile.read()

    # Split the entire document into sections by '"'
    splitMongoStr = mdbRawStr.split('"')[1::1]

    for x in range(0, len(splitMongoStr)):
        if (splitMongoStr[x] == "education"):
            count = x
            while(True):
                if (splitMongoStr[count] == endSection or splitMongoStr[count] == endSection2 or splitMongoStr[count] == endSection3 or splitMongoStr[count] == endSection4):
                    extractEducation = extractEducation + endSection    # if we reach the end of the education section, put the end section after it
                    break;
                extractEducation = extractEducation + splitMongoStr[count]  # if not, keep adding the education section
                count += 1

        if (splitMongoStr[x] == "experience"):
            count = x
            while(True):
                if (splitMongoStr[count] == endSection or splitMongoStr[count] == endSection2 or splitMongoStr[count] == endSection3 or splitMongoStr[count] == endSection4):
                    extractExperience = extractExperience + endSection    # if we reach the end of the education section, put the end section after it
                    print(extractExperience)
                    print("////////////////////////////////////////////////")
                    print("////////////////////////////////////////////////")

                    break;
                extractExperience = extractExperience + splitMongoStr[count]  # if not, keep adding the experience section
                count += 1


        if (splitMongoStr[x] == "job"):     # adds the job description at the end of the file
            extractEducation += splitMongoStr[x] + splitMongoStr[x + 1] + splitMongoStr[x + 2]
            extractExperience += splitMongoStr[x] + splitMongoStr[x + 1] + splitMongoStr[x + 2]

    with open("education.txt", 'w') as educationFile:
        educationFile.write(extractEducation)

    with open("experience.txt", 'w') as experienceFile:
        experienceFile.write(extractExperience)


if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
