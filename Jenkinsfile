pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Получение кода из репозитория
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    // Запуск Docker Compose для сборки и запуска контейнеров
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Тестирование работоспособности сервисов
                    sh 'curl http://localhost/microservice1'
                    sh 'curl http://localhost/microservice2'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Отправка образов в реестр, если это необходимо
                    // sh 'docker push your-docker-hub-user/microservice1'
                    // sh 'docker push your-docker-hub-user/microservice2'
                }
            }
        }
    }

    post {
        always {
            // Очистка после завершения работы
            sh 'docker-compose down'
        }
    }
}
