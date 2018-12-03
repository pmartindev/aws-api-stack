pipeline {
    agent none
    stages {
        stage("Run Unit Tests") {
            steps {
                echo 'Run Unit Tests'
            }
        }
        stage("Deploy CloudFormation Stack") {
            steps {
                echo 'Deploy CFT'
            }
        }
    }  
    post {
        always {
            echo 'Delete Stack'
        }
    }
}