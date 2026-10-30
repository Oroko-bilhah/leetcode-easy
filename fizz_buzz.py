# Leetcode: Fizz Buzz
# Time complexity: 0(n)
# Space complexity: 0(n)

def fizz_buzz(n):
    result = []
    
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")

        elif num % 3 == 0:
            result.append("Fizz")

        elif num % 5 == 0:
            result.append("Buzz")

        else:
            result.append(str(num))

    return result

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))