# YouTube Data Analysis

## Overview
This project performs an **exploratory data analysis (EDA)** of YouTube trending videos in the US.  
Using Python and popular libraries such as Pandas, NumPy, Matplotlib, and Seaborn, we clean, preprocess, and visualize the dataset to extract meaningful insights about video performance, trends, and user engagement.

The analysis includes:
- Average and total views per category
- Likes, dislikes, and comment ratios
- Trends over time
- Correlation between key metrics

---

## Dataset
The dataset used in this project is from Kaggle: [YouTube Trending Videos](https://www.kaggle.com/datasnaek/youtube-new).  

**Note:** The CSV files are **not included** in this repository due to size constraints. Please download the dataset manually and place it in the `data/` folder:

---

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/DiegoAladren/youtube-data-analysis.git
cd youtube-data-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
Install required packages:
pip install -r requirements.txt
```

---

## Usage

### Data Cleaning

Run the 01_data_cleaning.ipynb notebook or src/data_preprocessing.py to:
- Remove duplicates and null values
- Convert date columns
- Map category IDs to category names
- Compute interaction ratios (like_ratio, comment_ratio)

This will generate a cleaned dataset.

### Exploratory Data Analysis

Run the 02_eda.ipynb notebook to explore:
- Views
- Interaction
- Dates and times

Visualizations include:
- Horizontal bar plots
- Histograms
- Correlation heatmaps
- Pie charts

## License

This project is for educational purposes. Please check the original dataset license on Kaggle.

## Contact

For questions or feedback, contact: diegoaladren854@gmail.com

LinkedIn: www.linkedin.com/in/diego-aladrén-mateo-7a6034307
