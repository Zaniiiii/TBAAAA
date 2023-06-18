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
            transition[('q5', i)] = 'q7'
        elif i == '-':
            transition[('q6', i)] = 'q7'
    transition[('q7', ' ')] = 'q7'
    transition[('q7', ';')] = 'ACCEPT'
#     for i in neg:
#         transition[('q4', i)] = 'q7'
#     for i in neg:
#         transition[('q7', i)] = 'q8'
#     transition[('q8', ';')] = 'q13'
#     transition[('q4', '=')] = 'q9'
#     transition[('q9', ' ')] = 'q9'
#     for i in var:
#         transition[('q9', i)] = 'q10'
#     transition[('q10', ' ')] = 'q10'
#     for i in operator:
#         transition[('q10', i)] = 'q11'
#     transition[('q10', '+')] = 'q11'
#     transition[('q10', '-')] = 'q11'
#     transition[('q11', ' ')] = 'q11'
#     for i in var:
#         transition[('q11', i)] = 'q12'
#     transition[('q12', ';')] = 'q13'
#     transition[('q13', '}')] = 'q14'
#     transition[('q14', ' ')] = 'q14'
#     transition[('q14', 'w')] = 'q15'
#     transition[('q15', 'h')] = 'q16'
#     transition[('q16', 'i')] = 'q17'
#     transition[('q17', 'l')] = 'q18'
#     transition[('q18', 'e')] = 'q19'
#     transition[('q19', ' ')] = 'q19'
#     transition[('q19', '(')] = 'q20'
#     transition[('q20', ' ')] = 'q20'
#     for i in var:
#         transition[('q20', i)] = 'q21'
#     transition[('q21', ' ')] = 'q21'
#     transition[('q20', i)] = 'q21'

    return transition

