# Fertilizer Recommendation System

**Case Study 142 | B.Tech CSE (2024-28) | Semester V | Machine Learning**

A machine learning project that recommends a fertilizer from soil and crop details. Six classification algorithms are compared, the best model is saved, and a Streamlit web app lets anyone get a recommendation.

**Live app:** https://fertilizer-recommender-ehxmrvtef6jmviguwwrcvf.streamlit.app/

---

## 1. What is in this project

```
Fertilizer Recommendation System/
├── COLAB.ipynb                 <- the notebook: data analysis, 6 models, comparison
├── Fertilizer Prediction.csv   <- the dataset (99 rows)
├── model.joblib                <- the trained model (Decision Tree pipeline)
├── columns.joblib              <- column names and model name used by the app
└── fertilizer-app/
    ├── app.py                  <- the Streamlit web app
    ├── requirements.txt        <- libraries needed to run the app
    ├── model.joblib            <- copy of the trained model
    └── columns.joblib          <- copy of the column info
```

The `.venv` folder (if present) is only the local Python environment. It is not part of the project and must never be uploaded or submitted.

---

## 2. About the dataset

- Source: Kaggle "Fertilizer Prediction" dataset
- 99 rows, 9 columns, no missing values, no duplicates
- Inputs: Temperature, Humidity, Moisture, Soil Type (5 types), Crop Type (11 types), Nitrogen, Phosphorus, Potassium
- Target: Fertilizer name (7 classes): Urea, DAP, 28-28, 14-35-14, 20-20, 17-17-17, 10-26-26
- **The dataset has no soil pH column.** pH is therefore not a model feature. The app shows a pH box because the case study asks for it, and it says clearly that pH is not used.

---

## 3. What the notebook does

1. Loads and cleans the data (fixes column names such as `Temparature` and `Phosphorous`).
2. Explores it: class counts, nutrient averages per fertilizer, box plots, correlation heatmap.
3. Splits the data 80/20 (stratified, `random_state=42`).
4. Builds one pipeline per model: one-hot encoding for soil and crop, scaling for numbers, then the classifier.
5. Trains and compares six algorithms: Logistic Regression, KNN, Decision Tree, Random Forest, SVM, Gradient Boosting.
6. Compares them with accuracy, precision, recall, F1 and confusion matrices.
7. Runs 5-fold cross-validation, because the test set has only 20 rows.
8. Studies feature importance with a Random Forest.
9. Saves the chosen model as `model.joblib`.

### Results (from the notebook)

| Model | Test accuracy | CV F1 (mean) |
|---|---|---|
| Decision Tree | 0.95 | **0.972** |
| Logistic Regression | 1.00 | 0.962 |
| Gradient Boosting | 0.95 | 0.942 |
| Random Forest | 1.00 | 0.935 |
| SVM | 1.00 | 0.846 |
| KNN | 0.90 | 0.724 |

- **Selected model:** Decision Tree, because it had the best cross-validation score.
- **Most important features:** Phosphorus, Nitrogen and Potassium, followed by Moisture, Temperature and Humidity. Soil and crop types have small influence.
- **Limitations:** only 99 rows, so results can change with a different split; no pH data; the model recommends a fertilizer type, not a quantity.

---

## 4. How to get the files

1. Download `Fertilizer_Recommendation_System.zip` (the submitted project).
2. Double-click it to unzip. You get the folder `Fertilizer Recommendation System`.
3. Open that folder. You should see the files listed in section 1.

---

## 5. Run the app on your computer (VS Code)

You need Python 3.12 installed. Check with `python3 --version`.

1. Open **VS Code**. Click **File > Open Folder** and choose the `fertilizer-app` folder.
2. Open the terminal: **Terminal > New Terminal**.
3. Create a virtual environment (first time only):
   - Mac / Linux: `python3 -m venv .venv`
   - Windows: `python -m venv .venv`
4. Activate it:
   - Mac / Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
