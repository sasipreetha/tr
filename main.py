try:
  number = int(input("Enter the number :"))
  print("Entered value is ", number)
  print("Hi")
except Exception as e:
  print("The error is ", e)
  
finally:
  print("I will be executed for ever")