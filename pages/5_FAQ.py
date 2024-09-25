import streamlit as st

st.header('Frequently Asked Questions')

st.markdown("""
        ### Q: How should I credit the data that I download ?  
        A: Use of any data featured on this site for publication purposes should include references to the article that 
        describes the experiments conducted for generating the data. See the  __Our team & Researches__ section for details. Please cite the corresponding article and https://batterydatabase-imech-app.streamlit.app/ as the sources from where
         the data was downloaded. 
        ### Q: How are the cells named ?
        A: The cell ID is arranged in the form of: "Manufacturer abbr. & batch number-Form abbr.-Cathode-Nominal Capacity
        -Charge-rate-Upper Voltage-Discharge-rate-Lower Voltage-Working Temperature-Cell Number of repeated experiment".
         __For example:__"LG1-18-NCA-3.35-1_4.2-3_2.5-T25-1" represents the first batch 18650 cell with NCA cathode and 3.35
        Ah nominal capacity from LG, which charged at 1C to 4.2V and discharged to 2.5V at 3C in an environment of 25 degree.
        ### Q: How how can I get access to the raw data ?
        A: To offer site feedback or contribute datasets, please email：liujin@imech.ac.cn
        ### Q: How do I contribute data to the site ?
        A: To offer site feedback or contribute datasets, please email：liujin@imech.ac.cn
        
        """)
