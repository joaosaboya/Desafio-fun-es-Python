notas = int(input('Digite sua nota: '))   
if notas <= 100 and notas >= 90:
    print('Parabéns, você tirou A!')
elif notas <= 89 and notas >= 80:
    print('Muito bem, você tirou B!')    
elif notas <= 79 and notas >= 70:
    print('Bom trabalho, você tirou C!')    
elif notas <= 69 and notas >= 60:
    print('Fique atento, você tirou D!')    
else:
    print('Estude um pouco mais, você tirou F!')