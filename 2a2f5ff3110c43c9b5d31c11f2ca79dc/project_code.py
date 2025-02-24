go// cmd/main.go
package main

import (
	"k8s-manager/pkg"
	"github.com/spf13/cobra"
	"log"
)

var rootCmd = &cobra.Command{
	Use:   "k8s-manager",
	Short: "A CLI tool to manage Kubernetes deployments and pods",
}

var deployCmd = &cobra.Command{
	Use:   "deploy [deployment|pod]",
	Short: "Deploy a Kubernetes deployment or pod",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		switch args[0] {
		case "deployment":
			pkg.DeployDeployment()
		case "pod":
			pkg.DeployPod()
		default:
			log.Fatalf("Invalid argument: %s", args[0])
		}
	},
}

var deleteCmd = &cobra.Command{
	Use:   "delete [deployment|pod]",
	Short: "Delete a Kubernetes deployment or pod",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		switch args[0] {
		case "deployment":
			pkg.DeleteDeployment()
		case "pod":
			pkg.DeletePod()
		default:
			log.Fatalf("Invalid argument: %s", args[0])
		}
	},
}

var viewCmd = &cobra.Command{
	Use:   "view [deployment|pod]",
	Short: "View information about a Kubernetes deployment or pod",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		switch args[0] {
		case "deployment":
			pkg.ViewDeployments()
		case "pod":
			pkg.ViewPods()
		default:
			log.Fatalf("Invalid argument: %s", args[0])
		}
	},
}

func init() {
	rootCmd.AddCommand(deployCmd)
	rootCmd.AddCommand(deleteCmd)
	rootCmd.AddCommand(viewCmd)
}

func main() {
	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}

// pkg/deployment.go
package pkg

import (
	"context"
	"fmt"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"log"
	"os"
)

func getClientSet() (*kubernetes.Clientset, error) {
	kubeconfig := os.Getenv("KUBECONFIG")
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		return nil, err
	}
	return kubernetes.NewForConfig(config)
}

func DeployDeployment() {
	fmt.Println("Deploying a Kubernetes deployment...")
	// Implement deployment creation logic here
}

func DeleteDeployment() {
	fmt.Println("Deleting a Kubernetes deployment...")
	// Implement deployment deletion logic here
}

func ViewDeployments() {
	clientset, err := getClientSet()
	if err != nil {
		log.Fatal(err)
	}

	deployments, err := clientset.AppsV1().Deployments("default").List(context.TODO(), metav1.ListOptions{})
	if err != nil {
		log.Fatal(err)
	}

	for _, deployment := range deployments.Items {
		fmt.Printf("Deployment: %s\n", deployment.Name)
	}
}

// pkg/pod.go
package pkg

import (
	"context"
	"fmt"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"log"
	"os"
)

func DeployPod() {
	fmt.Println("Deploying a Kubernetes pod...")
	// Implement pod creation logic here
}

func DeletePod() {
	fmt.Println("Deleting a Kubernetes pod...")
	// Implement pod deletion logic here
}

func ViewPods() {
	clientset, err := getClientSet()
	if err != nil {
		log.Fatal(err)
	}

	pods, err := clientset.CoreV1().Pods("default").List(context.TODO(), metav1.ListOptions{})
	if err != nil {
		log.Fatal(err)
	}

	for _, pod := range pods.Items {
		fmt.Printf("Pod: %s\n", pod.Name)
	}
}

// pkg/deployment_test.go
package pkg

import (
	"testing"
)

func TestDeployDeployment(t *testing.T) {
	// Test deployment creation logic
}

func TestDeleteDeployment(t *testing.T) {
	// Test deployment deletion logic
}

// pkg/pod_test.go
package pkg

import (
	"testing"
)

func TestDeployPod(t *testing.T) {
	// Test pod creation logic
}

func TestDeletePod(t *testing.T) {
	// Test pod deletion logic
}
