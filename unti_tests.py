# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:36:19 2017

@author: USER_DELL_2014_06
"""

import unittest
from romanMathematicalOperations import * 

class TestRoman(unittest.TestCase):
    
    '''below are the values used for the testing '''
    listOfRomanAndIntValues = ( (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (31, 'XXXI'),
                    (50, 'L'),
                    (100, 'C'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1000, 'M'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'),
                    (4910,'(IV)CMX'),
                    (4920,'(IV)CMXX'),
                    (4974,'(IV)CMLXXIV'),
                    (5000,'(V)'),
                    (19998,'(XIX)CMXCVIII'),
                    (19999,'(XIX)CMXCIX'),
                    (20001,'(XX)I'),
                    (20002,'(XX)II'),
                    (90000,'(XC)'),
                    (100000,'(C)'),
                    (300000,'(CCC)'),
                    (750000,'(DCCL)'),
                    (1000000,'(M)'),
                    
   
                ) 
    
    '''Below are the all arthmetic operations operations, we are making use of checkRangeForDecimalValue() methode to make conversion from decimal to roman in the below test cases and because of that first we tested functionality of this mehode. '''
    def test_romanToDecimal(self):
        for integer,roman in self.listOfRomanAndIntValues:
            self.assertEqual(checkRangeForDecimalValue(integer),roman)
       
    def test_addition(self):
        for integer,roman in self.listOfRomanAndIntValues:
            self.assertEqual(arthemeticOperationsForRomanNumbers(roman,'+',roman),checkRangeForDecimalValue(integer+integer))


    def test_subtraction(self):
        for integer,roman in self.listOfRomanAndIntValues:
           self.assertEqual(arthemeticOperationsForRomanNumbers(checkRangeForDecimalValue(2*integer),'-',checkRangeForDecimalValue(integer)),checkRangeForDecimalValue(integer))

    def test_multiplication(self):
        for integer,roman in self.listOfRomanAndIntValues:
            self.assertEqual(arthemeticOperationsForRomanNumbers(roman,'*','II'),checkRangeForDecimalValue(integer*2))

    def test_devision(self):
        for integer,roman in self.listOfRomanAndIntValues:
           self.assertEqual(arthemeticOperationsForRomanNumbers(roman,'/','II'),checkRangeForDecimalValue(integer/2),msg="ssssss")
        
    '''Below is the test cases for verifiying the custom exceptions '''
    def test_assertionForInvalidRomanNumberError(self):
        self.assertRaises(InvalidRomanNumberError, arthemeticOperationsForRomanNumbers,"WWW","DDD","l")

    def test_assertionForOutOfRomanValueRangeError(self):
        self.assertRaises(OutOfRomanValueRangeError, arthemeticOperationsForRomanNumbers,"(M)","*","(M)")

    def test_assertionInvalidOperatorInputError(self):
        self.assertRaises(InvalidOperatorInputError, arthemeticOperationsForRomanNumbers,"(M)","*)","(M)")

    def test_assertionForInvalidOperationOutputError(self):
        self.assertRaises(InvalidOperationOutputError, arthemeticOperationsForRomanNumbers,"(M)","-","(M)")

   
if __name__=="__main__":
    unittest.main()