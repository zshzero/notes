- When Startup.cs or Program.cs (Minimal API) has lot of services registered, Add extension method in a different file instead and call it all in here
	- Differentiate the services based on the DDD layers (App, Infra, Domain, API) 
```c#
// Code in DependencyInjection.cs
public static IServiceColIection AddCaching(this IServiceCollection services, IConfiguration configuration)  
{  
	services.AddStackExchangeRedisCache(redisOptions =>  
	{  
		string connection = conFiguration.GetConnectionString("Redis")!;  
		redisOptions.ConFiguration = connection;  
	});  
	services.AddMemoryCache();  
	return services;  
}

// Code in Startup/Program.cs
service.AddCaching()
	   .AddAuthentication
	   .AddAuthorization()
```
- Drawback - There is a chance of missing a service to register and wont force you to register the missed services

- Solution - Use a Interface (IServiceInstaller) with a install method for service configuration
```c#
// Code in IServiceInstaller
public interface IServiceInstaller  
{  
	void Install(IServiceCollection services, 
		IConFiguration configuration);  
}

// Code in InfrastructureServiceInstaller
public class InfrastructureServiceInstaller : IServiceInstaller  
{  
	public void Install(IServiceCollection services, 
	IConFiguration configuration)  
	{  
		// Regsiter all the services here  
	}
}

// Code in Startup/Program.cs
public static IServiceCollection InstallServices( this IServiceCollection services, IConFiguration configuration, params Assembly[] assemblies)  
{  
	IEnumerab1e serviceInstalIers = assemblies  
		.SelectMany(a => a.DeFinedTypes)  
		.Where(IsAssignableToType<IServiceInstaller>)  
		.Select(Activator.CreateInstance)  
		.Cast();  
		
	foreach (IServiceInstaller serviceInstaller in serviceInstallers)  
	{  
		serviceInstaller.Install(services, configuration);  
	}  
	return services;
	  
	static bool IsAssignableToType(TypeInfo typeInfo) =>
		typeoFCT).IsAssignableFrom(typeInfo) &&  
		!typeInFo.IsInterFace &&  
		!typeInFo.IsAbstract; 
}

builder.Services.InstallServices(builder.Configuration,
					typeof(IServiceInstaller).Assembly);
```