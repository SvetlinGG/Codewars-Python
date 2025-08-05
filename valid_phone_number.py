
import re
def valid_phone_number(phone_number):
    pattern = r'[(]123[)]\s([0-9]{3})-([0-9]{4})'
    matches = re.findall(pattern, phone_number)

    if matches == phone_number:
        return True
    else:
        return False

result = valid_phone_number('(123) 456-7890')
#result = valid_phone_number('(1111)555 2345')
#result = valid_phone_number('(098) 123 4567')
print(result)