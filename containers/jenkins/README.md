# Jenkins Docker image with automated configuration for inital user and plugins.

# Build the Image:

`docker build build_server .`

# Run container from image.
`docker run -p8080:8080 -p5000:5000 -d build_server`
 
