yaml# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-web-app-pod
spec:
  containers:
  - name: web-app-container
    image: nginx:latest
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    env:
    - name: ENV_VAR
      value: "example"
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: web-app-config

# web-app-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: web-app-config
data:
  config.properties: |
    key1=value1
    key2=value2

# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-web-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-web-app
  template:
    metadata:
      labels:
        app: my-web-app
    spec:
      containers:
      - name: web-app-container
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        env:
        - name: ENV_VAR
          value: "example"
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
      - name: config-volume
        configMap:
          name: web-app-config

# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-web-app-service
spec:
  selector:
    app: my-web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer

# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: my-web-app-network-policy
spec:
  podSelector:
    matchLabels:
      app: my-web-app
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: my-web-app-db
    ports:
    - protocol: TCP
      port: 3306

# security-context.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-secure-pod
spec:
  securityContext:
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: secure-container
    image: nginx:latest
    ports:
    - containerPort: 80

# deployment.sh
#!/bin/bash
kubectl apply -f web-app-config.yaml
kubectl apply -f pod.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f network-policy.yaml
kubectl apply -f security-context.yaml

# test.sh
#!/bin/bash
kubectl get pods
kubectl logs my-web-app-pod
kubectl port-forward my-web-app-pod 8080:80

# monitor.sh
#!/bin/bash
kubectl get pods -w
kubectl describe pod my-web-app-pod
kubectl top pod my-web-app-pod
kubectl exec my-web-app-pod -- env

# delete.sh
#!/bin/bash
kubectl delete pod my-web-app-pod
kubectl get pods
