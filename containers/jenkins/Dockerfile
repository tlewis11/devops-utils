FROM jenkins/jenkins:lts
EXPOSE 8080
EXPOSE 5000
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
COPY jenkins-user /run/secrets/jenkins-user
COPY jenkins-pass /run/secrets/jenkins-pass
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
USER root
RUN curl -o /usr/share/get-pip.py https://bootstrap.pypa.io/get-pip.py 
RUN chmod 755 /usr/share/get-pip.py; /usr/share/get-pip.py
RUN pip install awscli
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
