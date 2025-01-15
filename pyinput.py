import pyinputplus
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
        print(i, digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers) # Return an int form of the (string) numbers.

response = pyinputplus.inputCustom(addsUpToTen)
print(response)