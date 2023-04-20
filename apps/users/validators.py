from rest_framework.exceptions import ValidationError

kg_nums=['770','771','772','773','774','775','776','777','778','779',
         '550','551','552','553','554','555','556','557','558','559',
         '700','701','702','703','704','705','706','707','708','709']

def validate_phone_number(phone_number):
    if phone_number[:4]!='+996':
        ValidationError('Number should start with "+996"')
    if len(phone_number)>13 and len(phone_number)<13:
        ValidationError('Numbers len should be 13')
    if phone_number[4:7] not in kg_nums:
        ValidationError('Number is not correct')

    

