if __name__ == '__main__':
    engine_displacement = input('Type the engine displacement: ')
    engine_displacement = int(engine_displacement)
    user_age = input('Type your age: ')
    user_age = int(user_age)

    if engine_displacement <= 1000:
        yearly_insurance = 150
    elif engine_displacement <= 2000:
        yearly_insurance = 200
    else:
        yearly_insurance = 300

    if user_age <= 23:
        yearly_insurance = yearly_insurance + 40
    '''
  
  fpa =  24 / 100 * etisia_asfalistra
  etisia_asfalistra = fpa + etisia_asfalistra     
  '''
    