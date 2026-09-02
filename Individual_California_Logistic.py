import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

#----------------------------------------------
# Step 1 : Load the data
#----------------------------------------------

df = pd.read_csv("california_housing.csv")
print("Shape of Datset :", df.shape)
print("Fisrt few records :", df.head())

#----------------------------------------------
# Step 2 : Convert target into classes
#----------------------------------------------

meadian_value = df['target'].median()

# If target is greater than or equal to median -> 1
# Otherwise -> 0
df['target_class'] = (df['target'] >= meadian_value).astype(int)

print("\nMedian target value :", meadian_value)
print("\nTarget Class :")
print(df["target_class"].value_counts())


#----------------------------------------------
# Step 2 : Separate features and labels
#----------------------------------------------

X = df.drop(["target", "target_class"], axis=1)
Y = df["target_class"]

print("\nShape of X :", X.shape)
print("Shape of Y :", Y.shape)

#----------------------------------------------
# Step 3 : Split Dataset for training and Testing
#----------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data :", X_test.shape)

#----------------------------------------------
# Step 4 : Create the model
#----------------------------------------------

model = LogisticRegression(
    max_iter=1000,
    random_state=42
    )

#----------------------------------------------
# Step 5 : Train the model
#----------------------------------------------

model = model.fit(X_train, Y_train)

#----------------------------------------------
# Step 6 : Test the model
#----------------------------------------------

Y_pred = model.predict(X_test)

#----------------------------------------------
# Step 7 : Evaluate the model
#----------------------------------------------

print("MSE :", mean_squared_error(Y_test, Y_pred))
print("R2 :", r2_score(Y_test, Y_pred))