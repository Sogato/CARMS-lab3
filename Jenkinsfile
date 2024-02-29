pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Проверка...'
                // Получение кода из репозитория
                checkout scm
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                echo 'Развертывание...'
                script {
                    // Определение ОС и запуск Docker Compose соответствующим образом
                    if (isUnix()) {
                        sh 'docker-compose up --build'
                    } else {
                        bat 'docker-compose up --build'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Тестирование...'
                script {
                    // Тестирование работоспособности сервисов с учетом ОС
                    if (isUnix()) {
                        sh 'curl http://localhost/microservice1'
                        sh 'curl http://localhost/microservice2'
                    } else {
                        bat 'curl http://localhost/microservice1'
                        bat 'curl http://localhost/microservice2'
                    }
                }
            }
        }
    }

    post {
        always {
            // Очистка после завершения работы с учетом ОС
            script {
                if (isUnix()) {
                    sh 'docker-compose down'
                } else {
                    bat 'docker-compose down'
                }
            }
        }
    }
}
