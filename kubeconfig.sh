# <!-- Back-end Challenge
# In the Bash script, you will need to modify the configuration file and provide some clusters and context to it. Use the --kubeconfig flag and set it to a file named kube_custom.config
# With the CLI command config, first set 2 clusters with set-cluster. The first should be called
# "development", its --server should be set to "https://0.0.1.1" and the --certificate-authority should be set to "temp_ca_file" Then add another cluster similar to the one above, except it should be called "staging" and the server should be set to "https://5.6.7.8*
# Then set 2 contexts, the first should be called "dev-frontend", the --cluser should be set to
# "development", the --namespace should be set to "frontend", and finally --user should be
# •developer". The second context should be similar to the one above, except it should be called
# "dev-staging" and it should be tied to the "staging" cluster.
# Finally, print the contents of this config file. -->

#!/bin/bash

# Setting up clusters
kubectl config set-cluster development --server="https://0.0.1.1" --certificate-authority="temp_ca_file" --kubeconfig=kube_custom.config
kubectl config set-cluster staging --server="https://5.6.7.8" --certificate-authority="temp_ca_file" --kubeconfig=kube_custom.config

# Setting up contexts
kubectl config set-context dev-frontend --cluster="development" --namespace="frontend" --user="developer" --kubeconfig=kube_custom.config
kubectl config set-context dev-staging --cluster="staging" --namespace="frontend" --user="developer" --kubeconfig=kube_custom.config

# Printing the contents of the config file
cat kube_custom.config
