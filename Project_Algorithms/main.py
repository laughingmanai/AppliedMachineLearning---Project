import getopt
import sys
from collections import Counter
import argparse


data_training = []
data_testing = []
counterTEST = 0
counterTRAIN = 0

kValueList = []


def Results():
    count0 = 0;
    correct0 = 0;
    accuracy0 = 0;
    count1 = 0;
    correct1 = 0;
    accuracy1 = 0;
    count2 = 0;
    correct2 = 0;
    accuracy2 = 0;
    count3 = 0;
    correct3 = 0;
    accuracy3 = 0;
    count4 = 0;
    correct4 = 0;
    accuracy4 = 0;
    count5 = 0;
    correct5 = 0;
    accuracy5 = 0;
    count6 = 0;
    correct6 = 0;
    accuracy6 = 0;
    count7 = 0;
    correct7 = 0;
    accuracy7 = 0;
    count8 = 0;
    correct8 = 0;
    accuracy8 = 0;
    count9 = 0;
    correct9 = 0;
    accuracy9 = 0;

    for data_test in data_testing:

        if DataSet_TESTING.print_label(data_test) == 0:
            count0 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct0 += 1
        elif DataSet_TESTING.print_label(data_test) == 1:
            count1 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct1 += 1
        elif DataSet_TESTING.print_label(data_test) == 2:
            count2 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct2 += 1
        elif DataSet_TESTING.print_label(data_test) == 3:
            count3 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct3 += 1
        elif DataSet_TESTING.print_label(data_test) == 4:
            count4 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct4 += 1
        elif DataSet_TESTING.print_label(data_test) == 5:
            count5 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct5 += 1
        elif DataSet_TESTING.print_label(data_test) == 6:
            count6 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct6 += 1
        elif DataSet_TESTING.print_label(data_test) == 7:
            count7 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct7 += 1
        elif DataSet_TESTING.print_label(data_test) == 8:
            count8 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct8 += 1
        elif DataSet_TESTING.print_label(data_test) == 9:
            count9 += 1
            if DataSet_TESTING.get_correct(data_test)==True:
                correct9 += 1
    accuracy0 = (correct0 / count0) * 100
    accuracy1 = (correct1 / count1) * 100
    accuracy2 = (correct2 / count2) * 100
    accuracy3 = (correct3 / count3) * 100
    accuracy4 = (correct4 / count4) * 100
    accuracy5 = (correct5 / count5) * 100
    accuracy6 = (correct6 / count6) * 100
    accuracy7 = (correct7 / count7) * 100
    accuracy8 = (correct8 / count8) * 100
    accuracy9 = (correct9 / count9) * 100

    print("Accuracy for Label 0 - {}".format(accuracy0))
    print("Accuracy for Label 1 - {}".format(accuracy1))
    print("Accuracy for Label 2 - {}".format(accuracy2))
    print("Accuracy for Label 3 - {}".format(accuracy3))
    print("Accuracy for Label 4 - {}".format(accuracy4))
    print("Accuracy for Label 5 - {}".format(accuracy5))
    print("Accuracy for Label 6 - {}".format(accuracy6))
    print("Accuracy for Label 7 - {}".format(accuracy7))
    print("Accuracy for Label 8 - {}".format(accuracy8))
    print("Accuracy for Label 9 - {}".format(accuracy9))


class DataSet_TRAINING:

    def __init__(self, data, label):
        self._data = data
        self._label = label

    def get_data(self):
        return self._data

    def set_distance(self, distance):
        self._distance = distance

    def print_label(self):
        return self._label

    def print_data_set(self):
        return self._data

    def print_distance(self):
        return self._distance

class DataSet_TESTING:

    def __init__(self, data, label):
        self._data = data
        self._label = label

    def get_data(self):
        return self._data

    def print_label(self):
        return self._label

    def print_data_set(self):
        return self._data

    def set_correct(self, isCorrect):
        self._isCorrect = isCorrect

    def get_correct(self):
        return self._isCorrect

def display_training_data():

    for train_data in data_training:
        print ("Label - " + DataSet_TRAINING.print_label(train_data))
        print (DataSet_TRAINING.print_data_set(train_data))
        # print(DataSet_TRAINING.print_distance(train_data))

