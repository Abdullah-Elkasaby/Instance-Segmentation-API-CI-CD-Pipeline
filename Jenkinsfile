pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                   withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                       sh """
                            docker login -u ${USERNAME} -p ${PASSWORD}
                            docker build -t abdullahelkasaby/fast-api:v${BUILD_NUMBER} . --network=host
                            docker push abdullahelkasaby/fast-api:v${BUILD_NUMBER}
                            echo ${BUILD_NUMBER} > ../build_num.txt
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
                                export BUILD_NUMBER=$(cat ../build_num.txt)
                                mv deployments/api-deploy.yaml deployments/api-deploy.yaml.tmp
                                cat deployments/api-deploy.yaml.tmp | envsubst > deployments/api-deploy.yaml
                                rm -rf deployments/deploy.yaml.tmp
                                kubectl apply -f deployments/namespace.yaml
                                kubectl apply -f deployments/ 
                            '''
                    }    
                }
            }
        }
    }
}
