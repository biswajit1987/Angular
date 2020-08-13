From selenium/standalone-chrome
USER root
RUN mkdir /workspace && chmod -R 777 /workspace
WORKDIR /workspace
RUN apt update
RUN apt install python-pip -y
RUN pip install robotframework robotframework-seleniumlibrary
USER seluser
CMD python -m robot -d results /workspace 
