kubectl delete svc db-service
kubectl delete svc app-service
kubectl delete svc auth-service
kubectl apply -f app-config.yaml
kubectl apply -f postgres-pv.yaml
kubectl apply -f db-deployment.yaml
kubectl apply -f db-service.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
kubectl apply -f auth-deployment.yaml
kubectl apply -f auth-service.yaml

kubectl get svc
kubectl delete pods -l app=book-app
kubectl delete pods -l app=book-db
kubectl delete pods -l app=book-auth
kubectl port-forward service/app-service 5000:5000

#kubectl rollout restart deployment book-db
#kubectl rollout restart deployment book-app