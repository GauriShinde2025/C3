import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
n = int(input("Enter an integer to compute its factorial: "))

# Call remote method
result = proxy.compute_factorial(n)

# Print the result
print(f"Factorial of {n} is: {result}")
