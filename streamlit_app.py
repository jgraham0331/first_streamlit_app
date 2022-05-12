import streamlit
import pandas as pd
import requests

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Reindex fruit list
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add a pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")

# Normalize fruityvice
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output to screen
streamlit.dataframe(fruityvice_normalized)
