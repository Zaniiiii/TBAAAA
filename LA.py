import tbaDude
from collections import defaultdict
import streamlit as st

state_parse = []
def analyze(input_string):
    # Inisialisasi State 
    state_list = []; list(state_list.append(f'q{i}') for i in range(30+1))
    # Inisilisasi Nilai Awal
    transition_table = defaultdict(lambda: "ERROR", {})
     
    transition_table = tbaDude.transisi(transition_table)
    
    idx = 0
    state = 'q0'
    current_token = ''
    # state_parse.append('#')
    while state != 'ACCEPT':
        current_char = input_string[idx]
        current_token += current_char
        state = transition_table[(state, current_char)]
        print(f'{state} : {current_token}')
        if current_token[idx] == ' ': state_parse.append('space')
        else: state_parse.append(current_token[idx])
        
        if state == "ERROR":
            print("ERROR : Lexical Error")
            break
        idx += 1
    
    return state == "ACCEPT" 

def concat(input_string):
    return 
def main():
    # input_string = input("Input String : ")
    input_string = st.text_area("Tulis Kodemu : ", placeholder="Input String")
    input_string = input_string.replace('\n', ' ')
    if st.button('Run'):
        output = ""
        try:
            if analyze(input_string):
                st.write(f'Running')
            else:
                st.write('Syntax Error')
            if analyze(input_string):
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
#                     elif hasil[i] == 'space':
#                         for y in range(i,len(hasil)):
#                             if hasil[y+1] != 'space':
#                                  hasil[y] = ''
#                             else:
#                                 break
                st.write(hasil)
            else:
                st.write('ERROR : Lexical Error')
        except:
            print("ERROR : Lexical Error")
            st.write('ERROR : Lexical Error')
    st.title('Contoh kode dapat dilihat di:')
    st.text('https://www.w3schools.com/cpp/cpp_do_while_loop.asp')
        
main()
