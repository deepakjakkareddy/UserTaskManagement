# UserTaskManagement
This repository contains all the source code and related files for User Task Management
# Docker hub Images
https://hub.docker.com/repository/docker/deepakjakkareddy/task-service
https://hub.docker.com/repository/docker/deepakjakkareddy/user-service
# Git repository
https://github.com/deepakjakkareddy/UserTaskManagement
# Step 1 Download the Microservices from the Docker hub using the above urls
# Step 2 Download source code files from above GIT repository
# Step 3 Apply YAML files for PostgresSQL:
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl apply -f postgres-deployment.yaml
# Step 4 Apply the manifests (Deploy to kubernetes)
kubectl apply -f task-service.yaml
kubectl apply -f user-service.yaml
# Step 5 Verify if the database is running
kubectl get pods
kubectl get services
kubectl get deployments
# Step 6 Verify if the persistence volume is created
kubectl get pv
# Step 7 The persistent volume (PV) is mounted on my host system at /mnt/data/postgres.  Since I am running Kubernetes locally through Docker Desktop, I need to create this path explicitly.
# Steps to create directory in DockerDesktop
# 1. Open Docker Desktop and make sure it is running.
# 2. Open a Terminal or Command Prompt: I have Windows, hence using Command Prompt.
# 3. Access the Docker VM where Kubernetes is running.# On Docker Desktop, you can do this using the command: docker run -it --rm --privileged --pid=host justincormack/nsenter1
# This command runs a lightweight container that gives you access to the host namespaces.
# 4. Create the Directory: Once inside the container, I created the directory by executing the following commands: mkdir -p /mnt/data/postgres
# 5. Verify the Directory: I verified that the directory has been created by listing the contents: ls /mnt/data
# 6. Exit the Container: Type exit to leave the container's shell.
