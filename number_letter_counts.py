# function to convert the digit to words
def convert_to_words(n):
    if n == 0:
        return "Zero"
    units = ["", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten", 
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"
             ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", 
            "seventy", "eighty", "ninety"
            ]
    multiplier = ["", "thousand", "million", "billion"]

    res = ""
    group = 0

    while n > 0:
        if n % 1000 != 0:
            value = n%1000
            temp = ""

            # Handle 3 digit number
            if value >= 100:
                temp = units[value // 100] + " Hundred"
                value %= 100
                if value > 0:
                    temp += " and "

            # Handle 2 digit number
            if value >= 20:
                temp += tens[value // 10]
                value %= 10
                if value > 0:
                    temp += "-"+ units[value]
            elif value > 0:
                temp += units[value]

            if multiplier[group]:
                temp += " " + multiplier[group]

            res = temp + " " + res
        n //= 1000
        group += 1
    
    return res.strip()

total = 0
for i in range(1,1001): # traversing 1 to 1000
    temp = convert_to_words(i) 
    count = 0
    for j in temp: # traversing each character in the word
        if j.isalpha(): # alphabet checking
            count = count + 1
    total = total + count

print("How many letter would be used: ",total)




        
