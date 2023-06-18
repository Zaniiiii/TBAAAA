def transition_tab(transition):
    var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    angka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ['+', '-', '*', '/', '%', '=', '<', '>']
    indecrement = ['++','--']
    hasil = []
    
    # Syntax for
    # < do { > 
    transition[('q0', 'd')] = 'q1'
    transition[('q1', 'o')] = 'q2'
    transition[('q2', ' ')] = 'q2'
    transition[('q2', '{')] = 'q3'
    transition[('q3', ' ')] = 'q3'
    for i in var:
        transition[('q3', 'i')] = 'q4'
    transition[('q4', ' ')] = 'ACCEPT'
#     for i in indecrement:
#         transition[('q4', '++')] = 'ACCEPT'
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

