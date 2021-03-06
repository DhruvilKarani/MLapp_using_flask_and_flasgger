# ML_app_using_flask_and_flasgger

Deploying ML models as flask apps and creating UI using flasgger

rf.py -> saving a random forest model as a pickle file

autogenerating_UI_flasgger.py -> building app to deploy the Random Forest model and creating a UI around it


Building an ML model
Before we deploy any model, let’s first build one. For now, let’s build a simple model on a simple dataset so that we can spend more time on the deployment part. We will use the Iris dataset from sklearn’s datasets. The required imports are given in the code.


The variable to be predicted, i.e. Species, has thee categories - Setosa, Virginica, Versicolour.

http://www.analyticskhoj.com/wp-content/uploads/2015/04/IRIS-Dataset.jpg


The model we build is saved as a pickle file. A pickle file saves any file into its binary form. Next time we want to use this model, we don’t have to train it again. We can simply load this pickle file.



Next, we create a Flask object and name it app. The argument to this Flask object will be the special keyword __name__. To create an easy UI for this app, we use Swagger module in Flasgger library.



Now, we create two apps - One which accepts individual values for all 4 input values and the other which accepts a CSV file as inputs. The first line @app.route(‘/predict’) specifies the part of the URL which will run this particular app. The next thing we do is create a function, named predict_iris. Under this function, we have a long docstring. This string is actually used by the Swagger for creating a UI. It says that the app requires 4 parameters namely S_length, S_width, P_length, P_width. All of these input values are of query type. Next, the app uses GET method to accept these values. This just means that we need to enter the numbers by ourselves. Then we pass these values to our model in a 2 D numpy array and return the predictions. Two things here - 
Predictions[0] returns the element in the prediction numpy array
We always output a string, never a numeric value to avoid errors.

Now we build the second app, the one that accepts file. But before the app, we create a file that has all four variable values for which we will predict output. In the Python console, type the following


Select any 2-4 rows at random, copy them and save them in a csv file. We use this file to test our second app. 

Notice the changes here. The @app.route decorator has ‘/predict_file’ as one of its argument. The docstring under our new function predict_iris_file tells Swagger to set file as input file. Next, we read the CSV using read_csv and make sure the header is set to None if you haven’t set the column names while making the CSV. Next, we use the model to make the predictions and return them as a string.



Copy the URL (the one highlighted) and paste it in your browser. Add /apidocs to it and hit Enter. For example: http://127.0.0.1:5000/apidocs. 

UI for your first app is created. Go ahead, insert the four values and click on ‘Try it out!’.  Under the response body, you will find the predicted class. For our second app, upload the file by clicking on choose file.


When you try it out, you will get a string of predicted classes. 

Congratulations! You have just created a nice UI for your ML model. Feel free to play around and try out new things.

