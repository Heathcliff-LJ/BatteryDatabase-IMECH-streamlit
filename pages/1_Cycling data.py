import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from openpyxl import Workbook

# 侧栏标题
st.sidebar.header("Select Specific Conditions")
# 标题
st.header('Cycling Test Dataset')
st.markdown("""
        The Cycling Test Dataset now contains 1406 different batteries. You can filter out specific batteries, visualize
         the capacity fade curves, and download the raw data.  
         __Select battery characteristics and operating conditions in the side bar to START!__
         """)

# 多选项设置
forms = st.sidebar.multiselect(
    'Form',
    [1865],
    [1865]
)

cathodes = st.sidebar.multiselect(
    'Cathode',
    ['NMC', 'LFP', 'NCA'],
    ['NMC', 'LFP', 'NCA']
)


anodes = st.sidebar.multiselect(
    'Anode',
    ['graphite'],
    ['graphite']
)

ahs = st.sidebar.multiselect(
    'Nominal Capacity (Ah)',
    [1.5, 2.6, 3.18, 3.35],
    [1.5, 2.6, 3.35]
)

temperatures = st.sidebar.multiselect(
    'Temperature (℃)',
    [0, 25, 40, 60, 80],
    [25, 40, 60]
)

chg_rates = st.sidebar.multiselect(
    'Charge rate (C)',
    [0.3, 0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.2, 2.5, 3, 8],
    [0.8, 1, 1.5, 1.8, 2]
)

dischg_rates = st.sidebar.multiselect(
    'Discharge rate (C)',
    [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8],
    [1.5, 2, 3, 4]
)

uppers = st.sidebar.multiselect(
    'Upper Voltage (V)',
    [4, 4.1, 4.2, 4.3, 4.4, 4.5],
    [4, 4.2, 4.3]
)

lowers = st.sidebar.multiselect(
    'Lower Voltage (V)',
    [2, 2.5, 2.65, 2.75],
    [2, 2.5, 2.65, 2.75]
)

manufacturers = st.sidebar.multiselect(
    'Manufacturer',
    ['LG', 'EVE', 'LISHEN', 'Samsung', 'Panasonic', 'MOLICELL'],
    ['Samsung', 'LISHEN']
)


cell_list = pd.read_excel('cell_list.xlsx')    # 读取电池ID列表
cell_number = len(cell_list)              # 列表行数，即电池个数
indexs = list(range(0, cell_number))    # 给每个电池添加索引
# 选择完成后，开始数据过滤
# if st.sidebar.button("Filter to List"):
if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.sidebar.button('Filter to List', on_click=click_button)

if st.session_state.clicked:

    # ###_remove 代表要去除的选项
    forms_remove = [1865]
    if not forms:                  # 首先判断选择是否为空
        forms_remove = []
    else:
        for form in forms:                 # 若不为空从原始的所有选项中，去除用户选择项，即得到要删去的项
            forms_remove.remove(form)

    cathodes_remove = ['NMC', 'LFP', 'NCA']
    if not cathodes:
        cathodes_remove = []
    else:
        for cathode in cathodes:
            cathodes_remove.remove(cathode)

    anodes_remove = ['graphite']
    if not anodes:
        anodes_remove = []
    else:
        for anode in anodes:
            anodes_remove.remove(anode)

    ahs_remove = [1.5, 2.6, 3.18, 3.35]
    if not ahs:
        ahs_remove = []
    else:
        for ah in ahs:
            ahs_remove.remove(ah)

    temperatures_remove = [0, 25, 40, 60, 80]
    if not temperatures:
        temperatures_remove = []
    else:
        for temperature in temperatures:
            temperatures_remove.remove(temperature)

    chg_rates_remove = [0.3, 0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.2, 2.5, 3, 8]
    if not chg_rates:
        chg_rates_remove = []
    else:
        for chg_rate in chg_rates:
            chg_rates_remove.remove(chg_rate)

    dischg_rates_remove = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
    if not dischg_rates:
        dischg_rates_remove = []
    else:
        for dischg_rate in dischg_rates:
            dischg_rates_remove.remove(dischg_rate)

    uppers_remove = [4, 4.1, 4.2, 4.3, 4.4, 4.5]
    if not uppers:
        uppers_remove = []
    else:
        for upper in uppers:
            uppers_remove.remove(upper)

    lowers_remove = [2, 2.5, 2.65, 2.75]
    if not lowers:
        lowers_remove = []
    else:
        for lower in lowers:
            lowers_remove.remove(lower)

    manufacturers_remove = ['LG', 'EVE', 'LISHEN', 'Samsung', 'Panasonic', 'MOLICELL']
    if not manufacturers:
        manufacturers_remove = []
    else:
        for manufacturer in manufacturers:
            manufacturers_remove.remove(manufacturer)
