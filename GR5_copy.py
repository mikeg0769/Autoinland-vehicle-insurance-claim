import pandas as pd
import numpy as np
import streamlit as st
import joblib
from os.path import dirname, join, realpath
from PIL import Image


st.header('AUTOINLAND INSURANCE CLAIM CHALLENGE')

#Add image
image = Image.open('/home/arc/Desktop/ML_Bootcamp/week_6/2_wednesday/insurance2.jpg')
st.image(image, caption='Auto Insurance', width=680)

st.subheader("""A model to predict if a customer will submit a vehicle insuarance claims in next three months""")

#Form to collect customers information
Form = st.form(key= "Customers_form")

Gender_ext = Form.selectbox("Gender", ("Female","Male","Other"))
Age = Form.number_input("Age", min_value=1,max_value=200)
State_ext = Form.selectbox("State", ("Lagos","Benue","Other","Abuja-Municipal","Eti-Osa","Ibeju-Lekki","Ogun"))
ProductName = Form.selectbox("Name of the product",("Car Classic","CarSafe","Customized Motor","Car Plus","Other"))
Car_Category_ext = Form.selectbox("Vehicle Category", ("Saloon","JEEP","Truck","Other"))
Car_Make_ext = Form.selectbox("Brand of Vehicle", ("TOYOTA","Honda","Other","Lexus","Mercedes","Hyundai"))
Car_Colour_ext = Form.selectbox("Color of the Vehicle", ("Black","Silver","Grey","As Attached","Other"))
No_Pol = (Form.number_input("Number of Policies", min_value=1,max_value=7))
Policy_Duration  = Form.number_input("Policy Duration (Days)?", min_value=16,max_value=11108)

submit = Form.form_submit_button(label="make prediction")


#loading the model
with open(join(dirname(realpath(__file__)), "/home/arc/Desktop/ML_Bootcamp/week_5/1_Monday_5/notebook/hgbc_model.pkl"),"rb",) as e:
    model = joblib.load(e)






