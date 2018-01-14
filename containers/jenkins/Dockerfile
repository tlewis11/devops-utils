FROM jenkins/jenkins:lts
EXPOSE 8080
EXPOSE 5000
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
COPY jenkins-user /run/secrets/jenkins-user
COPY jenkins-pass /run/secrets/jenkins-pass
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
