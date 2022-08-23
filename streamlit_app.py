import streamlit
streamlit.title('Mere mummy ka subah ka nashta Ma sha Allah')
streamlit.header('mere favorite khane')
streamlit.text(' ☕ Chai')
streamlit.text(' 🥟 toast')
streamlit.text('main to ghareeb hun mere ma bap mujhe ghareeb janam diye')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
