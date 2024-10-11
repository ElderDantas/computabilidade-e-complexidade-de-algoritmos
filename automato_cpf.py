def mascara_cpf (cpf):
    estado = 'q0'
    resultado = ""
    
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido, tente novamente."
    
    for i, char in enumerate(cpf):
        if estado == 'q0':
            char = 'X'
            estado = 'q1'
        elif estado == 'q1':
            char = 'X'
            estado = 'q2'
        elif estado == 'q2':
            char = 'X'
            estado = 'q3'
        elif estado == 'q3':
            estado = 'q4'
        elif estado == 'q4':
            estado = 'q5'
        elif estado == 'q5':
            estado = 'q6'
        elif estado == 'q6':
            estado = 'q7'
        elif estado == 'q7':
            estado = 'q8'
        elif estado == 'q8':
            estado = 'q9'
        elif estado == 'q9':
            char = 'X'
            estado = 'q10'
        elif estado == 'q10':
            char = 'X'
            estado = 'q_aceita'
            
        resultado += char
        
    return f"CPF mascarado com sucesso! ==> {resultado}."

# Testes
print(mascara_cpf("12345678910"))
print(mascara_cpf("9134567"))
print(mascara_cpf("13264789"))