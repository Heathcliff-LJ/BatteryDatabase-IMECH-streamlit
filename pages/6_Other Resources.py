import streamlit as st

st.header('Resources')

st.markdown("""
    This page is intended to help users to find information and get access to other public battery database and 
    literatures. The listing of a resources is not intended to be an endorsement. Please let us know if there are other
     resources that could also be included. """)

st.markdown("""
    ### Prognostics Data Repository (NASA)
    The Prognostics Data Repository from NASA is a collection of data sets that have been donated by universities, agencies, 
    or companies. The data repository focuses exclusively on prognostic data sets, i.e., data sets that can be used for 
    the development of prognostic algorithms. Most of these are time-series data from a prior nominal state to a failed 
    state.
    """)
st.link_button("Prognostics Data Repository NASA", "https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/")

st.markdown("""
    ### Center for Advanced Life Cycle Engineering (Maryland)
    The CALCE battery team from University of Maryland is open to collaborate with research groups and companies around the world. They provide open
     access to their experimental test data on lithium-ion batteries, which includes continuous full and partial cycling
     , storage, dynamic driving profiles, open circuit voltage measurements, and impedance measurements. The data from 
     these tests can be used for battery state estimation, remaining useful life prediction, accelerated battery
      degradation modeling, and reliability analysis.
    """)
st.link_button("CALCE University of Maryland", "https://calce.umd.edu/data")

st.markdown("""
    ### Experiment Data Platform (Standford & MIT & TOYOTA)    
    This dataset is used in the publication “Data-driven prediction of battery cycle life before capacity degradation” 
    and “Closed-loop optimization of extreme fast charging for batteries using machine learning”. The dataset consists 
    of lithium-ion phosphate (LFP)/graphite cells, manufactured by A123 Systems (APR18650M1A) cycled under fast-charging
     conditions.
    """)
st.link_button("Experiment Data Platform", "https://data.matr.io/1/")

st.markdown("""
    ### BatteryArchive (Sandia National Lab) 
    The dataset from Sandia National Labs used in the publication, “Degradation of Commercial Lithium-ion Cells as a 
    Function of Chemistry and Cycling Conditions,” consists of commercial 18650 NCA, NMC, and LFP cells cycled to 80% 
    capacity. This study examines the influence of temperature, depth of discharge 
    (DOD), and discharge current on the long-term degradation of the commercial cells.
    """)
st.link_button("BatteryArchive Sandia", "https://www.batteryarchive.org/index.html")

st.markdown("""
    ### Everlasting Project  
    Cycling ageing of Li ion 18650 commercial cell (Ni rich positive electrode and Si/Gr based negative electrode). The 
    cells were aged at different C-rates (0.5C, 3C, 0.5D, 1D) and different environmental temperatures (0, 10, 25, 45). 
    Each test condition was applied on two cells. The cells were cycled within a 10-90%SOC window. These levels are 
    defined from fresh cells and fixed (i.e. not updated with ageing). The cycling is regularly interrupted to run a 
    reference test. More details of the ageing tests can be found in the Everlasting deliverable.
    """)
col1, col2= st.columns(2)
with col1:
    st.link_button("Everlasting Project 0℃ & 10℃",
                   "https://data.4tu.nl/articles/dataset/Lifecycle_ageing_tests_on_commercial_18650_Li_ion_cell_10_C_and_0_C/14377295")
with col2:
    st.link_button("Everlasting Project 25℃ & 45℃",
                   "https://data.4tu.nl/articles/dataset/Lifecycle_ageing_tests_on_commercial_18650_Li_ion_cell_25_C_and_45_C/13739296/1")

