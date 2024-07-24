- Circuit breaker can be viewed as a state machine 
	- It starts in the closed state; this is its normal state and allows the flow of requests across it. 
	- When a problem is detected the circuit breaker moves to the open state, blocking all requests for specified period. 
	- After that period elapses, the circuit breaker moves to a half-open state where the first request is treated as a test request. 
		- If request succeeds, the circuit closes and normal operation resumes
		- If request fails ,the circuit moves back to open and remains there for a specified period before once again moving to half-open.

- Basic Circuit Breaker policy 
```csharp
var basicCircuitBreakerPolicy = Policy
.HandleResult<HttpResponseMessage>(r => !r.IsSuccessStatusCode)
.OrTransientHttpError()
.CircuitBreakerAsync(<No. of FailedReq>, <WaitPeriod until test req>);
```
- Advanced Circuit Breaker policy
```csharp
var advancedCircuitBreakerPolicy = Policy
.HandleResult<HttpResponseMessage>(r => !r.IsSuccessStatusCode)
.OrTransientHttpError()
.AdvancedCircuitBreakerAsync(<% of Failures>, <Sample Duration>, <No. of requests to consider>, <WaitPeriod until test req>);
```
- It also stores last exception and last Handled Result
- Isolated state means its changed to open state manually `_circuitBreaker.Isolate()`  and has to be reset: `_circuitBreaker.Reset()` 

- Implementing Circuit Breaker is half the job, Handling the Fall Back when circuit breaker is in Open State is also important
	- Ex: When Weather API is broken, return cached values