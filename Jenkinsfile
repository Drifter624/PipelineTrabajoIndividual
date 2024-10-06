pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                // Reemplaza la URL con tu propio repositorio
                git 'https://github.com/usuario/repo.git'
            }
        }
        
        stage('Construir Imagen Docker') {
            steps {
                script {
                    // Construir la imagen Docker con un Dockerfile desde el repositorio
                    docker.build('mi-app-simple')
                }
            }
        }

        stage('Levantar Contenedor Docker') {
            steps {
                script {
                    // Levantar el contenedor en el puerto 8085 (puedes cambiarlo)
                    docker.image('mi-app-simple').run('-d -p 8085:80')
                }
            }
        }
    }
}
