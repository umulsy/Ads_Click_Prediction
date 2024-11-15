# -*- coding: utf-8 -*-
"""ads click prediction-umul syarifah

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LlhwBepVpOlCvGGsSPlYkAbq-M8LtqL-

# Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# %matplotlib inline

"""#Loading Dataset"""

df = pd.read_csv('https://raw.githubusercontent.com/umulsy/Ads_Click_Prediction/refs/heads/main/ads_dataset.csv')
df.head()

df.info()

"""Terdapat 6 data bertipe object berarti terdapat 6 categorical feature. 2 bertipe angka atau integer (int) 1 bertipe desimal (float)

<div class="alert alert-success" style="background-color: #f5e6c8; border-color: #e0c097; padding: 20px;">
    <h1 align="center" style="color:black; font-size: 28px; font-family: Arial, sans-serif; margin-bottom: 10px;">Exploratory Data Analysis
    </h1>
</div>
"""

df = df.drop(columns=['id'])

df.describe(include='all')

categorical_columns = df.select_dtypes(include=['object']).columns
unique_values = {col: df[col].nunique() for col in categorical_columns}
for col, unique_count in unique_values.items():
        print(f"{col}: {unique_count} unique values")
        print(df[col].unique(), "\n")

missing_df = df.isna().mean() * 100
missing_df = missing_df[missing_df > 5].sort_values(ascending=False)
print("Columns with more than 5% missing values:")
print(missing_df)

import plotly.express as px
def plot_pie_chart(df, column_name):
    value_counts = df[column_name].value_counts(dropna=False)
    value_counts = value_counts.reset_index()
    value_counts.columns = [column_name, 'count']

    fig = px.pie(value_counts, names=column_name, values='count',
                 title=f'{column_name} Distribution (Including Unknown)',
                 color_discrete_sequence=px.colors.qualitative.T10,
                 hole=0.4)

    fig.update_traces(textinfo='percent+label')

    fig.update_layout(title_x=0.5)

    fig.show()

categorical_columns = df.select_dtypes(include=['object']).columns
categorical_columns = categorical_columns.drop('full_name', errors='ignore')
for col in categorical_columns:
    plot_pie_chart(df, col)

# Cek duplikasi
duplicate_rows = df[df.duplicated()]
print("Jumlah baris duplikat:", len(duplicate_rows))

"""<div style="border-radius:10px; border:#e0c097 solid 2px; padding: 15px; background-color: white; font-size:100%; text-align:left"> <h3 align="center" style="color: #d4a017;">Data Cleaning</h3>

- The proportion of recurring users and first-time users among the 4,000 unique users was analyzed.
- First-time users consist of 3,500 individuals, each contributing one record, none of whom clicked on the ads.
- Recurring users include 500 individuals who collectively contributed 6,500 records, and all of these users clicked on the ads.
"""

df_type_user = df.copy()
user_counts = df_type_user['full_name'].value_counts()

df_type_user['user_type'] = df_type_user['full_name'].apply(lambda x: 'First Time Users' if user_counts[x] == 1 else 'Recurring Users')

recurring_users = df_type_user[df_type_user.duplicated(subset=['full_name'], keep=False)]
first_time_users = df_type_user.drop_duplicates(subset=['full_name'], keep=False)

recurring_users.describe(include='all')

first_time_users.describe(include='all')

feature_counts = df_type_user.groupby(['user_type', 'click']).size().reset_index(name='count')

feature_counts['click'] = feature_counts['click'].map({0: 'No Click', 1: 'Click'})

fig = px.bar(feature_counts,
             x='user_type', y='count', color='click',
             title='Ad Clicks by User Type (First Time vs Recurring)',
             labels={"user_type": "User Type", "count": "Number of Clicks", "click": "Click Status"},
             color_discrete_sequence=px.colors.qualitative.T10,
             text='count',
             barmode="group")

fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    title_x=0.5,
    xaxis_title="User Type",
    yaxis_title="Number of Clicks",
    legend_title="Click Status",
    bargap=0.5,
    bargroupgap=0.1
)

fig.show()

recurring_users.sort_values(by='full_name', ascending=True).head(30)

df.update(df.groupby('full_name').transform(lambda x: x.ffill().bfill()))
df = df.drop(columns=['full_name'])

"""<div style="border-radius:10px; border:#e0c097 solid 2px; padding: 15px; background-color: white; font-size:100%; text-align:left">

<h3 align="center" style="color: #d4a017;">Handling Other Missing Values</h3>

- An "Unknown" category was introduced to handle missing values.
- Imputation methods such as mode, mean, or random filling based on the original distribution were deliberately avoided.
- This approach prevents over-analyzing the original data while preserving the information carried by missing values.
- Additionally, it helps mitigate model bias and reduces the risk of overfitting.

"""

for col in df.select_dtypes(include='object').columns:
    df[col].fillna('Unknown', inplace=True)

