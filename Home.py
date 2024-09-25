import streamlit as st

# 页面名称
st.set_page_config(
    page_title="IMECH CAS Battery Database",
    page_icon="🔋"
)

# 总标题
st.write("## Welcome to IMECH CAS Battery Database! 🔋")
st.markdown(
    """
     A repository for easy access of battery experiment data worldwide.
    ### Battery Experiments Data
    """)

# 分列1
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Cycling")
    st.image('pics/Aging.png')
with col2:
    st.write("Characterization")
    st.image('pics/Characterization.png')
with col3:
    st.write("Disruptive")
    st.image('pics/Disruptive.png')

st.markdown(
    """
    ### Data Visualization & Comparison
    """)

# 分列2
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Voltage curves")
    st.image('pics/Voltage.png')
with col2:
    st.write("Capacity fade")
    st.image('pics/Capacity.jpg')
with col3:
    st.write("Temperature rise")
    st.image('pics/Temperature.jpg')

st.markdown(
    """
     ### Access to Related Studies
     - End of Life Prediction
     - State of Health Evaluation
     - Degradation Mechanism Analysis
     - ......
     ## Contact us
     To ask for raw data, offer site feedback or contribute datasets, please email ...@imech...
     """
 )

# 侧栏文字
st.sidebar.header("IMECH CAS Battery Database")
