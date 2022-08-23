import streamlit
streamlit.title('Mere mummy ka subah ka nashta Ma sha Allah')
streamlit.header('mere favorite khane')
streamlit.text(' ☕ Chai')
streamlit.text(' 🥟 toast')
streamlit.text('main to ghareeb hun mere ma bap mujhe ghareeb janam diye')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
