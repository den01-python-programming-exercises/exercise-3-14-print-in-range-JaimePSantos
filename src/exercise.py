def main():
    #write your code below this line
    numbers = []


def print_numbers_in_range(numbers, lower_limit, upper_limit):
  print("The numbers in the range [%s, %s]"%(lower_limit,upper_limit))
  for number in numbers:
    if(number>=lower_limit and number <= upper_limit):
      print(number)

if __name__ == '__main__':
    main()
