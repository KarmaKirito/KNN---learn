# KNN---learn
This is a test of applying KNN method into AI after I learned KNN.
line explanations:
- all import lines: Import the libraries needed for the code, need to have all libraries downloaded
- "digits = datasets.load_digit()": this line is used to load and then store the information of the digits dataset in to the "digits" variable.
- "x = digit.data, y = digit.target": to store the feature data (x) and the target labels (y) in x and y variables.
- "x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)": Split x_test, y_test and x_train, y_train into training values and testing values. Test size is the amount of information in the database is used for training (In this case it is 20%).
- "best = 0, run = True": this line is used for later purposes of trying to find a model which has an accuracy of 1.0 (which means 100%). Run is used to keep the code keep running until a model with the max accuracy is made.
- "while run:" : Make a loop to find the best model. If there's no intention of finding the best model but just making the code works, there's no need to create a loop like in this code.
- "x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)" Split the data set again just so that every time the loop starts again, the data is trained differently so the outcome has a higher chance to be different from the previous model.
- "clf = KNeighborsClassifier(n_neighbors=9)" : This line is used to create a K Nearest Neighbor classifier and it's called "clf".
- "clf.fit(x_train, y_train)" : Fit the training datas and labels into the model.
- "y_pred = clf.predict(x_test)" :Get the predicted value, which is the result of the model given out so that later it is possible to measure the accuracy of the model.
- "acc = metrics.accuracy_score(y_test, y_pred)": measure the model's accuracy.
- "print(best)": print the best accuracy value, first value would be 0 but then will change to the first accuracy value after 1 run.
-     "if acc > 0.99:
        with open('digits.pickle', 'wb') as f:
            pickle.dump(clf, f)
        run = False" : These lines are used to store the model in the digits.pickle file if the accuracy of the file reaches higher than 0.99 and also stop the program from running, can change the acc to 1 in order to store a model with 100% accuracy.
- "    if acc > best:
        best = acc" : These lines are used to get the best value to equal to the accuracy value then print it out.
- "pickle_in = open('digits.pickle', 'rb')
clf = pickle.load(pickle_in)" : After finishing to getting a model with more than 99% accuracy, the model is opened and stored in pickle_in variable. Then the model is loaded with the pickle.load function and called 'clf'.
- "clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
acc = metrics.accuracy_score(y_test, y_pred)
print(acc)" These last lines are just used to create the model again and to use the previous model that has gotten the > 99% acc. if there's already a model, the loop 'while run' can be commented out since it's just used for training a model.
