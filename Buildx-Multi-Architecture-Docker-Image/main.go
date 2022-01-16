package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Printf("Hello, my architecture is %s\n", runtime.GOOS)
}
