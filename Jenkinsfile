pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Проверка...'
                checkout scm // Получение кода из репозитория
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                echo 'Развертывание...'
                script {
                    // Запуск Docker Compose для сборки и запуска контейнеров
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Тестирование...'
                script {
                    // Тестирование работоспособности сервисов
                    sh 'curl http://localhost/microservice1'
                    sh 'curl http://localhost/microservice2'
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
