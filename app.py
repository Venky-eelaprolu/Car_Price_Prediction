import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open("car_price_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🚗 Car Price Prediction System")
st.caption("Machine Learning Based Vehicle Valuation")

st.subheader("🔧 Enter Car Details")

levy  = st.number_input("Levy(Additional mandatory charge paid to the government for owning or importing a vehicle)",
                         value=0.0, format="%.1f")

manufacture = st.selectbox("Manufacture", ['TOYOTA', 'FORD', 'HYUNDAI', 'CHEVROLET', 'NISSAN', 'LEXUS',
       'AUDI', 'MERCEDES-BENZ', 'HONDA', 'KIA', 'BMW', 'SUBARU', 'OPEL',
       'MAZDA', 'VOLKSWAGEN', 'DAEWOO', 'ACURA', 'JAGUAR', 'SSANGYONG',
       'MITSUBISHI', 'DODGE', 'FIAT', 'GMC', 'BENTLEY', 'BUICK',
       'CHRYSLER', 'MINI', 'CADILLAC', 'JEEP', 'PORSCHE', 'RENAULT',
       'MASERATI', 'SUZUKI', 'LINCOLN', 'LAND ROVER', 'INFINITI', 'SCION',
       'FERRARI', 'CITROEN', 'VAZ', 'GAZ', 'LAMBORGHINI', 'DAIHATSU',
       'VOLVO', 'MERCURY', 'HUMMER', 'PEUGEOT', 'SKODA'])

category = st.selectbox("Car Category", ['Hatchback', 'Sedan', 'Jeep', 'Coupe', 'Goods wagon', 'Microbus',
       'Minivan', 'Universal', 'Pickup', 'Cabriolet'])

interior = st.radio("Interior Status", ['Yes', 'No'])

fuel = st.selectbox("Fuel Type", ['Petrol', 'Hybrid', 'Diesel', 'LPG', 'Plug-in Hybrid', 'CNG'])

volume  = st.number_input("Engine Volume", value=0.0, format="%.1f")

mileage  = int(st.number_input("Mileage", value=0))

cylinders  = st.number_input("Cylinders", value=0.0, format="%.1f")

gear = st.pills("Gear Box Type", ['Automatic', 'Variator', 'Tiptronic', 'Manual'])


wheels = st.pills("Drive Wheels", ['Front', '4x4', 'Rear'])

air_bags  = int(st.number_input("Air Bags", value=0))

turbo = st.pills("Turbo (0 --> No Turbo) or (1 --> Turbo)", [0, 1])

age  = int(st.number_input("Car Age", value=0))

if st.button("🚀 Predict Car Price"):
    input_df = pd.DataFrame([{'Levy' : levy, 
                              'Manufacturer' : manufacture, 
                              'Category' : category, 
                              'Leather interior' : interior, 
                              'Fuel type' : fuel,
                              'Engine volume' : volume, 
                              'Mileage' : mileage, 
                              'Cylinders' : cylinders, 
                              'Gear box type' : gear,
                              'Drive wheels' : wheels, 
                              'Airbags' : air_bags, 
                              'Turbo' : turbo, 
                              'Car_Age' : age}])
    
    result = model.predict(input_df)[0]
    st.metric(
        label="Predicted Car Price",
        value=f"${result:,.2f}"
    )
