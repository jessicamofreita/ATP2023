
info=[]
file=open("diabetes_prediction_dataset.csv")
diab=0     

for linha in file:
    reader=linha.split(",")
    if "1" in reader[-1]: #retira apenas a informação dos pacientes doentes
        gender = reader[0]
        age= float(reader[1])
        hypertension=reader[2]
        heart_disease=reader[3]
        smoking_history=reader[4]
        bmi=float(reader[5])
        HbA1c=float(reader[6])
        glucose=int(reader[7])
        diabetes=reader[8]


        info.append((gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c,glucose,diabetes))
        diab+=1

         
file.close()




def sex_distribuition():
    
    F=0
    M=0
    print("                 Masculino(percentagem)       |          Feminino(percentagem)                              ")
    print("**************************************************************************************************************")
    
    for termo in info:
            if termo[0]=="Female":
                F+=1
            elif termo[0] =="Male":
                M+=1
    p_M=(M/diab)*100
    p_F=(F/diab)*100

    print(f"                      {M}({p_M:0.2f}%)            |               {F}({p_F:0.2f}%)                          ")
    
    
    


def age_distribution():
    ranges=[(0,10),(11,24),(25,29),(30,34),(35,39),(40,44),(45,49),(50,54),(55,59),(60,64),(65,69),(70,74),(75,79),(80,84),(85,89)]
    dic_ranges={range:0 for range in ranges}
    for termo in info:
        for range in ranges:
            if range[0] <= termo[1] <=range[1]:
                dic_ranges[range]+=1
    max_width = max(len(f"({range[0]}, {range[1]})") for range in ranges)
    for range,count in dic_ranges.items():
        p_R=(count/diab)*100
        formatted_range = f"({range[0]}, {range[1]})"

        print(f"                                    {formatted_range:^{max_width}}  | {count} ({p_R:0.2f}%)")
       

 



def glucose_distribution():

    intervals= [(x, x+9) for x in range(110, 321, 10)]

    dic_intervals = {interval: 0 for interval in intervals}

    for termo in info:
        for interval in intervals:
            if interval[0] <= termo[7] <= interval[1]:
                dic_intervals[interval] += 1
    max_width = max(len(f"({interval[0]}, {interval[1]})") for interval in intervals)
    for interval, count in dic_intervals.items():
        p_R = (count / diab) * 100
        formatted_range = f"({interval[0]}, {interval[1]})"


        print(f"                                    {formatted_range:^{max_width}}  | {count} ({p_R:0.2f}%)")

        


        
def Table():
    print("*********************Análise de dados de uma amostra populacional**************************")
    print("***********************Estudo de dados de pacientes diabéticos*****************************")
    print("***********************Amostra de 100000 (cem mil) indivíduos******************************")
    print("******************************8000 (oito mil) pacientes************************************")
    print("*******************************************************************************************")
    print("*******Dados em estudo: Distribuição por género, idade e niveis de glucose no sangue*******")
    print("*******************************************************************************************")
    print("*******************************************Género******************************************")
    sex_distribuition()
    print("*******************************************************************************************")
    print("********************************************Idade******************************************")

    age_distribution()
    print("*******************************************************************************************")
    print("**********************************Niveis de açúcar no sangue*******************************")
    glucose_distribution()

Table()