if submit:
    #Gender_ext
    if Gender_ext == "Female":
        Gender_ext_Female = 1
        Gender_ext_Male = Gender_ext_Other = 0
    elif Gender_ext == "Male":
        Gender_ext_Female = Gender_ext_Other = 0
        Gender_ext_Male = 1
    else:
        Gender_ext_Female = Gender_ext_Male = 0
        Gender_ext_Other = 1

    #Car_Category
    if Car_Category_ext == "Saloon":
        Car_Category_ext_Other = Car_Category_ext_JEEP = Car_Category_ext_Truck = 0
        Car_Category_ext_Saloon = 1
    elif Car_Category_ext == "JEEP":
        Car_Category_ext_Other = Car_Category_ext_Saloon = Car_Category_ext_Truck = 0
        Car_Category_ext_JEEP = 1
    elif Car_Category_ext == "Truck":
        Car_Category_ext_Other = Car_Category_ext_JEEP = Car_Category_ext_Saloon = 0
        Car_Category_ext_Truck = 1
    else:
        Car_Category_ext_Other = 1
        Car_Category_ext_JEEP = Car_Category_ext_Saloon = Car_Category_ext_Truck = 0

    #Car_Colour
    if Car_Colour_ext == "As Attached":
        Car_Colour_ext_As_Attached = 1
        Car_Colour_ext_Black = Car_Colour_ext_Grey = Car_Colour_ext_Other = Car_Colour_ext_Silver = 0
    elif Car_Colour_ext == "Black":
        Car_Colour_ext_As_Attached = Car_Colour_ext_Grey = Car_Colour_ext_Other = Car_Colour_ext_Silver = 0
        Car_Colour_ext_Black = 1
    elif Car_Colour_ext == "Grey":
        Car_Colour_ext_As_Attached = Car_Colour_ext_Black = Car_Colour_ext_Other = Car_Colour_ext_Silver = 0
        Car_Colour_ext_Grey = 1
    elif Car_Colour_ext == "Other":
        Car_Colour_ext_As_Attached = Car_Colour_ext_Black = Car_Colour_ext_Grey = Car_Colour_ext_Silver = 0
        Car_Colour_ext_Other = 1
    else:
        Car_Colour_ext_As_Attached = Car_Colour_ext_Black = Car_Colour_ext_Grey = Car_Colour_ext_Other = 0
        Car_Colour_ext_Silver = 1

    #Age_bin
    if Age >= 0 and Age < 15:
        Age_bin_1= 1
        Age_bin_2= Age_bin_3= Age_bin_4= Age_bin_5= Age_bin_6= Age_bin_7= 0
    elif Age >= 15 and Age < 30:
        Age_bin_1= Age_bin_3= Age_bin_4= Age_bin_5= Age_bin_6= Age_bin_7= 0
        Age_bin_2= 1
    elif Age >= 30 and Age < 45:
        Age_bin_1= Age_bin_2= Age_bin_4= Age_bin_5= Age_bin_6= Age_bin_7= 0
        Age_bin_3= 1
    elif Age >= 45 and Age < 60:
        Age_bin_1= Age_bin_2= Age_bin_3= Age_bin_5= Age_bin_6= Age_bin_7= 0
        Age_bin_4= 1
    elif Age >= 60 and Age < 75:
        Age_bin_1= Age_bin_2= Age_bin_3= Age_bin_4= Age_bin_6= Age_bin_7= 0
        Age_bin_5= 1
    elif Age >= 75 and Age < 100:
        Age_bin_1= Age_bin_2= Age_bin_3= Age_bin_4= Age_bin_5= Age_bin_7= 0
        Age_bin_6= 1
    else:
        Age_bin_1= Age_bin_2= Age_bin_3= Age_bin_4= Age_bin_5= Age_bin_6= 0
        Age_bin_7= 1

    #No_Pol
    if No_Pol == 1:
        No_Pol_1 = 1
        No_Pol_2 = No_Pol_3 = No_Pol_4 = No_Pol_5 = No_Pol_6 = No_Pol_7 = No_Pol_10 = 0
    elif No_Pol == 2:
        No_Pol_1 = No_Pol_3 = No_Pol_4 = No_Pol_5 = No_Pol_6 = No_Pol_7 = No_Pol_10 = 0
        No_Pol_2 = 1
    elif No_Pol == 3:
        No_Pol_1 = No_Pol_2 = No_Pol_4 = No_Pol_5 = No_Pol_6 = No_Pol_7 = No_Pol_10 = 0
        No_Pol_3 = 1
    elif No_Pol == 4:
        No_Pol_1 = No_Pol_2 = No_Pol_3 = No_Pol_5 = No_Pol_6 = No_Pol_7 = No_Pol_10 = 0
        No_Pol_4 = 1
    elif No_Pol == 5:
        No_Pol_1 = No_Pol_2 = No_Pol_3 = No_Pol_4 = No_Pol_6 = No_Pol_7 = No_Pol_10 = 0
        No_Pol_5 = 1
    elif No_Pol == 6:
        No_Pol_1 = No_Pol_2 = No_Pol_3 = No_Pol_4 = No_Pol_5 = No_Pol_7 = No_Pol_10 = 0
        No_Pol_6 = 1
    else:
        No_Pol_1 =No_Pol_2 = No_Pol_3 = No_Pol_4 = No_Pol_5 = No_Pol_6 = No_Pol_10 = 0
        No_Pol_7 = 1
        
    #Car_Make
    if Car_Make_ext == "Honda":
        Car_Make_ext_Honda = 1
        Car_Make_ext_Hyundai = Car_Make_ext_Lexus = Car_Make_ext_Mercedes = Car_Make_ext_Other = Car_Make_ext_TOYOTA = 0
    elif Car_Make_ext == "Hyundai":
        Car_Make_ext_Hyundai = 1
        Car_Make_ext_Honda = Car_Make_ext_Lexus = Car_Make_ext_Mercedes = Car_Make_ext_Other = Car_Make_ext_TOYOTA = 0
    elif Car_Make_ext == "Mercedes":
        Car_Make_ext_Mercedes = 1
        Car_Make_ext_Honda = Car_Make_ext_Hyundai = Car_Make_ext_Lexus = Car_Make_ext_Other = Car_Make_ext_TOYOTA = 0
    elif Car_Make_ext == "Lexus":
        Car_Make_ext_Lexus = 1
        Car_Make_ext_Honda = Car_Make_ext_Hyundai = Car_Make_ext_Mercedes = Car_Make_ext_Other = Car_Make_ext_TOYOTA = 0
    elif Car_Make_ext == "TOYOTA":
        Car_Make_ext_TOYOTA = 1
        Car_Make_ext_Honda = Car_Make_ext_Hyundai = Car_Make_ext_Lexus = Car_Make_ext_Mercedes = Car_Make_ext_Other = 0
    else:
        Car_Make_ext_Other = 1
        Car_Make_ext_Honda = Car_Make_ext_Hyundai = Car_Make_ext_Lexus = Car_Make_ext_Mercedes = Car_Make_ext_TOYOTA = 0


    #ProductName
    if ProductName == "Car Classic":
        ProductName_ext_Car_Classic = 1
        ProductName_ext_Car_Plus = ProductName_ext_CarSafe = ProductName_ext_Customized_Motor = ProductName_ext_Other = 0
    elif ProductName == "Car Plus":
        ProductName_ext_Car_Plus = 1
        ProductName_ext_Car_Classic = ProductName_ext_CarSafe = ProductName_ext_Customized_Motor = ProductName_ext_Other = 0
    elif ProductName == "CarSafe":
        ProductName_ext_CarSafe = 1
        ProductName_ext_Car_Classic = ProductName_ext_Car_Plus = ProductName_ext_Customized_Motor = ProductName_ext_Other = 0
    elif ProductName == "Customized Motor":
        ProductName_ext_Customized_Motor = 1
        ProductName_ext_Car_Classic = ProductName_ext_Car_Plus = ProductName_ext_CarSafe = ProductName_ext_Other = 0
    else:
        ProductName_ext_Other = 1
        ProductName_ext_Car_Classic = ProductName_ext_Car_Plus = ProductName_ext_CarSafe = ProductName_ext_Customized_Motor = 0

    #State
    if State_ext == "Abuja-Municipal":
        State_ext_Abuja_Municipal = 1
        State_ext_Benue = State_ext_Eti_Osa = State_ext_Ibeju_Lekki = State_ext_Lagos = State_ext_Ogun = State_ext_Other = 0
    elif State_ext == "Benue":
        State_ext_Benue = 1
        State_ext_Abuja_Municipal = State_ext_Eti_Osa = State_ext_Ibeju_Lekki = State_ext_Lagos = State_ext_Ogun = State_ext_Other = 0
    elif State_ext == "Eti-Osa":
        State_ext_Eti_Osa = 1
        State_ext_Abuja_Municipal = State_ext_Benue = State_ext_Ibeju_Lekki = State_ext_Lagos = State_ext_Ogun = State_ext_Other = 0
    elif State_ext == "Ibeju-Lekki":
        State_ext_Ibeju_Lekki = 1
        State_ext_Abuja_Municipal = State_ext_Benue = State_ext_Eti_Osa = State_ext_Lagos = State_ext_Ogun = State_ext_Other = 0
    elif State_ext == "Lagos":
        State_ext_Lagos = 1
        State_ext_Abuja_Municipal = State_ext_Benue = State_ext_Eti_Osa = State_ext_Ibeju_Lekki =State_ext_Ogun = State_ext_Other = 0
    elif State_ext == "Ogun":
        State_ext_Ogun = 1
        State_ext_Abuja_Municipal = State_ext_Benue = State_ext_Eti_Osa = State_ext_Ibeju_Lekki = State_ext_Lagos = State_ext_Other = 0
    else:
        State_ext_Other = 1
        State_ext_Abuja_Municipal = State_ext_Benue = State_ext_Eti_Osa = State_ext_Ibeju_Lekki = State_ext_Lagos = State_ext_Ogun = 0

    #No_Days_Policy
    No_Days_Policy = (float(Policy_Duration) - 16) / 11092






    # collect inputs
    input = {
        "Gender_ext_Female" : Gender_ext_Female, "Gender_ext_Male" : Gender_ext_Male, "Gender_ext_Other" : Gender_ext_Other,
        "Car_Category_ext_Other" : Car_Category_ext_Other, "Car_Category_ext_JEEP" : Car_Category_ext_JEEP, "Car_Category_ext_Truck" : Car_Category_ext_Truck, "Car_Category_ext_Saloon" : Car_Category_ext_Saloon,
        "Car_Colour_ext_As Attached" : Car_Colour_ext_As_Attached, "Car_Colour_ext_Black" : Car_Colour_ext_Black, "Car_Colour_ext_Grey" : Car_Colour_ext_Grey, "Car_Colour_ext_Other" : Car_Colour_ext_Other, "Car_Colour_ext_Silver" : Car_Colour_ext_Silver,
        "Age_bin_1": Age_bin_1, "Age_bin_2" : Age_bin_2, "Age_bin_3" : Age_bin_3, "Age_bin_4" : Age_bin_4, "Age_bin_5" : Age_bin_5, "Age_bin_6" : Age_bin_6, "Age_bin_7" : Age_bin_7,
        "No_Pol_1" : No_Pol_1, "No_Pol_2" : No_Pol_2, "No_Pol_3" : No_Pol_3, "No_Pol_4" : No_Pol_4, "No_Pol_5" : No_Pol_5, "No_Pol_6" : No_Pol_6, "No_Pol_7" : No_Pol_7, "No_Pol_10" : No_Pol_10,
        "Car_Make_ext_Honda" : Car_Make_ext_Honda, "Car_Make_ext_Hyundai" : Car_Make_ext_Hyundai, "Car_Make_ext_Lexus" : Car_Make_ext_Lexus, "Car_Make_ext_Mercedes" : Car_Make_ext_Mercedes, "Car_Make_ext_Other" : Car_Make_ext_Other, "Car_Make_ext_TOYOTA" : Car_Make_ext_TOYOTA,
        "ProductName_ext_Car Classic" : ProductName_ext_Car_Classic, "ProductName_ext_Car Plus" : ProductName_ext_Car_Plus, "ProductName_ext_CarSafe" : ProductName_ext_CarSafe, "ProductName_ext_Customized Motor" : ProductName_ext_Customized_Motor, "ProductName_ext_Other" : ProductName_ext_Other,
        "State_ext_Abuja-Municipal" : State_ext_Abuja_Municipal, "State_ext_Benue" : State_ext_Benue, "State_ext_Eti-Osa" : State_ext_Eti_Osa, "State_ext_Ibeju-Lekki" : State_ext_Ibeju_Lekki, "State_ext_Lagos" : State_ext_Lagos, "State_ext_Ogun" : State_ext_Ogun, "State_ext_Other" : State_ext_Other,
        "No_Days_Policy" : No_Days_Policy}

    # create a draframe
    data = pd.DataFrame(input, index=[0])
    
    # perform prediction
    output = model.predict(data)
    probability = model.predict_proba(data)


    #Display results of the NLP task
    st.header("Results")
    if output[0] == 0:
        st.write(f'You are most likely not to submit claims with probability of {round(min(probability[0]),4)*100}% \n 😊')
    else:
        st.write(f'You are most likely to submit claims with probability of {round(max(probability[0]),4)*100}% \n  😔')
