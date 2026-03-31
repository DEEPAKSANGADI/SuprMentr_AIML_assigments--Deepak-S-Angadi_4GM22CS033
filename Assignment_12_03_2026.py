from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import pandas as pd

import matplotlib.pyplot as plt


data = {
    'Temperature': [25, 15, 30, 10, 28, 12, 22, 35, 18, 26],
    'Humidity': [60, 80, 50, 90, 55, 85, 65, 40, 75, 58],
    'Is_Raining': [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    'Play_Outside': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)


X = df[['Temperature', 'Humidity', 'Is_Raining']]
y = df['Play_Outside']

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X, y)

plt.figure(figsize=(15, 10))
plot_tree(tree, 
          feature_names=['Temperature', 'Humidity', 'Is_Raining'],
          class_names=['Don\'t Play', 'Play'],
          filled=True,
          rounded=True)
plt.title("Decision Tree: Should You Play Outside?")
plt.tight_layout()
plt.show()

test_case = [[25, 60, 0]]  # Temp: 25°C, Humidity: 60%, Not raining
prediction = tree.predict(test_case)
print(f"Prediction: {'Play Outside' if prediction[0] == 1 else 'Don\'t Play Outside'}")