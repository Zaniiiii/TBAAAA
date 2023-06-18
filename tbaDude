def transisi(transition):
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ['+','-','=','*', '/', '%', '<', '>']
    
    # Syntax for
    # < do { > 
    transition[('q0', 'd')] = 'q1'
    transition[('q1', 'o')] = 'q2'
    transition[('q2', ' ')] = 'q2'
    transition[('q2', '{')] = 'q3'
    transition[('q3', ' ')] = 'q3'
    for i in letter:
        transition[('q3', i)] = 'q4'
    for i in digit:
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
    for i in letter:
        transition[('q7', i)] = 'q8'
    transition[('q8', ' ')] = 'q8'
    for i in operator:
        if i != '=' and i != '>' and i != '<':
            transition[('q8', i)] = 'q9'
    transition[('q9', ' ')] = 'q9'
    for i in letter:
        transition[('q9', i)] = 'q10'
    for i in digit:
        transition[('q9', i)] = 'q10'
    transition[('q10', ' ')] = 'q10'
    transition[('q10', ';')] = 'q11'
    transition[('q11', ' ')] = 'q12'
    transition[('q12', '}')] = 'q13'
    transition[('q13', ' ')] = 'q13'
    transition[('q13', 'w')] = 'q14'
    transition[('q14', 'h')] = 'q15'
    transition[('q15', 'i')] = 'q16'
    transition[('q16', 'l')] = 'q17'
    transition[('q17', 'e')] = 'q18'
    transition[('q18', ' ')] = 'q18'
    transition[('q18', '(')] = 'q19'
    for i in letter:
        transition[('q19', i)] = 'q20'
    transition[('q20', ' ')] = 'q20'
    for i in operator:
        if i == '=':
            transition[('q20', i)] = 'q21'
        if i == '>' or i == '<':
            transition[('q20', i)] = 'q22'
    for i in operator:
        if i == '=':
            transition[('q21', i)] = 'q23'
            transition[('q22', i)] = 'q23'
    transition[('q23', ' ')] = 'q23'
    for i in letter:
        transition[('q22', i)] = 'q24'
        transition[('q23', i)] = 'q24'
    for i in digit:
        transition[('q22', i)] = 'q24'
        transition[('q23', i)] = 'q24'
    transition[('q24', ' ')] = 'q24'
    transition[('q24', ')')] = 'q25'
    transition[('q25', ';')] = 'ACCEPT'

        

    return transition

