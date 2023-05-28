pipeline {
    agent { label 'jenkins-agent' }
    stages {
        stage('build') {
            steps {
                script {
                   withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                       sh """
                            docker login -u $USERNAME -p $PASSWORD
                            docker build -t abdullahelkasaby/fast-api:${BUILD_NUMBER} .
                            docker push abdullahelkasaby/fast-api:${BUILD_NUMBER}
                       """
                   }
                }
            }
        }
        stage('deploy') {
            steps {
                script {
                  withCredentials([file(credentialsId: 'kube-cnfig-id', variable: 'KUBECONFIG')]) {
                      sh """
                          mv Deployment/api-deploy.yaml Deployment/api-deploy.yaml.tmp
                          cat Deployment/api-deploy.yaml.tmp | envsubst > Deployment/api-deploy.yaml
                          rm -f Deployment/api-deploy.yaml.tmp
                          kubectl apply -f Deployment -n default
                        """
                  }
                }
            }
        }
    }
}