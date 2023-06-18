def transition_tab(transition):
    var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    angka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ['+', '-', '*', '/', '%', '=', '<', '>']
    indecrementplus = ['+']
    indecrementneg = ['-']
    hasil = []
    
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
    for i in indecrementplus:
        transition[('q4', 'i')] = 'q5'
    for i in indecrementplus:
        transition[('q5', 'i')] = 'q6'
    transition[('q6', ';')] = 'ACCEPT'
#     transition[('q4', '-')] = 'q7'
#     transition[('q5', '-')] = 'q8'
#     transition[('q8', ';')] = 'ACCEPT'
#     for i in operator:
#         transition[('q4', i)] = 'q9'
#     transition[('q9', ' ')] = 'q9'
#     for i in var:
#         transition[('q9', i)] = 'q10'
#     transition[('q10', ';')] = 'ACCEPT'
#     transition[('q6', "1")] = 'ACCEPT'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'
    # transition[('q3', ' ')] = 'q3'


  
    return transition