# 开始遍历所有电池，删选出需要展示的电池
    for index in range(0, cell_number):
        for form_remove in forms_remove:
            if form_remove == cell_list.loc[index, 'Form']:
                indexs.remove(index)
        for cathode_remove in cathodes_remove:
            if cathode_remove == cell_list.loc[index, 'Cathode']:
                if index in indexs:
                    indexs.remove(index)
        for anode_remove in anodes_remove:
            if anode_remove == cell_list.loc[index, 'Anode']:
                if index in indexs:
                    indexs.remove(index)
        for ah_remove in ahs_remove:
            if ah_remove == cell_list.loc[index, 'Capacity']:
                if index in indexs:
                    indexs.remove(index)
        for temperature_remove in temperatures_remove:
            if temperature_remove == cell_list.loc[index, 'Temperature']:
                if index in indexs:
                    indexs.remove(index)
        for chg_rate_remove in chg_rates_remove:
            if chg_rate_remove == cell_list.loc[index, 'Charge-rate']:
                if index in indexs:
                    indexs.remove(index)
        for dischg_rate_remove in dischg_rates_remove:
            if dischg_rate_remove == cell_list.loc[index, 'Discharge-rate']:
                if index in indexs:
                    indexs.remove(index)
        for upper_remove in uppers_remove:
            if upper_remove == cell_list.loc[index, 'Upper-voltage']:
                if index in indexs:
                    indexs.remove(index)
        for lower_remove in lowers_remove:
            if lower_remove == cell_list.loc[index, 'Lower-voltage']:
                if index in indexs:
                    indexs.remove(index)
        for manufacturer_remove in manufacturers_remove:
            if manufacturer_remove == cell_list.loc[index, 'Manufacturer']:
                if index in indexs:
                    indexs.remove(index)

    st.markdown("""
        __The cell ID is arranged in the form of:__  
        "Manufacturer abbr. & batch number-Form abbr.-Cathode-Nominal Capacity-Charge-rate-Upper 
        Voltage-Discharge-rate-Lower Voltage-Working Temperature-Cell Number of repeated experiment."  
        __For example:__  
        "LG1-18-NCA-3.35-1_4.2-3_2.5-T25-1" represents the first batch 18650 cell with NCA cathode and 3.35
        Ah nominal capacity from LG, which charged at 1C to 4.2V and discharged to 2.5V at 3C in an environment of 25 degree.  
        __Click the Cell ID for visualization and details.__
        """)

    cell_list = cell_list.reindex(columns=['Choose'] + list(cell_list.columns))   # 添加新列
    cell_list.loc[:, 'Choose'] = False                                             # 新列的所有行均赋值True
    datalist = st.data_editor(cell_list.iloc[indexs], height=400, width=2000,
                              column_config={"Choose": st.column_config.CheckboxColumn(
                                  "Choose",
                                  help = "Choose a battery to plot and download",
                                  default = False,
                              )},
                              disabled=["ID", "Form", "Cathode", "Anode", "Capacity", "Temperature", "Charge-rate",
                                    "Discharge-rate", "Upper-voltage", "Lower-voltage", "Manufacturer"],
                              hide_index=True)

    if st.button('Capacity Plot'):
        chose_list = []
        for index in indexs:
            if datalist.loc[index, 'Choose']:
                chose_list.append(datalist.loc[index, 'ID'])
        st.write('The cells you selected:')
        plot_df = pd.DataFrame()

        for chose in chose_list:
            path = 'processed_data/' + chose + '.xlsx'
            workbook = pd.read_excel(path)
            plot_df['Cycle (N)'] = workbook['Cycle (N)']
            plot_df[chose] = workbook['Capacity (mAh)']
        # st.write(plot_df)
        plot_df = plot_df.drop(index=0)
        title = "Capacity Fade"
        column_names = plot_df.columns.tolist()
        column_names.pop(0)
        figure, ax = plt.subplots()
        for column_name in column_names:
            plt.plot(plot_df['Cycle (N)'], plot_df[column_name], '-')
        plt.title(title)
        plt.ylabel("Capacity (mAh)")
        plt.xlabel("Cycle Number (N)")
        plt.legend(column_names)
        st.pyplot(figure)

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation in every rerun
            return df.to_csv().encode("utf-8")

        csv = convert_df(plot_df)

        st.download_button(
            label="Download Plot Data",
            data=csv,
            file_name="plot_df.csv",
            mime="text/csv",
        )

    if st.button('Voltage Plot'):
        chose_list = []
        for index in indexs:
            if datalist.loc[index, 'Choose']:
                chose_list.append(datalist.loc[index, 'ID'])

        plot_df = {}
        for chose in chose_list:
            title = 'Voltage variations of Cell ' + ' : ' + chose
            path = 'cycle data/' + chose + '.xlsx'
            workbook = pd.read_excel(path)
            column_names = workbook.columns.tolist()
            figure, ax = plt.subplots()
            plt.plot(workbook[column_names[1]], workbook[column_names[0]], '-')
            plt.plot(workbook[column_names[3]], workbook[column_names[2]], '-')
            plt.plot(workbook[column_names[5]], workbook[column_names[4]], '-')
            plt.plot(workbook[column_names[7]], workbook[column_names[6]], '-')
            plt.plot(workbook[column_names[9]], workbook[column_names[8]], '-')
            plt.plot(workbook[column_names[11]], workbook[column_names[10]], '-')
            plt.title(title)
            plt.xlabel("Capacity (mAh)")
            plt.ylabel("Voltage (V)")
            plt.legend([column_names[0], column_names[2], column_names[4],
                        column_names[6], column_names[8], column_names[10]])
            st.pyplot(figure)

