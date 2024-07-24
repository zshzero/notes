- When you want to do more than 1 thing to IEnumerable typed variable,  it can be prone to multiple enumerations
- Ex: Write a query to get values from db which returns a IEnumerable. First, get the count and then print the fields
	- Here, DB is called twice because Enumerables are only executed on demand
```c#
var customers = GetCustomers(); // GetCustomers() isnt called here, instead instruction to call is set in place as its values are not asked yet

Console.WriteLine(customers.Count()) // GetCustomers() is called here

foreach(var customer in GetCustomers()) // GetCustomers() is called here as well
{
	Console.WriteLine(customer.Name);
}

IEnumerable<Customer> GetCustomers()
{
	// Code to call db and return IEnumerable<Customer>
}
```
- Solution
	- Convert them to list or array as its a interface that every other type of collection inherits from