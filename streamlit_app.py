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









  
def insert_row_snowflake(new_fruit):
 with my_cnx_cursor() as my_cur:
  my_cur.execute("insert into fruit_load_list values ('" +jackfruit+ "')")
  return "thanks for adding" +new_fruit


 
except URLError as e:
  streamlit.error()