def display_testing_data():

    for train_data in data_training:
        print ("Label - " + DataSet_TESTING.print_label(train_data))
        print (DataSet_TESTING.print_data_set(train_data))

def load_training_data(train_file):
    training_data_file = open(train_file, "r");

    x = 1;

    for line in training_data_file.readlines():
        # print(x)

        # ds = DataSet_TRAINING(line.split(",")[:-1], line.split(",")[-1])
        ds = DataSet_TRAINING([int(x) for x in line.split(",")[:-1]], int(line.split(",")[-1]))
        data_training.insert(x - 1, ds)
        x += 1

def load_testing_data(test_file):
    testing_data_file = open(test_file, "r");

    x = 1;

    for line in testing_data_file.readlines():
        # print(x)

        ds = DataSet_TESTING([int(x) for x in line.split(",")[:-1]], int(line.split(",")[-1]))
        data_testing.insert(x - 1, ds)
        x += 1

def workEuclidean(_element, _tempResult, _counterTRAIN, _counterTEST):
    if _element < len(DataSet_TESTING.get_data(data_testing[counterTEST]))-1:
        _tempResult += pow(((DataSet_TRAINING.get_data(data_training[_counterTRAIN])[_element]) -
                            (DataSet_TESTING.get_data(data_testing[_counterTEST])[_element])), 2)
        # print("pow((DataSet_TRAINING.get_data(data_training[{}][{}]".format(_counterTRAIN,_element))
        # print("- DataSet_TESTING.get_data(data_testing[{}])[{}]), 2)".format(_counterTEST, _element))
        return workEuclidean(_element+1, _tempResult, _counterTRAIN, _counterTEST)
    else:
        return _tempResult



def nearestNeighbourAlgorithm():
    for test_data in data_testing:
        counterTEST = data_testing.index(test_data)
        print("Test - {}".format(counterTEST))
        for train_data in data_training:
            counterTRAIN = data_training.index(train_data)
            # print("Counter Train - {}".format(counterTRAIN))
            element = 0
            temp_result = 0

            distance = [((DataSet_TRAINING.get_data(data_training[counterTRAIN])[i] -
                    DataSet_TESTING.get_data(data_testing[counterTEST])[i]) ** 2)
                  for i in range(len(DataSet_TESTING.get_data(data_testing[counterTEST])))]

            # l3 = [((l1[i] - l2[i]) ** 2) for i in range(len(l1))]
            distance = sum(distance) ** 0.5

            #distance = workEuclidean(element, temp_result, counterTRAIN, counterTEST)
            #distance = distance ** 0.5

            #print("Euclidean - {}".format(distance))
            DataSet_TRAINING.set_distance(data_training[counterTRAIN], distance)
            counterTRAIN += 1



        data_training.sort(key=lambda x: DataSet_TRAINING.print_distance(x))

        # print("Checking Test - {}".format(data_testing.index(test_data)))
        print("Training Distance Min - {}".format(DataSet_TRAINING.print_distance(data_training[0])))
        # print("Training Label - {}".format(DataSet_TRAINING.print_label(data_training[0])))
        # print("Testing Label - {}".format(DataSet_TESTING.print_label(test_data)))

        if (DataSet_TRAINING.print_label(data_training[0])) == (DataSet_TESTING.print_label(test_data)):
            DataSet_TESTING.set_correct(test_data, True)
            print("Correct")
        else:
            DataSet_TESTING.set_correct(test_data, False)
            print("Incorrect")

        counterTEST += 1

    test_size = len(data_testing)
    correct = 0

    for tests in data_testing:
        if DataSet_TESTING.get_correct(tests) == True:
            correct+=1

    print("Total number of tests taken - {}".format(test_size))
    print("Total number of Correct Recognition - {}".format(correct))
    accuracy = (correct/test_size)*100
    print("Accuracy for Nearest Neighbour - {}".format(accuracy))

    Results()





