import streamlit as st
import numpy as np 
import pickle


# st.title("hello world")

with open("iris_dataset.pkl",'rb') as f:
    model=pickle.load(f)

st.title("Iris Flower Prediction")   

sepal_length=st.slider("Sepal length(cm)",4.0,8.0)
sepal_width=st.slider("Sepal width(cm)",2.0,8.0)
petal_length=st.slider("Petal length(cm)",1.0,8.0)
petal_width=st.slider("Petal width(cm)",1.0,3.0)

#create button  
if st.button("prediction"):
    input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    prediction=model.predict(input_data)
    Species=['Iris-setosa','Iris-versicolor','Iris-virginica']
    st.success(f"Predicted Iris Species:{Species[prediction[0]]}")