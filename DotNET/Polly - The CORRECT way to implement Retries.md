- Constant Back-off - Retry five times and pause 200ms between each call
 ```c#
Policy.Handle<FooException>()
	   .WaitAndRetryAsync(retryCount: 5, retryNumber => 
		   TimeSpan.FromMilliseconds(200));
```
- Linear Back-off - Retry and increase retry delay linearly (Here 100ms)
 ```c#
var delay = Backoff.LinearBackoff(TimeSpan.FromMilliseconds(100), retryCount: 5); // Retry after 100, 200, 300, 400, 500ms

var retryPolicy = Policy
    .Handle<FooException>()
    .WaitAndRetryAsync(delay);
```
- Exponential Back-off - Retry and increase retry delay by `initialDelay x 2^iteration`
 ```c#
var delay = Backoff.ExponentialBackoff(TimeSpan.FromMilliseconds(100), retryCount: 5); // Retry after 100, 200, 400, 800, 1600ms

var retryPolicy = Policy
    .Handle<FooException>()
    .WaitAndRetryAsync(delay);
```
- Jittered Back-off - Retry and add randomness to the wait delay
	- if there are 50 concurrent failures, and all 50 requests enter a wait-and-retry for 10 ms, then all 50 requests will hit the service again in 10 ms; potentially overwhelming the service again.
 ```c#
var delay = Backoff.DecorrelatedJitterBackoffV2(medianFirstRetryDelay: TimeSpan.FromSeconds(1), retryCount: 5);

var retryPolicy = Policy
    .Handle<FooException>()
    .WaitAndRetryAsync(delay);
```

- Http.Polly is a integration to httpclient and polly itself which can be used while registering the httpclient service itself
```c#
// Program.cs
builder.Services.AddHttpClient<IBasketService, BasketService>()
        .SetHandlerLifetime(TimeSpan.FromMinutes(5))  //Set lifetime to five minutes
        .AddPolicyHandler(GetRetryPolicy());

static IAsyncPolicy<HttpResponseMessage> GetRetryPolicy()
{
    return HttpPolicyExtensions
        .HandleTransientHttpError()
        .OrResult(msg => msg.StatusCode ==
	         System.Net.HttpStatusCode.NotFound)
        .WaitAndRetryAsync(5, retryAttempt =>
	         TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));
}
```

- Scoped implementation only for a particular call in a class 
```c#
var _retryPolicy = Policy
	.Handle<SomeExceptionType>()
	.WaitAndRetry(5, retryAttempt => 
		TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));

_retryPolicy.ExecuteAsync( () => _httpClient.GetAsync(urlpath));
```