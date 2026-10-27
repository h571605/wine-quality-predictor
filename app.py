
import pandas as pd
import gradio as gr

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the red wine dataset
url = (
    "https://archive.ics.uci.edu/ml/"
    "machine-learning-databases/wine-quality/"
    "winequality-red.csv"
)

df = pd.read_csv(url, sep=";")

# Separate input features and target
X = df.drop(columns=["quality"])
y = df["quality"]

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Test accuracy: {accuracy:.2%}")


# Predict wine quality
def predict_wine(
    fixed_acidity,
    volatile_acidity,
    citric_acid,
    residual_sugar,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    pH,
    sulphates,
    alcohol
):
    values = [[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
    ]]

    wine = pd.DataFrame(values, columns=X.columns)
    quality = int(model.predict(wine)[0])

    if quality <= 4:
        category = "Lower quality"
    elif quality <= 6:
        category = "Average quality"
    else:
        category = "Higher quality"

    return (
        f"Predicted quality score: {quality}/10\n"
        f"Category: {category}\n"
        f"Test accuracy: {accuracy:.1%}\n\n"
        "This is a prediction, not a guarantee."
    )


# Create the website
inputs = [
    gr.Number(label="Fixed acidity", value=7.4),
    gr.Number(label="Volatile acidity", value=0.70),
    gr.Number(label="Citric acid", value=0.00),
    gr.Number(label="Residual sugar", value=1.9),
    gr.Number(label="Chlorides", value=0.076),
    gr.Number(label="Free sulfur dioxide", value=11),
    gr.Number(label="Total sulfur dioxide", value=34),
    gr.Number(label="Density", value=0.9978),
    gr.Number(label="pH", value=3.51),
    gr.Number(label="Sulphates", value=0.56),
    gr.Number(label="Alcohol", value=9.4)
]

demo = gr.Interface(
    fn=predict_wine,
    inputs=inputs,
    outputs=gr.Textbox(label="Prediction"),
    title="Wine Quality Predictor",
    description=(
        "Enter the chemical measurements of red wine "
        "to predict its quality using machine learning."
    )
)

demo.launch()
