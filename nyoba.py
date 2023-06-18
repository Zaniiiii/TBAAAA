def transition_tab(transition):
    var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    angka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ['+','-','=','*', '/', '%', '<', '>']
    
    # Syntax for
    # < do { > 
    transition[('q0', 'd')] = 'q1'
    transition[('q1', 'o')] = 'q2'
    transition[('q2', ' ')] = 'q2'
    transition[('q2', '{')] = 'q3'
    transition[('q3', ' ')] = 'q3'
    for i in var:
        transition[('q3', i)] = 'q4'
    transition[('q4', ' ')] = 'q4'
    for i in operator:
        if i == '+':
            transition[('q4', i)] = 'q5'
        elif i == '-':
            transition[('q4', i)] = 'q6'
    for i in operator:
        if i == '+':
            transition[('q5', i)] = 'q10'
        elif i == '-':
            transition[('q6', i)] = 'q10'
    transition[('q4', '=')] = 'q7'
    transition[('q7', ' ')] = 'q7'
    for i in var:
        transition[('q7', i)] = 'q8'
    transition[('q8', ' ')] = 'q8'
    for i in operator:
        if i != '=' and i != '>' and i != '<':
            transition[('q8', i)] = 'q9'
    transition[('q9', ' ')] = 'q9'
    for i in var:
        transition[('q9', i)] = 'q10'
    for i in angka:
        transition[('q9', i)] = 'q10'
    transition[('q10', ' ')] = 'q10'
#     transition[('q10', ';')] = 'ACCEPT'
    transition[('q11', '}')] = 'q12'
    transition[('q12', ' ')] = 'q13'
    transition[('q13', 'w')] = 'q14'
    transition[('q14', 'h')] = 'q15'
    transition[('q15', 'i')] = 'q16'
    transition[('q16', 'l')] = 'q17'
    transition[('q17', 'e')] = 'q18'
    transition[('q18', ';')] = 'ACCEPT'
#     transition[('q19', '(')] = 'q20'
#     for i in var:
#         transition[('q20', i)] = 'q21'
#     transition[('q21', ' ')] = 'q21'
#     for i in operator:
#         if i == '=' or i == '>' or i == '<':
#             transition[('q21', i)] = 'q22'
#     for i in operator:
#         if i == '=':
#             transition[('q22', i)] = 'q23'
#     for i in var:
#         transition[('q22', i)] = 'q24'
#         transition[('q23', i)] = 'q24'
#     for i in angka:
#         transition[('q22', i)] = 'q24'
#         transition[('q23', i)] = 'q24'
#     transition[('q24', ' ')] = 'q24'
#     transition[('q24', ')')] = 'q25'
#     transition[('q25', ';')] = 'ACCEPT'

        

    return transition

