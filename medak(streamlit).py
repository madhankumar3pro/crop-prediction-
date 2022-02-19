# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:42:55 2022

@author: madha
"""
import pyodbc
import streamlit as st
import pandas as pd 

from PIL import Image

conx=pyodbc.connect("driver={ODBC Driver 17 for SQL Server};server=DESKTOP-TGP0OCM;database=demo;trusted_connection=YES")
cursor=conx.cursor()
query="select *from dbo.medak"
data=pd.read_sql(query,conx)



dict={"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7,"August":8, "September":9, "October":10, "November":11,"December":12}   
def categorise(row):
        if row['date'] ==1:
            return "January"
        else:
            if row['date'] ==2:
                return "February"
            else:
                if row['date'] ==3:
                    return "March"
                else:
                    if row['date'] ==4:
                        return "April"
                    else:
                        if row['date'] ==5:
                            return "May"
                        else:
                            if row['date'] ==6:
                                return "June"
                            else:
                                if row['date'] ==7:
                                    return 'July'
                                else:
                                    if row['date'] ==8:
                                        return "August"
                                    else:
                                        if row['date'] ==9:
                                            return "September"
                                        else:
                                            if row['date'] ==10:
                                                return "October"
                                            else:
                                                if row['date'] ==11:
                                                    return "November"
                                                else:
                                                    
                                                    return "December"
                                                  
data['date'] = data.apply(lambda row: categorise(row), axis=1)





df = st.sidebar.selectbox("Navigation",["Crop Prediction","Contribute","About us"])
                                        
data.Soil_type.unique()
def gh(a):
    if df=="Crop Prediction":
        
        st.title("CROP PREDICTION")
        image=Image.open("C:\\Users\\madha\\OneDrive\\Desktop\\streamlit\\agriculture\\download.png")
        st.image(image,width=200)
        
        d=st.selectbox("Month",["January", "February", "March", "April", "May", "June", "July","August", "September", "October", "November","December"])
        f=st.selectbox("Crop_type",['Other', 'Flowers', 'vegetables', 'Fruits'])
        g=st.selectbox("Duration_term",['short_term', 'Intermediate_term', 'Long_term'])
        l=st.selectbox("Soil",['loamy soil', 'sandy loam', 'rich loam', 'deep loam', 'sandy soil','light loamy', 'fertile loam', 'red sandy loam', 'clay loam','deep black', 'clay'])
        e=st.selectbox("Irrigation",[True, False])
        i=st.selectbox("Crop_sown",[True, False])
        month=data[data['date']==d]
        crop_type=month[month['type_crop']==f]
        Duration_term=crop_type[crop_type['crop_term']==g]
        soil=Duration_term[Duration_term['Soil_type']==l]
        irrigation=soil[soil['irrigation']==e]
        crop_sown=irrigation[irrigation['crop_sown']==i]
        r=crop_sown.groupby(['Crop'])['Profit_per_acre'].mean().nlargest(2)
        data1=crop_sown.sort_values(by=['Profit_per_acre'], ascending=False)
        data2=data1[['Crop','avg_cost_of_cultivation_rs_ac','Profit_per_acre']]
        l=len(data2.Crop.unique())
        if st.button("submit"):
            if l==0:
                st.error("No profitable crops are there")
                
            elif l==1:
                st.success("Best Profitable crops")
                st.dataframe(data2)
            else:
                st.success("Best Profitable crops")
                for i in range(0,l):
                    h=data2.iloc[i,:]
                    h=h.astype(str)
                    st.dataframe(data=h)
        return data2
        
jk=gh(df)

 

if df=="Contribute":
    st.title("Contribute crop data")
    m=st.selectbox("district",['medak'])
    n=st.selectbox("Month",["January", "February", "March", "April", "May", "June", "July","August", "September", "October", "November","December"])
    j=st.text_input('crop')
    h=st.selectbox("Crop_sown",[True, False])
    W=st.text_input("rainfall_mm")
    g=st.text_input('temp_avg_C')
    f=st.text_input('humidity_avg')
    a=st.text_input('wind_speed_avg_Kmph')
    d=st.text_input('mrp_rs_kg')
    s=st.text_input('Min_duration_days')
    z=st.text_input('max_duration_days')
    x=st.text_input('duration_months')
    c=st.text_input('avg_cost_of_cultivation_rs_ac')
    v=st.text_input('Yield_kg_ac')
    b=st.selectbox('Soil_type',['loamy soil', 'sandy loam', 'rich loam', 'deep loam', 'sandy soil','light loamy', 'fertile loam', 'red sandy loam', 'clay loam','deep black', 'clay'])
    t=st.text_input('avg_pH')
    w=st.text_input('N_kg_ha')
    e=st.text_input('P_kg_ha')
    r=st.text_input('K_kg_ha')
    T=st.selectbox('irrigation',[ True, False])
    Y=st.text_input('gross_profit_rs_ac')
    u=st.text_input('net_profit_rs_ac')
    o=st.text_input('ROI')
    G=st.selectbox('sow_and_harvest',['one_sow_one_harvest', 'one_sow_few_harvests','one_sow_many_harvests'])
    O=st.text_input('get_amount_amount_acre')
    Q=st.text_input('Profit_per_acre')
    B=st.selectbox("Crop_term",['short_term', 'Intermediate_term', 'Long_term'])
    I=st.selectbox('type_crop',['Other', 'Flowers', 'vegetables', 'Fruits'])
    
    dict={"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7,"August":8, "September":9, "October":10, "November":11,"December":12}
    for i in dict.keys():
        V=dict[i]
    if st.button("submit"):
        cursor.execute("insert into [demo].[dbo].[medak] values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(m,V,j,h,W,g,f,a,d,s,z,x,c,v,b,t,w,e,r,T,Y,u,o,G,O,Q,B,I))
        conx.commit()
        st.success("successfully submit the data")

if df=="About us":
    
    
    
    st.title("CROP PREDICTION")
    
    st.subheader("INTRODUCTION")
    st.write("""The history of Agriculture in India dates back to Indus Valley Civilization Era 
             and even before that in some parts of Southern India.India ranks second worldwide in 
             farm outputs. Agriculture and allied sectors like forestry and fisheries accounted 
             for 20.9% of the GDP (gross domestic product) in 2021 with about 31% of the workforce
             in 2019. India ranks first globally with highest net cropped area followed by US and
             China. The economic contribution of agriculture to India's GDP is steadily declining 
             with the country's broad-based economic growth. Still, agriculture is demographically
             the broadest economic sector and plays a significant role in the overall 
             socio-economic fabric of India. The reason for this decline in the agriculture sector
             is due to the fact that farmers are not empowered and due to lack of application of 
             IT in the farming sector. Farmers have less knowledge about the crops they grow We 
             tend to overcome this obstacle by applying machine learning techniques to predict 
             the crop yield and name by considering various factors such as temperature, rainfall,
             season and area.""")
    st.subheader("Application Domain and Goals")
    
    st.write("""The project finds a huge application in improving real life farming scenarios. 
             A lot of crop is destroyed every year due to lack of knowledge of weather patterns 
             such as temperature, rainfall, etc. which play a huge role in deciding the crop 
             yield. This project not only helps in predicting these parameters for throughout the 
             year, but also assists in predicting the yield of various crops in various seasons 
             based on past trends. Hence it allows the farmers to decide the best crop to grow to 
             suffer minimum losses.""")

    image=Image.open("C:\\Users\\madha\\OneDrive\\Desktop\\streamlit\\agriculture\\agriculture-logo-design-free-downlaod-scaled.jpg")
    st.image(image,width=200)
    
    st.subheader("Conclusion and Future Scope")
    st.write("""This project solves one of the fundamental problems that the Indian farmers are 
             facing that is selection of which type of crop will yield the maximum results. 
             The sole objective is to increase farmer's income.""")
    st.write("""Lack of proper dataset is the major hurdle while predicting the name of the crops 
             but we were able to manage that by merging different data sets""")
    st.write("""This project right now covers only five features that are season ,area ,
             temperature, rainfall and crop name but that's not the end, this project holds 
             numerous possibilities such as the addition of vapour pressure, soil quality and 
             market integration.""")
    st.write("""This project if compiled with a bigger data set can be a boon for the government 
             as it may help them plan properly and in turn help our objective.""")
    
    image=Image.open("C:\\Users\\madha\\OneDrive\\Desktop\\streamlit\\agriculture\\data_science.jpg")
    st.image(image,width=200)
    
