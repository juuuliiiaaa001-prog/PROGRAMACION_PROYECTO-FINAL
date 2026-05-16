
def colores():
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    RESET  = '\033[0m'
    return RED, GREEN, YELLOW, RESET

def ilustracion(color):

    RED, GREEN, YELLOW, RESET = colores()


    a = f'''
    _______________________________
    |      {color[0]}o|______11_____|o {RESET}     |   
    |         {color[0]}o o o o o o  {RESET}       |
    |{color[1]}_o_{RESET}                      {color[2]} _o_{RESET}|
    |{color[1]}_1_| {RESET}                    {color[2]}|_2_{RESET}|
    |{color[1]} o {RESET}                       {color[2]} o {RESET}|     
    |{color[3]}_o_{RESET}     {color[4]} _o_{RESET}    {color[5]} _o_{RESET}     {color[6]} _o_{RESET}|
    |{color[3]}_3_|{RESET}   {color[4]}o|_4_|o{RESET} {color[5]}o|_5_|o{RESET}   {color[6]}|_6_{RESET}|
    | {color[3]}o {RESET}       {color[4]}o {RESET}     {color[5]} o {RESET}      {color[6]} o {RESET}|
    |{color[7]}_o_{RESET}      {color[8]}_o_{RESET}     {color[9]}_o_{RESET}     {color[10]}__o_{RESET}|
    |{color[7]}_7_|{RESET}   {color[8]}o|_8_|o{RESET} {color[9]}o|_9_|o{RESET}  {color[10]}|_10_{RESET}|
    | {color[7]}o {RESET}      {color[8]} o {RESET}     {color[9]} o {RESET}      {color[10]} o {RESET}|    
    |            _____            |
    |___________|_____|___________|
    '''

    
    print(a)

    return a
    

