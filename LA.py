import nyoba
from collections import defaultdict
import streamlit as st

state_parse = []
def analyze(input_string):
    # Inisialisasi State 
    state_list = []; list(state_list.append(f'q{i}') for i in range(30+1))
    # Inisilisasi Nilai Awal
    transition_table = defaultdict(lambda: "ERROR", {})
     
    transition_table = nyoba.transition_tab(transition_table)
    
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
                for i in range(len(state_parse)):
                    if state_parse[i] == 'd' and state_parse[i+1] == 'o':
                        state_parse[i] = 'do'
                        state_parse[i+1] = ''
                    elif state_parse[i] == 'w' and state_parse[i+1] == 'h' and state_parse[i+2] == 'i' and state_parse[i+3] == 'l' and state_parse[i+4] == 'e':
                        state_parse[i] = 'while'
                        state_parse[i+1] = ''
                        state_parse[i+2] = ''
                        state_parse[i+3] = ''
                        state_parse[i+4] = ''
                   elif state_parse[i] == 'space':
                        for y in range(i,len(state_parse)):
                            if state_parse[y+1] != 'space':
                                 state_parse[y] = ''
                            else:
                                break
                st.write(state_parse)
            else:
                st.write('ERROR : Lexical Error')
        except:
            print("ERROR : Lexical Error")
            st.write('ERROR : Lexical Error')
    st.title('Contoh kode dapat dilihat di:')
    st.text('https://www.w3schools.com/cpp/cpp_do_while_loop.asp')
        
main()
