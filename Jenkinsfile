

pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops106/ITJobsWatch:1." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_cred'
  }
  stages {
    stage('Cloning the project from GitHub'){
      steps {
        checkout([
            $class: 'GitSCM', branches: [[name: '*/jenkins']],
            userRemoteConfigs: [[
              url: 'git@github.com:d-ungureanu/devops106_ItJobsWatch.git',
              credentialsId: 'ssh_git_cred'
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

    stage('Push to Docker Hub'){
      steps {
        script {
          docker.withRegistry('', DOCKER_CREDENTIALS){
            DOCKER_IMAGE.push()
          }
        }
      }
    }

    stage('Removing the Docker Image'){
      steps {
        sh "docker rmi $IMAGE_NAME"
      }
    }
  }
}