from sklearn.impute import KNNImputer
import pandas as pd
def knn_impute(df, n_neighbors=5):
    df_encoded = df.copy()

    category_mappings = {}
    for col in df_encoded.select_dtypes(include='object').columns:
        df_encoded[col] = df_encoded[col].astype('category').cat.codes
        category_mappings[col] = dict(enumerate(df[col].astype('category').cat.categories))


    knn_imputer = KNNImputer(n_neighbors=n_neighbors)
    df_imputed = pd.DataFrame(knn_imputer.fit_transform(df_encoded), columns=df_encoded.columns)


    for col in df.select_dtypes(include='object').columns:
        df_imputed[col] = df_imputed[col].round().astype(int).map(category_mappings[col])

    return df_imputed

df_imputed = knn_impute(df, n_neighbors=5)


df = df_imputed

print(df.isna().sum())

"""<div class="alert alert-success" style="background-color: #f5e6c8; border-color: #e0c097; padding: 20px;">
    <h1 align="center" style="color:black; font-size: 28px; font-family: Arial, sans-serif; margin-bottom: 10px;">Data Visualization
    </h1>
</div>
"""

age_bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
age_labels = ['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64']
df_visualization = df.copy()
df_visualization['age_group'] = pd.cut(df_visualization['age'], bins=age_bins, labels=age_labels, right=False)


click_counts = df_visualization.groupby(['age_group', 'click']).size().reset_index(name='count')

click_counts['click'] = click_counts['click'].map({0: 'No Click', 1: 'Click'})

fig = px.bar(
    click_counts,
    x='age_group',
    y='count',
    color='click',
    title='Age Group Distribution of Clicks vs No Clicks',
    labels={'age_group': 'Age group', 'count': 'Count', 'click': 'Click Status'},
    text='count',
    color_discrete_sequence=px.colors.qualitative.T10,
    category_orders={'age_group': age_labels}
)

fig.update_layout(
    barmode='stack',
    xaxis_title='Age group',
    yaxis_title='Count',
    legend_title='Click Status',
    title_x=0.5
)

fig.show()

feature_counts = df.groupby([df['click'].map({1: 'Click', 0: 'No Click'}), 'ad_position']).size().reset_index(name='count')

total_count = feature_counts['count'].sum()
feature_counts['percent'] = feature_counts['count'] / total_count * 100

fig = px.sunburst(feature_counts, path=['click', 'ad_position'], values='count',
                 color='count', color_continuous_scale='Teal',
                 title='Ad Clicks by Ad position')

fig.update_traces(
    textinfo='label+percent entry',
    texttemplate='<b>%{label}</b><br>%{percentEntry:.2%}'
)

fig.update_layout(title_text='Ad Clicks by Ad position',
                  title_x=0.5, width=900, height=600)

fig.show()

feature_counts = df.groupby([df['click'].map({1: 'Click', 0: 'No Click'}), 'time_of_day']).size().reset_index(name='count')

total_count = feature_counts['count'].sum()
feature_counts['percent'] = feature_counts['count'] / total_count * 100

fig = px.sunburst(feature_counts, path=['click', 'time_of_day'], values='count',
                 color='count', color_continuous_scale='Teal',
                 title='Ad Clicks by time_of_day')

fig.update_traces(
    textinfo='label+percent entry',
    texttemplate='<b>%{label}</b><br>%{percentEntry:.2%}'
)

fig.update_layout(title_text='Ad Clicks by Time of Day ',
                  title_x=0.5, width=900, height=600)

fig.show()

feature_counts = df.groupby(['device_type', 'ad_position'])['click'].size().reset_index(name='click')
fig = px.bar(feature_counts,
             x='device_type', y='click', color='ad_position',
             title='Ad Clicks by Device Type and Ad Position',
             labels={"device_type": "Device Type", "click": "Number of Clicks", "ad_position": "Ad Position"},
             color_discrete_sequence=px.colors.qualitative.T10,
             text='click',
             barmode="group")
fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    title_x=0.5,
    xaxis_title="Device Type",
    yaxis_title="Number of Clicks",
    legend_title="Ad Position",
    bargap=0.5,
    bargroupgap=0.1
)

fig.show()

!pip install dython

from dython.nominal import associations
associations_df = associations(df, nominal_columns='all', plot=False)

corr_matrix = associations_df['corr']

