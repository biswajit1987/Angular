# ROBOT DOCS IN PROGRESS
command to build the image
`docker build -t robot .`

command to run the testsuites present in testsuties directory
`docker run -it -e SERVER_URL=http://3.15.232.59:8080/ -v $PWD/testsuites:/workspace robot`

Results will be stored in testsuites folder
