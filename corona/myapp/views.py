from django.shortcuts import render
import joblib
import numpy as np
import os

# Create your views here.

def html_1(request):
    return render(request,"home.html")

def html_2(request):
    return render(request,"predict.html")

def read(request):
    # get the absolute path to the file
    #file_path = os.path.abspath('model_covid.pkl')
    # Load the saved model
    model = joblib.load("model")
    if request.method == 'POST':
        # Get the form data
        platelets = float(request.POST.get('input1'))
        leukocytes = float(request.POST.get('input2'))
        eosinophils = float(request.POST.get('input3'))
        monocytes = float(request.POST.get('input4'))
        est_malade = bool(request.POST.get('input5'))

        # Reshape the input data
        X=np.array([[18, 1.358054995536804, 1.356091856956482, platelets,
        -0.4380969405174255, 1.142195582389832, -0.5174806714057922,
        0.2441485673189163, leukocytes, -0.2237665057182312,
        0.1781749874353409, eosinophils, 0.0660446211695671,
        monocytes, -0.0058774976059794, est_malade]])

        X_2d = X.reshape(1, -1)
        # Use the loaded model for prediction
        y_pred = model.predict(X_2d)

        # Return the prediction as a response
        if y_pred==0:
            result="your test is negative"
        else:
            result="your test is positive"
        return render(request, 'predict2.html', {'result': result})




