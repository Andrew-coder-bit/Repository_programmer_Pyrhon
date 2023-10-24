a = 1024; inf_V_MB = 1.44; count_sheets = 100; count_str = 50; count_simvol = 25; v_simv = 4
result = (a * a * inf_V_MB)/(count_sheets * count_str * count_simvol * v_simv)
print("Количество книг, помещающихся на дискету:", int(result))
