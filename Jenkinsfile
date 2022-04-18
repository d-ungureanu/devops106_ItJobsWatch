pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops106/itjobswatch:0." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_credentials'
  }

  stages {
    stage('Cloning the project from GitHub') {
      steps {
        checkout([
            $class: 'GitSCM', branches: [[name: '*/jenkins']],
            userRemoteConfigs: [[
              url: 'git@github.com:d-ungureanu/devops106_ItJobsWatch.git',
              credentialsId: 'github_credentials'
              ]]
          ])
        }
      }

    stage('Build Docker Image') {
      steps {
        script {
          DOCKER_IMAGE = docker.build IMAGE_NAME
        }
      }
    }

    stage('Push to DockerHub') {
      steps {
        script {
          docker.withRegistry('', DOCKER_CREDENTIALS) {
            DOCKER_IMAGE.push()
          }
        }
      }
    }

    stage('Removing the Docker Image') {
      steps {
        sh "docker rmi $IMAGE_NAME"
      }
    }
  }
}
