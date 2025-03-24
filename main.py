import streamlit as st

def unit_comvertor(value,convert_from,convert_to):
    conversion={
        "meter_kilometers":0.001,
        "kilometers_meter":1000,
        "gram_kilogram":0.001,
        "kilogram_gram":1000,
        
    }
    key=f"{convert_from}_{convert_to}"
    if key in conversion:
        conversions=conversion[key]
        return value*conversions
    else:
        st.write("not supported")

st.title("Unit Converter App 💔 in Python 🐍")
value=st.number_input("Enter the value :")
convert_from=st.selectbox("Convert from: ",["meter","kilometers","gram","kilogram"])
convert_to=st.selectbox("Convert to: ",["kilometers","meter","gram","kilogram"])
if st.button("Convert"):
    result=unit_comvertor(value,convert_from,convert_to)
    if convert_from =="kilometers" and convert_to =="meter": 
        st.success(f"{result} m")
    
        # st.success(f"{result} m")
    elif convert_from =="meter" and convert_to =="kilometers": 
        st.success(f" {result} KM")
          
    elif convert_from =="gram" and convert_to =="kilogram": 
        st.success(f"{result} KG")
          
    elif convert_from =="kilogram" and convert_to =="gram": 
        st.success(f"{result} Gm")
    st.divider()   
    st.markdown("""
                <div style=text-align:center;>
                <p>Made By 💖 Muhammad Owais shah</p>
                """,unsafe_allow_html=True)
          
     
