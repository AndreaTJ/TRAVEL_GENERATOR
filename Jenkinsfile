pipeline {
    agent any
    stages {
        
        stage('Build'){
            steps{
                sh 'docker-compose build'
               
            }
        } 
        stage('Configure - Ansible'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
               
            }
        } 
        
        stage('Deploy'){
            steps{
                sh 'scp -i ./ssh/id_rsa docker-compose.yaml jenkins@35.188.151.251:docker-compose.yaml'
               
            }
        } 
    }
}