import tbaDude
from collections import defaultdict
import streamlit as st
from PIL import Image

state_parse = []
def analyze(inputCode):
    # Inisialisasi State 
    state_list = []; list(state_list.append(f'q{i}') for i in range(30+1))
    # Inisilisasi Nilai Awal
    transition_table = defaultdict(lambda: "ERROR", {})
     
    transition_table = tbaDude.transisi(transition_table)
    
    idx = 0
    state = 'q0'
    token = ''
    # state_parse.append('#')
    while state != 'ACCEPT':
        current_char = inputCode[idx]
        token += current_char
        state = transition_table[(state, current_char)]
        print(f'{state} : {token}')
        if token[idx] == ' ': state_parse.append('space')
        else: state_parse.append(token[idx])
        
        if state == "ERROR":
            print("ERROR : Lexical Error")
            break
        idx += 1
    
    return state == "ACCEPT" 

def concat(inputCode):
    return 
def main():
    st.title("Tugas TBA Kelompok 10")
    
    inputCode = st.text_area("Tulis Kodemu : ", placeholder="Input Code")
    inputCode = inputCode.replace('\n', ' ')
    if st.button('Run'):
        output = ""
        try:
            if analyze(inputCode):
                st.write(f'Running')
            else:
                st.write('Syntax Error')
            if analyze(inputCode):
                st.write('TOKEN:')
                hasil = state_parse
                for i in range(len(hasil)):
                    if hasil[i] == 'd' and hasil[i+1] == 'o':
                        hasil[i] = 'do'
                        hasil[i+1] = ''
                    elif hasil[i] == 'w' and hasil[i+1] == 'h' and hasil[i+2] == 'i' and hasil[i+3] == 'l' and hasil[i+4] == 'e':
                        hasil[i] = 'while'
                        hasil[i+1] = ''
                        hasil[i+2] = ''
                        hasil[i+3] = ''
                        hasil[i+4] = ''
                    elif hasil[i] == 'space' and hasil[i+1] == 'space':
                        hasil[i] = ''
                hasil = [i for i in hasil if i != '']
                st.write(hasil)
            else:
                st.write('ERROR : Lexical Error')
        except:
            print("ERROR : Lexical Error")
            st.write('ERROR : Lexical Error')
    st.title('Cara menjalankan:')
    st.write('Masukkan kode yang ingin dicek, pada tempat penulisan kode diatas')
    st.title('Berikut merupakan contoh code:')
    image1 = Image.open('1.png')
    image2 = Image.open('2.png')
    image3 = Image.open('3.png')
    st.image(image1, caption = 'Contoh 1')
    st.image(image2, caption = 'Contoh 2')
    st.image(image3, caption = 'Contoh 3')
        
main()
