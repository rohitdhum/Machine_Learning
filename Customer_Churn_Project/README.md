# Customer Churn Prediction using Machine Learning

## Project Description
This project predicts whether a customer is likely to leave a company or continue using its services. It uses Machine Learning with Logistic Regression to make predictions based on customer details.

A Streamlit dashboard is developed to make the project simple and easy to use. Users can enter customer information and get the churn prediction instantly.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning (Logistic Regression)

## Input Features
The model uses the following customer details:

- **Age:** Age of the customer.
- **Tenure:** Number of months the customer has stayed with the company.
- **Monthly Charges:** Monthly amount charged to the customer.
- **Support Calls:** Number of customer support calls.

## Project Structure

Customer_Churn_Project/
│
├── Dashboard_Customer_Churn.py
├── ML_Customer_ChurnX_Final.py
├── customer_churn.csv
├── Marvellous_ML_Customer_Churn.pkl
├── requirements.txt
└── README.md

Note: The actual filenames may differ. The deployed dashboard requires `app.py`, the trained model file, and `requirements.txt`. The training script and dataset are needed only if you want to retrain the model.

## How It Works
1. The customer dataset is loaded using Pandas.
2. The required input features and target variable are selected.
3. The dataset is divided into training and testing data.
4. Logistic Regression is trained using the training data.
5. The model is evaluated using accuracy and a confusion matrix.
6. The trained model is saved as a `.pkl` file using Joblib.
7. The Streamlit dashboard loads the saved model.
8. Users enter customer details and click the **Predict Churn** button.
9. The dashboard displays whether the customer is likely or unlikely to churn.

## How to Run the Project

### 1. Install the Required Libraries

pip install -r requirements.txt

### 2. Train the Machine Learning Model

Run the training script to generate the saved model:

python ML_Customer_ChurnX_Final.py

### 3. Run the Streamlit Dashboard

streamlit run Dashboard_Customer_Churn.py

The dashboard will open in your web browser.

## Prediction Output
The dashboard displays one of the following messages:

- **Customer is likely to churn**
- **Customer is unlikely to churn**

The prediction depends on the customer information entered by the user and the patterns learned by the trained model.

## Deployment
The application can be deployed using Streamlit Community Cloud and connected to a GitHub repository. Once deployed, users can access the dashboard through a public web link without running the application on their own computers.

## Future Improvements
- Improve model accuracy through feature engineering and model comparison.
- Display additional evaluation metrics such as precision, recall, and F1-score.
- Add visualizations for customer churn analysis.
- Improve the dashboard design and user experience.

## Conclusion
This project demonstrates how Machine Learning can be used to predict customer churn. It combines Logistic Regression with a Streamlit dashboard to provide a simple, interactive application for customer churn prediction.