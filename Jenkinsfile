pipeline {
    agent {
        label 'python'
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 add2numbers.py'
            }
        }
    }
}
