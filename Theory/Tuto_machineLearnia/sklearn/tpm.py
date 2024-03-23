#On commence par importer le dataset du titanic à l'aide de pandas
import pandas as pd
titanic = pd.read_excel('../Datasets/titanic.xls')
#On vérifie que l'importation est bien réussie
titanic.head()
#On supprime les valeurs NaN et on transforme les informations textuels en infos numériques
titanic = titanic[['survived','pclass','sex','age']]
titanic.dropna(axis=0,inplace=True)
titanic['sex'].replace(['male','female'],[0,1],inplace=True)
titanic.head()
# On crée les test et train sets
y = titanic['survived']
X = titanic.drop(['survived'],axis=1)
print(X['pclass'].shape)
# Ici notre étiquette est la survie du passager ou non (0 ou 1), il s'agira donc d'annoter les observations en fonction des caractéristiques pclass, age, sex
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=5)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Score : "+str(knn.score(X_test,y_test)))
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Création de la grille de subplots 3D
plt.figure(figsize=(30, 10))
plt.subplot(141, projection='3d')  # 1 ligne, 4 colonnes, subplot 1
plt.scatter(X['pclass'], X['sex'],X['age'],c=y, cmap='plasma',linewidths=1, alpha=0.5)
plt.title("Set")
plt.subplot(142, projection='3d')  # 1 ligne, 4 colonnes, subplot 2
plt.scatter(X_train['pclass'], X_train['sex'],X_train['age'],c=y_train)
plt.title("Train Set")
plt.subplot(143, projection='3d')  # 1 ligne, 4 colonnes, subplot 3
plt.scatter(X_test['pclass'], X_test['sex'],X_test['age'],c=y_test)
plt.title("Test Set")
plt.subplot(144, projection='3d')  # 1 ligne, 4 colonnes, subplot 3
plt.scatter(X_test['pclass'], X_test['sex'],X_test['age'],c=y_pred)
plt.title("Estimated Survival")
plt.show()
