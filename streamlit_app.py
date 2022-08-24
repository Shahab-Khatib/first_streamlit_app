import streamlit
streamlit.title('Mere mummy ka subah ka nashta Ma sha Allah')
streamlit.header('mere favorite khane')
streamlit.header('Choose your favorite Smoothie')
streamlit.text(' ☕ Chai')
streamlit.text(' 🥟 toast')
streamlit.text(' 🍔 Burger')
streamlit.text('main to ghareeb hun mere ma bap mujhe ghareeb janam diye')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
