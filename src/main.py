import numpy as np
import streamlit as st

st.title("Dps calculator")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    base_dmg = st.number_input("Base dmg", value=3)
with col2:
    flat_damage = st.number_input("Flat damage", value=1)
with col3:
    dmg_modifier = st.number_input("Damage modifier", value=0.5)
with col4:
    dmg_percent = st.number_input("Damage %", value=3)
with col5:
    atk_spd = st.number_input("Attack speed", value=3)
with col6:
    result_dmg = int((base_dmg + np.floor(flat_damage * dmg_modifier)) * (1 + dmg_percent / 100)) * (
            1 + (atk_spd / 100))
    st.write("Result:", result_dmg)

st.title("EHP calculator")

col11, col21, col31, col41 = st.columns(4)
with col11:
    base_hp = st.number_input("Base hp", value=10)
with col21:
    armor = st.number_input("Armor", value=1)
with col31:
    dodge = st.number_input("Dodge", value=1)
with col41:
    dmg_red = (1 - 1 / (1 + 1 / 15 * armor))
    ehp = base_hp / (1 - dmg_red) / (1 - dodge / 100)
    st.write("Result:", ehp)


