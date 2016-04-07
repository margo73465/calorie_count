height = float(raw_input('Enter your height in feet'))
weight = float(raw_input('Enter your weight in pounds'))
bmi = (weight * 4.88)/(height*height)
bmi = round(bmi, 1)    
if bmi <= 18.5:
    print 'Your BMI is ' +str(bmi) + ' and you are underweight.'
elif bmi > 18.5 and bmi  <= 25:
    print 'Your BMI is '+  str(bmi) + ' and you are normal weight.'
elif bmi > 25:
    print ' Your BMI is '+str(bmi) + ' and you are overweight.'
else:
    print 'There is an error with your input.'

