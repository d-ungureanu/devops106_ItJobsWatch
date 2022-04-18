pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops106/itjobswatch:0." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_credentials'
  }

  stages {
    stage('Cloning the project from GitHub') {
      steps {
        git branch: 'jenkins',
        url: 'https://github.com/d-ungureanu/devops106_ItJobsWatch.git'
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
  }
}
