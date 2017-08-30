import re

'''Custom exceptions for roman calculator '''
class RomanError(Exception):pass
class InvalidRomanNumberError(RomanError):pass
class InvalidOperatorInputError(RomanError):pass
class InvalidOperationOutputError(RomanError):pass
class OutOfRomanValueRangeError(RomanError):pass

DecimalValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
RomanValues = "M CM D CD C XC L XL X IX V IV I".split()
RegExpressionForRomanMatch = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
DecimalRomanValues = zip(DecimalValues,RomanValues)
Map = dict(DecimalRomanValues)
        
def checkForRegMatch(roman):
   '''Checks the provided  roman value macthes with the regex provided in the RegExpressionForRomanMatch'''
   if re.match(RegExpressionForRomanMatch, roman, re.IGNORECASE)==None:
	   raise InvalidRomanNumberError('Please enter the roman number according to the rules')
	   
def inputValidation(operator,*inputs):
    '''Validates the input roman and operation inputs based on the below defined regex '''
    patternForRomanVlaues = '^(\((I|V|X|L|C|D|M)+\))*((I|V|X|L|C|D|M)+)*$'
    patternForOperator = '^[\*\-\+\/]$'
    for input in inputs:
        if re.match(patternForRomanVlaues, input,re.IGNORECASE)==None:
            raise InvalidRomanNumberError('Please enter the roman number according to the rules')              
    
    if re.match(patternForOperator, operator,re.IGNORECASE)==None:
            raise InvalidOperatorInputError('Please provide any one of the operator +,-,@,/')   
            
def checkRangeInRomanValues(input):
    '''check the roman input for the () ones so that it can proceed according to the roman rules '''
    l = input.split(')')
    temp = 0
    if len(l)>1:
        temp = romanToDecimalConverter(l[0].replace('(',''))*1000+romanToDecimalConverter(l[1])
    else:
        temp = romanToDecimalConverter(l[0])
    return str(temp)

def decToRoman(inputNum):
    '''Converts the decimal value to the roman value '''    
    result = ""
    temp= int(inputNum)
    if(temp > 0):
        for dec in DecimalValues:
            while temp>=dec:
                result+=Map[dec]
                temp-=dec
        if temp!=0:
            result+=Map[dec]
        return str(result)
    else:
        return ''
       
def checkRangeForDecimalValue(decimalNum):
    '''Check the decimal value if its outside of  '''
    intDecimalValue = int(decimalNum)
    if intDecimalValue > 3999999:
        raise OutOfRomanValueRangeError('Roman value operation is greater than 3999999 so not supported') 
    elif int(decimalNum) > 3999:
        return (("(%s)" % decToRoman(decimalNum//1000))+(decToRoman(decimalNum%1000)))
    else:
        return decToRoman(decimalNum)

def romanToDecimalConverter(inputString):
    '''Which roman values to decimal values '''
    checkForRegMatch(inputString)
    inputString=inputString.upper()
    finalDecimalValue=0
    for dec, rom in zip(DecimalValues,RomanValues):
        while inputString.startswith(rom):
            finalDecimalValue+=dec
            inputString=inputString[len(rom):]
    return finalDecimalValue

    
def arthemeticOperationsForRomanNumbers(input1,operator,input2):
    '''Main methode which performs mathamatical operations based on the two roman input and the operator '''
    inputValidation(operator,input1,input2)
    decimal_input1 = checkRangeInRomanValues(input1)
    decimal_input2 = checkRangeInRomanValues(input2)
    temp = checkRangeForDecimalValue(eval(decimal_input1+operator+decimal_input2))
    if temp == '':
        raise InvalidOperationOutputError('Result of operation is either is 0 or negative') 
    return temp