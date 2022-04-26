pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops106/itjobswatch:1." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_credentials'
  }

  stages {
    stage('Cloning the project from GitHub') {
      steps {
        checkout([
            $class: 'GitSCM', branches: [[name: '*/working']],
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

    stage('Testing the Code'){
      steps{
        script {
          sh '''
            docker run --rm -v $PWD/test-results:/reports --workdir /app $IMAGE_NAME python -m pytest tests -v --junitxml=/reports/results.xml
            ls $PWD/test-results
            '''
        }
      }

      post {
        always {
          junit testResults: '**/test-results/*.xml'
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