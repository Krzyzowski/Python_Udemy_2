config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}
print(config)
print( )


print(len(config))
print(config.keys())

for key, value in config.items():
    print( key, ": ", value)