def kNearestNeighbourAlgorithm():
    global kValueList
    kValue = input('Enter k Value: ')

    for test_data in data_testing:

        counterTEST = data_testing.index(test_data)
        print("Test - {}".format(counterTEST))
        for train_data in data_training:
            counterTRAIN = data_training.index(train_data)
            # print("Counter Train - {}".format(counterTRAIN))
            element = 0
            temp_result = 0

            distance = [((DataSet_TRAINING.get_data(data_training[counterTRAIN])[i] -
                    DataSet_TESTING.get_data(data_testing[counterTEST])[i]) ** 2)
                  for i in range(len(DataSet_TESTING.get_data(data_testing[counterTEST])))]

            # l3 = [((l1[i] - l2[i]) ** 2) for i in range(len(l1))]
            distance = sum(distance) ** 0.5

            #distance = workEuclidean(element, temp_result, counterTRAIN, counterTEST)
            #distance = distance ** 0.5

            #print("Euclidean - {}".format(distance))
            DataSet_TRAINING.set_distance(data_training[counterTRAIN], distance)
            counterTRAIN += 1



        data_training.sort(key=lambda x: DataSet_TRAINING.print_distance(x))
        print("Training Distance Min - {}".format(DataSet_TRAINING.print_distance(data_training[0])))

        for x in range(0, int(kValue)):
            kValueList.insert(x, DataSet_TRAINING.print_label(data_training[x]))

        # print(len(kValueList))
        for kVal in kValueList:
            print(kVal)


        counter = Counter(kValueList)
        max_count = max(counter.values())
        mode = [k for k, v in counter.items() if v == max_count]

        if len(mode) > 1:
            kValueMode = mode[0]
            print("Mode is - {}".format(kValueMode))
        elif len(mode) == 1:
            kValueMode = mode[0]
            print("Mode is - {}".format(kValueMode))


        if DataSet_TESTING.print_label(test_data) == kValueMode:
            DataSet_TESTING.set_correct(test_data, True)
            print("Correct")
        else:
            DataSet_TESTING.set_correct(test_data, False)
            print("Incorrect")


        kValueList.clear()

        counterTEST += 1

    test_size = len(data_testing)
    correct = 0

    for tests in data_testing:
        if DataSet_TESTING.get_correct(tests) == True:
            correct += 1

    print("Total number of tests taken - {}".format(test_size))
    print("Total number of Correct Recognition - {}".format(correct))
    accuracy = (correct / test_size) * 100
    print("Accuracy for Nearest Neighbour - {}".format(accuracy))

    Results()






def kMeansAlgorithm():
    pass

def main(argv):
    # ds0 = DataSet_TRAINING([0, 1, 2, 3, 4,5], 0)
    # ds1 = DataSet_TRAINING([1,2,3,4,5], 1)
    # ds2 = DataSet_TRAINING([2,3,4,5,6], 2)

    # data_training.insert(0,ds0)
    # data_training.insert(1, ds1)
    # data_training.insert(2, ds2)

    # num = 20
    # test = 0
    # for train_index in data_training:
        # print(DataSet_TRAINING.get_data(data_training[counterTRAIN])[_element])
        # test += 1
        # print(data_training.index(train_index))
        # ds = DataSet_TRAINING.set_distance(train_index,num)
        # print("size")
        # print(len(DataSet_TRAINING.get_data(train_index)))
        # num-=1

    # display_training_data()

    # data_training.sort(key=lambda x: DataSet_TRAINING.print_distance(x))

    # load_training_data()
    # print("TRAINS")
    # display_training_data()
    # load_testing_data()
    # print("TEST")
    # display_testing_data()
    # nearestNeighbourAlgorithm()
    # nearestNeighbourAlgorithm()
    # kNearestNeighbourAlgorithm()

    # l3 = [((l1[i]-l2[i])**2) for i in range(len(l1))]

    # print (sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-file', help='path of test file', required=True)
    parser.add_argument('--train-file', help='path of train file', required=True)
    args = parser.parse_args()
    # print(args.test_file)
    # print(args.train_file)

    load_testing_data(args.test_file)
    load_training_data(args.train_file)

    nearestNeighbourAlgorithm()



if __name__ == "__main__":
    main(sys.argv[1:])












