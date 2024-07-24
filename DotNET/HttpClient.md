## Provides a class for sending HTTP requests and receiving HTTP responses from a resource identified by a URI

- Basic Implementation
	- But Causes circuit exhaustion on traffic increase
```csharp
using var httpclient = new {baseAddress = new Uri("<urlendpoint>")}
```

- Initializing in class level and reusing same client instance
	- But if DNS ttl expires and domain now points to new IP, it will fail

### Solution

- [Typed clients](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-6.0#typed-clients)  
	- Register in services and inject it in the class
```csharp
services.AddHttpClient<IDemoClient, DemoClient>(client => {
	client.BaseAddress = new Uri("<urlendpoint>")
})
```

Even though the service is Transient, the `httpclient` factory gives a reusable handler(`disposablehandle: false` ) fixing both DNS and circuit exhaustion issue

- [Named clients](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-6.0#named-clients)