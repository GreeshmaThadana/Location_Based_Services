from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class = 'multinomial',penalty='l2', max_iter = 1000, C=10)
# rounded_dataset = np.array(rerun)
# print(type(rerun))

train = df.drop('Target', axis=1)
train.shape

test = df['Target']
test.shape
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.2)

X_train.shape

model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print(accuracy)


# Accuracy = 93. 95 %