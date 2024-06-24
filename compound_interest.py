import pandas as pd #Porque se que voy a graficar.
import matplotlib.pyplot as plt

#================== FUNCIONES ==================
def init_calculator():
    print("===== Welcome to the compound interest calculator =====")
    print("1. Initial investment---")
    initial_investment = input("Initial investment: ")

    print("2. Contribution---")
    contribution_period = input("Contribución (Anual-Semestral-Trimestral-Mensual): ")
    monthly_contribution = input("Contribution amount: ")
    years_contribution_qty = input("Time in years: ")

    print("3. Interest rate---")
    estimated_interest_rate = input("Interest rate -estimated-: ")
    interest_rate_variance = input("Interest rate variance range: ")

    print("4. Capitalization---")
    capitalization_frequency = input("Capitalization frequency: ")



    compound_interest_data = {
            "initial_investment": float(initial_investment),
            "contribution": {
                    "contribution_period": contribution_period,
                    "contribution_qty": float(monthly_contribution),
                    "years_contribution_qty": int(years_contribution_qty)
                    },                        
            "interest_rate": float(estimated_interest_rate)/100,
            "capitalization": int(capitalization_frequency),
            "final_capital": float(0) 
        }
    
    return compound_interest_data

# def compound_interest_calc(ci_data):
    
#     #Para hacer más legible la fórmula
#     init_c = ci_data['initial_investment'] #Initial capital
#     contribution_period = ci_data['contribution']['contribution_period']
#     mc = ci_data['contribution']['contribution_qty'] #Monthly contribution   
#     years = ci_data['contribution']['years_contribution_qty']
#     irate = ci_data['interest_rate']#10% se interpreta como 0.1, 
#                                                    #si no da un número exorbitante.
#     i_rate_var = 0 #Interest rate variance
#     cap_freq = ci_data['capitalization']
    
#     cp = 0
    
#     if contribution_period == "Anual" or contribution_period == "anual":
#         cp = 1
#     elif contribution_period == "Semestral" or contribution_period == "semestral":
#         cp = 2
#     elif contribution_period == "Trimestral" or contribution_period == "trimestral":
#         cp = 4
#     elif contribution_period == "Mensual" or contribution_period == "mensual":
#         cp = 12
    
    
#     #Asignamos fórmulas a variables para que sea más legible
#     ci_formula = init_c * (1 + irate) ** years
#     ci_f_w_capitalization = init_c * (1 + irate/cap_freq)**(cap_freq*years)
#     ci_f_w_add_contrib = cp * mc*(
#         (
#             (1+irate/cap_freq)**(cap_freq*years) - 1) / (irate/cap_freq)
#         ) 
    
#     final_capital = ci_f_w_capitalization + ci_f_w_add_contrib
                     
#     ci_data['final_capital'] = round(final_capital, 2)
    
#     print(ci_data)
    
#     return ci_data

def compound_interest_calc(calculation_result, calc_type): 
    init_c = calculation_result['initial_investment'] #Initial capital
    contribution_period = calculation_result['contribution']['contribution_period']
    mc = calculation_result['contribution']['contribution_qty'] #Monthly contribution   
    years = calculation_result['contribution']['years_contribution_qty']
    irate = calculation_result['interest_rate']
    i_rate_var = 0 #Interest rate variance
    cap_freq = calculation_result['capitalization']
    
    cp = 0
    
    if contribution_period == "Anual" or contribution_period == "anual":
        cp = 1
    elif contribution_period == "Semestral" or contribution_period == "semestral":
        cp = 2
    elif contribution_period == "Trimestral" or contribution_period == "trimestral":
        cp = 4
    elif contribution_period == "Mensual" or contribution_period == "mensual":
        cp = 12
        
    final_annual_capital = {}
    
    years_range = range(years + 1)
    for n in years_range:
        if calc_type == "basic":
            ci_formula = init_c * (1 + irate) ** years
        elif calc_type != "basic":
            ci_f_w_capitalization = init_c * (1 + irate/cap_freq)**(cap_freq*n)
            ci_f_w_add_contrib = cp * mc*(
                 (
                     (1+irate/cap_freq)**(cap_freq*n) - 1) / (irate/cap_freq)
                 )#Si no hay contribuciones mensuales, todo va a dar 0. Con lo
                  # cual, en caso de ser así, el resultado final será solo con
                  # capitalización.
             
            final_capital = ci_f_w_capitalization + ci_f_w_add_contrib
            final_capital = round(final_capital, 2)
            
            final_annual_capital[f'{n} Year'] = final_capital           
            
            
    return final_annual_capital

def growth_plot(calculation_result):
    # years = range(len(calculation_result))
    # for year in years:
    #      plt.plot(year, calculation_result[f'{year} Year'], marker='o', linestyle='-')
    # plt.grid(True) #Grafica mál porque arranca del año 0 y no supe como arreglarlo. LPM.
    
    years = list(calculation_result.keys())
    capitals = list(calculation_result.values())

    plt.plot(years, capitals, marker='o', linestyle='-')
    plt.title('Crecimiento del Capital a lo largo de los Años')
    plt.xlabel('Años')
    plt.ylabel('Capital Final')
    plt.grid(True)
    plt.show()
    
    return 0

def variance_range_calc():
    return 0

#=============== PROGRAMA INICIAL ===============

#Puedo hacerlo en una función aparte y devolver un dict.
#Puedo hacerlo en un while y terminar de calcular con un éxit por condición.

data_calculation = init_calculator() #Inicia calculadora, falta el resultado.
calculation_result = compound_interest_calc(data_calculation, "") #Dict con result.
length = len(calculation_result) - 1
print(calculation_result[f"{length} Year"])
growth_plot(calculation_result)








