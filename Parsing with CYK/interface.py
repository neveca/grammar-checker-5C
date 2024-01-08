#Buat interface streamlitnya
import streamlit as st

from controller.open_file import open_file
from controller.conversion import conversion
from cyk.parse import parse


def run():
    st.set_page_config(layout='wide')
    rules = open_file('CNF-5C.txt')
    cnf = conversion(rules)
    st.title('Apakah kalimat ini baku atau tidak?')
    
    col1, col2 = st.columns(2, gap='small')
    
    with col1:
        string_input = st.text_input('Masukkan kalimat bahasa Indonesia', placeholder='Masukkan kalimat bahasa Indonesia')
        list_string = string_input.split(' ')
        button_click = st.button('Cek', type='primary')
        
        if button_click:
            if len(list_string) <= 1:
                st.error('Kalimat tidak boleh kosong ataupun hanya terdiri dari satu kata')
            else:
                with col2:
                    st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                    parse(cnf, string_input.split(' '))
