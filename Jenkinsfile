pipeline {
    agent { label 'jenkins-agent' }
    stages {
        stage('build') {
            steps {
                script {
                   withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                       sh """
                            docker login -u ${USERNAME} -p ${PASSWORD}
                            docker build -t abdullahelkasaby/fast-api:v${BUILD_NUMBER} .
                            docker push abdullahelkasaby/fast-api:v${BUILD_NUMBER}
                       """
                   }
                }
            }
        }
        stage('deploy') {
            steps {
                script {
                      withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                            sh '''
                                export release_exists=`helm list --short | grep model`
                                if [ -z $release_exists ]
                                then 
                                    helm install model-api helm-chart/ --set image.tag=v${BUILD_NUMBER}
                                else
                                    helm upgrade model-api helm-chart/ --set image.tag=v${BUILD_NUMBER}
                                fi
                            '''
                        }
                }
            }
        }
    }
}