5. Install the libraries (first time only): `pip install -r requirements.txt`
6. Start the app: `streamlit run app.py`
7. Your browser opens at `http://localhost:8501`. If not, open that address yourself.
8. To stop the app, click the terminal and press `Ctrl + C`.

**Important:** `requirements.txt` pins `scikit-learn==1.6.1`. The saved model only loads with that version. Do not change it.

---

## 6. How to use the app

1. Choose the **soil type** and **crop type**.
2. Enter **Nitrogen, Phosphorus, Potassium, Moisture, Temperature and Humidity**.
3. (Soil pH is shown for the brief but is not used by the model.)
4. Click **Recommend**. The app shows the recommended fertilizer and a probability table.

### Test cases to check it works

Leave Temperature = 30, Humidity = 60, pH = 6.5.

| Soil | Crop | N | P | K | Moisture | Expected |
|---|---|---|---|---|---|---|
| Sandy | Maize | 37 | 0 | 0 | 38 | Urea |
| Loamy | Sugarcane | 12 | 36 | 0 | 45 | DAP |
| Black | Cotton | 7 | 30 | 9 | 62 | 14-35-14 |
| Red | Tobacco | 22 | 20 | 0 | 34 | 28-28 |
| Sandy | Barley | 12 | 13 | 10 | 35 | 17-17-17 |
| Red | Cotton | 9 | 10 | 0 | 64 | 20-20 |
| Sandy | Barley | 5 | 15 | 18 | 47 | 10-26-26 |

A Decision Tree gives all-or-nothing probabilities, so the winner shows 1 and the others 0. This is normal.

### What the fertilizer names mean
The numbers are the percentage of **N-P-K** (nitrogen, phosphorus, potassium). For example 14-35-14 is 14% N, 35% P, 14% K. DAP is mainly phosphorus, and Urea is almost pure nitrogen.

---

## 7. Open and run the notebook

1. Go to colab.research.google.com and sign in.
2. **File > Upload notebook**, choose `COLAB.ipynb`.
3. Run the first cell and upload `Fertilizer Prediction.csv` when asked.
4. Use **Runtime > Run all**.

To retrain and replace the model, run the last cell. It downloads new `model.joblib` and `columns.joblib` files. Copy them into the `fertilizer-app` folder, replacing the old ones.

---

## 8. Deploy online (Streamlit Community Cloud)

1. Create a **Public** repository on github.com, for example `fertilizer-recommender`.
2. Upload only these 4 files: `app.py`, `requirements.txt`, `model.joblib`, `columns.joblib`. **Do not upload the `.venv` folder.**
3. Go to share.streamlit.io and sign in with GitHub.
4. Click **Create app**, choose the repository, branch `main`, main file `app.py`.
5. Open **Advanced settings** and set Python to **3.12**.
6. Click **Deploy** and wait a few minutes.

Free apps go to sleep after a few days without visitors. If you see "Yes, get this app back up", click it and wait a minute.

---

## 9. How to submit

Submit these:
1. The notebook (`COLAB.ipynb`, or a Colab share link set to "Anyone with the link can view").
2. The live app link (section at the top of this file).
3. The project zip, **without** the `.venv` folder.
4. This README.

Before submitting, check that:
- The notebook runs from top to bottom with no red errors.
- The live app returns the expected answers for the test cases in section 6.
- The app link opens in a private/incognito window.

---

## 10. Common problems

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` with the virtual environment active |
| Model fails to load | scikit-learn version is not 1.6.1. Reinstall with `pip install scikit-learn==1.6.1` |
| `streamlit: command not found` | Activate the virtual environment (section 5, step 4) |
| Deploy fails on Streamlit Cloud | Check that the repo has exactly the 4 files and that `requirements.txt` has no typos |
| App page is asleep | Click "Yes, get this app back up" |

---

## 11. Technologies used

Python 3.12, pandas, scikit-learn, joblib, matplotlib, seaborn, Streamlit, Google Colab, GitHub.
