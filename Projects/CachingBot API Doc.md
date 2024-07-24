## CachingBot API Documentation

### Specifics
- Branches - Gets all possible branches in Engineering
- Colleges - Gets all colleges under VTU
- Header - Gets a header for to fetch data from external service
- JWTAuth - Gets a valid JWT Token
- Student - Gets student result and indiviual semester marks
- Exception Middleware Extension - Generates generic error responses for failed requests
- Helpers
    - JWTAuth - Generates JWT Token
    - Shell - Runs bash command and gets us stdout
- Auth Middleware - Adds the Auth header (development environment only) 
- Logging - Log using Serilog in json format 
- Redis Service - Persists data using RedisDB in Json Format
- Dockerfile - Build app into a container
- Deployment
- Terraform Scripts
    - Create and setup a VM on Azure
- Ansible Playbook
    - Deploy Redis and App docker container on a server
