from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd
import joblib as jb
import os

# Loading the cleaned dataset
clean_csv_path = os.path.join("..", "data", "USvideos_clean.csv")
df = pd.read_csv(clean_csv_path)

# Adding new features based on channel statistics so that the model can predict more accurately
# Mean views per channel
df['channel_mean_views'] = df.groupby('channel_title')['views'].transform('mean')
# Mean likes per channel
df['channel_mean_likes'] = df.groupby('channel_title')['likes'].transform('mean')

# Extracting time-based features from 'publish_time'
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_day_of_week'] = df['publish_time'].dt.dayofweek
df['publish_month'] = df['publish_time'].dt.month

# Creating ratio features
# Ratio of comments to views
df['comments_to_views'] = df['comment_count'] / (df['views'] + 1)
# Ratio of dislikes to likes
df['dislikes_to_likes'] = df['dislikes'] / (df['likes'] + 1)

# Mean views per category
df['category_mean_views'] = df.groupby('category_id')['views'].transform('mean')
# Relative views compared to category mean
df['relative_views'] = df['views'] / (df['category_mean_views'] + 1)

# Defining features and target variable
features = [
    'views', 'category_id',
    'channel_mean_views', 'channel_mean_likes',
    'publish_hour', 'publish_day_of_week', 'publish_month',
    'comments_to_views', 'dislikes_to_likes', 'category_mean_views',
    'relative_views'
]

# Preparing data for modeling
X = df[features].fillna(0)
y = df['likes']

# Splitting data into training and validation sets
train_X, val_X, train_Y, val_Y = train_test_split(X, y, random_state=42)

# Initializing and training the Random Forest model
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)
model.fit(train_X, train_Y)

# Evaluating model performance
val_predictions = model.predict(val_X)
mae = mean_absolute_error((val_Y), val_predictions)
print("MAE:", mae)

# Comparing real values with predictions
for i in range(10):

    print("video number",i+1,"likes predicted:", model.predict(val_X.head(i+1))[-1].round(), "real likes:", val_Y.iloc[i])

# Saving the trained model
model_path = os.path.join("..", "models", "random_forest_likes_model.joblib")

jb.dump({"model": model, "features": features}, model_path)

print(f"Model saved to {model_path}")