plt.figure(figsize=(20, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix including Categorical Features')
plt.show()

"""<div class="alert alert-success" style="background-color: #f5e6c8; border-color: #e0c097; padding: 20px;">
    <h1 align="center" style="color:black; font-size: 28px; font-family: Arial, sans-serif; margin-bottom: 10px;">Model Building & Training
    </h1>
</div>
"""

from sklearn.preprocessing import OneHotEncoder

# Misal `df` adalah DataFrame kita
# Identifikasi kolom bertipe `object`
object_columns = df.select_dtypes(include='object').columns

# Inisialisasi OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# Terapkan OneHotEncoder pada kolom bertipe object
encoded_data = encoder.fit_transform(df[object_columns])

# Membuat DataFrame hasil encoding dengan nama kolom baru yang sesuai
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(object_columns))

# Menggabungkan hasil encoding dengan kolom numerik lainnya
df_final = pd.concat([df.drop(columns=object_columns).reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Tampilkan DataFrame hasil
print(df_final.head())

from sklearn.model_selection import train_test_split

X = df_final.drop('click', axis=1)
y = df_final['click']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=94)

from sklearn.neighbors import KNeighborsClassifier # Import the classifier instead of regressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
# Create a pipeline to combine preprocessing and model training
# Initialize and train K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

# Make predictions on the test data
y_predKNN = knn.predict(X_test)

# Calculate and print accuracy
accuracyKNN = accuracy_score(y_test, y_predKNN)
print(f'Accuracy: {accuracyKNN:.2f}')

y_test = y_test.astype(int)
y_predKNN = y_predKNN.astype(int)

from sklearn.metrics import confusion_matrix

# Membuat confusion matrix
conf_matrix = confusion_matrix(y_test, y_predKNN)

# Menampilkan confusion matrix dengan seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for KNN Model')
plt.show()

# Build Model Random Forest
from sklearn.ensemble import RandomForestClassifier # Import RandomForestClassifier

# buat model prediksi
RF = RandomForestClassifier(n_estimators=50, max_depth=16, random_state=50, n_jobs=-1)# Change to Classifier
RF.fit(X_train, y_train)

# make prediction
y_predRF = RF.predict(X_test)

#cek akurasi
accuracyRF = accuracy_score(y_test, y_predRF)
print(f'Accuracy: {accuracyRF:.2f}')

# Membuat confusion matrix
conf_matrix = confusion_matrix(y_test, y_predRF)

# Menampilkan confusion matrix dengan seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for Random Forest Model')
plt.show()

# Build model Xgboost
import xgboost as xgb

# buat model prediksi
xgb_model = xgb.XGBClassifier(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1) # Change to Classifier
xgb_model.fit(X_train, y_train)

# make prediction
y_predXGB = xgb_model.predict(X_test)

#cek akurasi
accuracyXGB = accuracy_score(y_test, y_predXGB)
print(f'Accuracy: {accuracyXGB:.2f}')

# evaluate model
xgb_model.score(X_test, y_test)

from sklearn.metrics import classification_report, confusion_matrix

print("Classification Report:\n", classification_report(y_test, y_predXGB))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_predXGB))
# Membuat confusion matrix
conf_matrix = confusion_matrix(y_test, y_predXGB)

# Menampilkan confusion matrix dengan seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for XGB Model')
plt.show()

# Model Comparison
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
models = {"KNN": KNeighborsClassifier(),
          "Random Forest": RandomForestClassifier(),
          "XGBoost": xgb.XGBClassifier()}

# function to fit and score models

def fit_and_score(models, X_train, X_test, y_train, y_test):
    np.random.seed(42)
    model_scores = {}
    for name, model in models.items():
        #fit the model
        model.fit(X_train, y_train)
        #append the score of the model
        model_scores[name] = model.score(X_test, y_test)
    return model_scores

model_scores = fit_and_score(models=models,
                             X_train = X_train,
                             X_test = X_test,
                             y_train = y_train,
                             y_test = y_test)
model_scores

model_compare = pd.DataFrame(model_scores, index=["accuracy", 'precission', 'f1 score', 'recall'])
model_compare

model_compare.T.plot.bar()

#set train size
#316 x 80% = 252 (20% for validation)
train_sizes = [1, 20, 40, 50, 100, 150, 252]

!pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import learning_curve

def learn_curve_plot(estimator, x, y, cv, train_sizes):
  train_sizes, train_scores, validation_scores = learning_curve(estimator,X=X,y=y, train_sizes= train_sizes, cv=cv)
  train_scores_mean = train_scores.mean(axis=1)
  validation_scores_mean = validation_scores.mean(axis=1)

  #Print
  print('Mean training scores\n\n', pd.Series(train_scores_mean, index=train_sizes))
  print('\n', '-' * 20) # separator
  print('\nMean validation scores\n\n',pd.Series(validation_scores_mean, index=train_sizes))

  # Use seaborn style.
  # Use sns.set_theme() instead of plt.style.use('seaborn')
  sns.set_theme()
  # sns.set_style("whitegrid")  # Alternatively, you can use sns.set_style to set a specific seaborn style before plotting.

  plt.plot(train_sizes, train_scores_mean, label = 'Training error')
  plt.plot(train_sizes, validation_scores_mean, label = 'Validation error')
  plt.ylabel('Accuracy', fontsize = 14)
  plt.xlabel('Training set size', fontsize = 14)
  plt.title('Learning Curve', fontsize = 18, y = 1.03)
  plt.legend()

# Learning Curve KNN
learn_curve_plot(estimator=knn, x=X, y=y, cv=5, train_sizes=train_sizes)

# Learning Curve Random Forest
learn_curve_plot(estimator=RF, x=X, y=y, cv=5, train_sizes=train_sizes)

# Learning Curve Xgboost
learn_curve_plot(estimator=xgb_model, x=X, y=y, cv=5, train_sizes=train_sizes)

df_final.head()

df_final.isna().sum()