# Jenkins Docker image with automated configuration for inital user and plugins.

# Build the Image:

`docker build build_server .`

# Run container from image.
`docker run -p8080:8080 -p5000:5000 -d build_server`

# Use Jenkins
1. browse to http://localhost:8080
2. log in to Jenkins with the default credentials:
	Usename: admin
	Password: changeme

 
