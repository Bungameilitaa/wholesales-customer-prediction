import streamlit as st 
from streamlit_option_menu import option_menu
import numpy as np
import pickle
from PIL import Image

loaded_model = pickle.load(open('Praktikum/trained_model.sav', 'rb'))



#Navigasi Menu 

with st.sidebar:
    
         selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "App", "About"],
            icons=["house", "bi bi-app", "bi bi-file-person"],
            menu_icon="bi bi-list",
            default_index=0,

            
        )

def deathevent_prediction(input_data):

    input_data =(2,3,12669,9656,7561,214,2674)

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Bukan Customer Grosir'
    else:
      return 'Customer Grosir'

def main():
    
 
    st.title('Wholesale Customers Classification Web App')
        
    
    Region = st.number_input('Region')
    Fresh = st.number_input('Annual spending (m.u.) on fresh products ')
    Milk = st.number_input(' Annual spending (m.u.) on milk products ')
    Grocery = st.number_input('Annual spending (m.u.) on grocery products ')
    Frozen = st.number_input('Annual spending (m.u.) on frozen products ')
    Detergents_Paper = st.number_input('Annual spending (m.u.) on detergents and paper products')
    Delicassen = st.number_input('Annual spending (m.u.) on delicatessen products')
    
    
    diagnosis = ''

    if st.button('Wholesale Customer Classification'):
        diagnosis = deathevent_prediction([Region, Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen])
        
    st.info(diagnosis)
       
def home():
    st.title('Selamat datang di Aplikasi Prediksi Customer Grosir atau Customer  Non-Grosir')
    img = Image.open("icon-wholesale.png")
    st.image(img, width=400)
    st.header("Wholesale Customer")
    st.caption('<div style="text-align: justify;">Aplikasi ini merupakan sebuah aplikasi yang dapat digunakan untuk mengklasifikasikan antara pelanggan grosir atau pelanggan non-grosir berdasarkan pembelian dari berbagai segmentasi produk dalam satuan monetary unit (m.u).</div>', unsafe_allow_html=True)
    st.text("")
    st.caption('<div style="text-align: justify;">Wholesale customer adalah setiap orang (atau bisnis) yang membeli barang eceran. Siapa pun yang mencari keuntungan dari produk grosir dapat menjadi pelanggan grosir potensial. Namun, tidak menutup kemungkinan bahwa individu, perusahaan, dan lain-lain boleh melakukan grosir. Ini sebenarnya sangat sederhana. Siapa pun yang ingin mendapat untung melalui produk grosir dapat menjadi pelanggan grosir potensial. Wholesale customer bisa banyak orang dan banyak perusahaan, tetapi produk mereka harus terkait dengan industri Anda, jadi jika Anda ingin menemukan pelanggan grosir secara akurat, Anda harus mencari pengecer atau perusahaan yang terkait dengan bisnis Anda.</div>', unsafe_allow_html=True)
    st.header("Algoritma")
    st.caption('<div style="text-align: justify;">Pada Aplikasi ini digunakan K-Nearest Neighbour sebagai Algoritma atau pendekatan untuk melakukan klasifikasi. Algoritma Nearest Neighbor Retrieval (K-Nearest Neighbor atau K-NN) adalah sebuah algoritma untuk melakukan klasifikasi terhadap objek dengan data pembelajaran yang jaraknya paling dekat dengan objek tersebut.</div>', unsafe_allow_html=True)
  
    
def about():
    st.title("Nama Anggota Kelompok 9 : ")
    st.caption('- Ayu Anggraini (20051214001)')
    st.caption('- Devi Yanti (200512140019)')
    st.caption('- Faalih Hibban (20051214029)')
    st.caption('- Bunga Meilita (20051214037)')
    st.caption('- Fauza Wayah   (20051214061)')
    st.caption('- Darell Timotius (20051214067)')

if selected == "Home":
    home()
    
if selected == "App":
    main()

if selected == "About":
    about()