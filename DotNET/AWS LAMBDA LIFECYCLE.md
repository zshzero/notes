![LifeCycle](https://res.cloudinary.com/practicaldev/image/fetch/s--6Lc7ZbQK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zcz3uej7trw3mb73c7bc.png)
- Extension Init starts all the extensions
- Runtime Init bootstrap the runtime
- Function init runs the function's static code
- Invoke phase is when we are triggering the lambda

Example:
```c#
public class Function
{
    public int Count { get; set; }

	public Function() // Code is only invoked during Init Phase
	{
		Count = 0;
	}

	// This method is called in Invoke Phase
	public string FunctionHandler(string input, ILambdaContext context)
    {
        Count++;
        Thread.Sleep(1000 * 5);
        return $"{input} - {Count}";
    }
}
```
- Variable of count is reset during :
	- a new deployment
	- shutdown of specific instance due to period of inactivity (20-30 mins)
	- Parallel calls
		- When 2 parallel calls are made , then one instance will return old value + 1 and the new instance will return value 1

- To reset count on every invocation, initialize count under `FunctionHandler`