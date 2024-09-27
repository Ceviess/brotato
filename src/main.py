import math
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
    result_dmg = int(
        (base_dmg + math.floor(flat_damage * dmg_modifier)) * (1 + dmg_percent / 100)
    ) * (1 + (atk_spd / 100))
    st.write("Result:", result_dmg)

col12, col22, col32, col42, col52, col62 = st.columns(6)
with col12:
    base_dmg_1 = st.number_input(" Base dmg", value=3)
with col22:
    flat_damage_1 = st.number_input(" Flat damage", value=1)
with col32:
    dmg_modifier_1 = st.number_input(" Damage modifier", value=0.5)
with col42:
    dmg_percent_1 = st.number_input(" Damage %", value=3)
with col52:
    atk_spd_1 = st.number_input(" Attack speed", value=3)
with col62:
    result_dmg_1 = int(
        (base_dmg_1 + math.floor(flat_damage_1 * dmg_modifier_1)) * (1 + dmg_percent_1 / 100)
    ) * (1 + (atk_spd_1 / 100))
    st.write(" Result:", result_dmg_1)

col121, col221, col321, col421, col521, col621 = st.columns(6)
with col121:
    base_dmg_2 = st.number_input("  Base dmg", value=3)
with col221:
    flat_damage_2 = st.number_input("  Flat damage", value=1)
with col321:
    dmg_modifier_2 = st.number_input("  Damage modifier", value=0.5)
with col421:
    dmg_percent_2 = st.number_input("  Damage %", value=3)
with col521:
    atk_spd_2 = st.number_input("  Attack speed", value=3)
with col621:
    result_dmg_2 = int(
        (base_dmg_2 + math.floor(flat_damage_2 * dmg_modifier_2)) * (1 + dmg_percent_2 / 100)
    ) * (1 + (atk_spd_2 / 100))
    st.write("  Result:", result_dmg_2)

st.title("EHP calculator")

col11, col21, col31, col41 = st.columns(4)
with col11:
    base_hp = st.number_input("Base hp", value=10)
with col21:
    armor = st.number_input("Armor", value=1)
with col31:
    dodge = st.number_input("Dodge", value=1)
with col41:
    dmg_red = 1 - 1 / (1 + 1 / 15 * armor)
    ehp = base_hp / (1 - dmg_red) / (1 - dodge / 100)
    st.write("Result:", ehp)

col112, col212, col312, col412 = st.columns(4)
with col112:
    base_hp_1 = st.number_input(" Base hp", value=10)
with col212:
    armor_1 = st.number_input(" Armor", value=1)
with col312:
    dodge_1 = st.number_input(" Dodge", value=1)
with col412:
    dmg_red_1 = 1 - 1 / (1 + 1 / 15 * armor_1)
    ehp_1 = base_hp_1 / (1 - dmg_red_1) / (1 - dodge_1 / 100)
    st.write(" Result:", ehp_1)
