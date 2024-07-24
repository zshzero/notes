- Try not to map fields manually and Don't add business logic in auto mapper

- Use Direct Class Mapping
```c#
public ProductDto ToProductDto()  
{  
	return new ProductDto  
	{  
		Name = ProductName,  
		Description = ProductDescription,  
		Prick = Price + Price * 100 / VatPercentage  
	};  
}
```
- Use Implicit/Explicit Operator
```c#
public static implicit/explicit operator ProductDto(Product product)  
{  
	return new ProductDto  
	{  
		Name = ProductName,  
		Description = ProductDescription,  
		Prick = Price + Price * 100 / VatPercentage  
	};  
}
```