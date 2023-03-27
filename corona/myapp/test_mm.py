import joblib
import numpy as np

# Load the saved model
model = joblib.load('model_cov.pkl')

# Reshape the input data
X = np.array([[11, -0.1525904834270477, 0.4162521064281464, -0.2159295827150345,
       1.693574905395508, 0.8777399659156799, 1.785361289978027,
       2.235712289810181, -0.5537709593772888, 1.914446830749512,
       -0.8672572374343872, 0.2179767936468124, -1.956940174102783,
       0.7252317070960999, 0.0825793221592903,1]])

# Use the loaded model for prediction
y_pred = model.predict(X)

print(y_pred)
