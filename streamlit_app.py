import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

streamlit.header("Fruit load list contains:")
def get_fruit_load_list():
    with my_cnx_cursor() as my_cur:
        my_cur.execute("select *from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)



def insert_row_snowflake(new_fruit):
  with my_cnx_cursor() as my_cur:
     my_cur.execute("insert into fruit_load_list values('"Jackfruit"')")
     return "thanks for adding" +new_fruit

add_my_fruit=streamlit.text_input('what fruit would you like to add')
if streamlit.button('add fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)  
  




def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about')
   if not fruit_choice:
       streamlit.error("please select a fruit to get info")
   else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)


 
except URLError as e:
  streamlit.error()
