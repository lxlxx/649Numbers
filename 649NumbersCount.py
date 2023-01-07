from typing import List
import re
import pathlib

class Solution:
    def countFreqNumber(self, numberOfRecordIncluded = None, bounsIncluded = None, numberOfOutput = None):
        nums = self.returnNumbers()
        result = {i:0 for i in range(1, 50)}

        totalNumbers = 7 if bounsIncluded else 6
        outputCount = 7 if bounsIncluded else 6
        recordsOfIncluded = len(nums)

        if numberOfRecordIncluded and numberOfRecordIncluded in range(len(nums)):
            recordsOfIncluded = numberOfRecordIncluded

        if numberOfOutput and numberOfOutput in range(50):
            outputCount = numberOfOutput

        for i in range(recordsOfIncluded):
            for n in range(totalNumbers):
                if nums[i][n]:
                    num = nums[i][n]
                    result[num] = result.get(num, 0) + 1

        sortResult = sorted(result.items(), key=lambda item: item[1], reverse=True)

        for i in sortResult[:outputCount]:
            print("numbers: {}, freq: {}".format(i[0], i[1]))

        print(sortResult)
            

    def returnNumbers(self):
        numbersByIndex = []

        validNumbers = [i for i in range(1, 50)]

        nums = []
        dateCheck = False
        path = pathlib.Path(__file__).parent.resolve()
        dateReg = '^["](19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])["]$'

        f = open("{}/649.csv".format(path), "r")
        for line in f:
            lineContents = []
            lineSplit = line.split(',')

            for c in lineSplit:
                if dateCheck:
                    only_number = re.sub('[^0-9]', '', c)
                    if only_number != '' :
                        if int(only_number) in validNumbers:
                            lineContents.append(int(only_number))

                if len(lineContents) == 7:
                    numbersByIndex.append(lineContents)
                    lineContents = []
                    dateCheck = False
                if re.findall(dateReg, c):
                    dateCheck = True
                    
        return numbersByIndex[::-1]

        
test = Solution()
test.returnNumbers()

# test.countFreqNumber(bounsIncluded=False)
# test.countFreqNumber(bounsIncluded=True)


# test.countFreqNumber(numberOfOutput=100)
# test.countFreqNumber(numberOfOutput=10)
# test.countFreqNumber(numberOfOutput=5)
# test.countFreqNumber(numberOfOutput=-1)

# test.countFreqNumber(numberOfRecordIncluded=10000)
# test.countFreqNumber(numberOfRecordIncluded=1000)
# test.countFreqNumber(numberOfRecordIncluded=100)
# test.countFreqNumber(numberOfRecordIncluded=10)
# test.countFreqNumber(numberOfRecordIncluded=5)
# test.countFreqNumber(numberOfRecordIncluded=-1)

    