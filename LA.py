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
        # print(f'{state} : {current_char}')
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
    input_string = st.text_area("Input String : ", placeholder="Input String")
    input_string = input_string.replace('\n', ' ')
    if st.button('Analyze'):
        output = ""
        try:
            st.write(f'STATUS : {analyze(input_string)}')
            if analyze(input_string):
                st.write('TOKEN PARSED:')
                # remove word 'space'
                result = [i for i in state_parse if i != 'space']
                # parse word 'for', 'in', 'range'
                for i in range(len(result)):
                    if result[i] == 'd' and result[i+1] == 'o':
                        result[i] = 'do'
                        result[i+1] = ''
                    elif result[i] == 'w' and result[i+1] == 'h' and result[i+2] == 'i' and result[i+3] == 'l' and result[i+4] == 'e':
                        result[i] = 'while'
                        result[i+1] = ''
                        result[i+2] = ''
                        result[i+3] = ''
                        result[i+4] = ''
                st.write(list(dict.fromkeys([i for i in result if i != ''])))
            else:
                st.write('ERROR : Lexical Error')
        except:
            print("ERROR : Lexical Error")
            st.write('ERROR : Lexical Error')
    ex_code1 = '''for i in range(0,9,3):
    i = i + 1'''
    ex_code2 = '''for i in range(5):
    i = i + 1
    '''
    ex_code3 = '''for i in x:
    i = i + 1
    '''
    st.title('Example Code: ')
    st.code(ex_code1, language='python')
    st.code(ex_code2, language='python')
    st.write('Sebagai contoh inisial x adalah list: [1,2,3,4,5]')
    st.code(ex_code3, language='python')
        
main()
