- Main intention of Inheritance is to re-use and abstract 

- Inheritance 
	- Class containing functionality that can be reused and extended 
		- Create a subclass to extend a functionality
	- Parent class contains all its variables and methods to abstract

- Composition 
	- Reuse code without inheritance
		- Class can call the functionality normally 
	- Unlike inheritance, an interface simply describes the contract of what an object can do - Goes in hand with Dependency Injection
	- Cons 
		- Lot of boilerplate code and need to initialize all internal types
		- More wrapper methods where you simply return a inner type or method
	- Pros
		- Reduces coupling to re-used code
		- Adaptable as new requirements come in

- When to use Inheritance
	- When you have only one thing to modify and is repeated highly in system
	- Tips
		- Avoid protected member variables with direct access
		- Create a protected API from children classes to use
		- Mark all other methods as final/sealed/private