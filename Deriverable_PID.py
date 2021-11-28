def gangorra():
    PID = 0
    kp = 3
    ki = 1
    kd = 0.1
    erro = 30
    erro_passado = 0
    erro_der = 0
    erro_int = 0
    sum_erro_past = 0
    for i in range(10):
        PID = kp*(erro) + kd*(erro_der) + ki*(erro_int)
        erro_der = erro + erro_passado
        sum_erro_past += erro_passado
        erro_int = erro + sum_erro_past
        erro_passado = erro
        print(PID)

gangorra()


