package lib

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"

	_ "exercise/statik"

	"github.com/rakyll/statik/fs"
)

func Echo() {
	stdin := bufio.NewScanner(os.Stdin)
	for stdin.Scan() {
		inputs := stdin.Text()
		fmt.Println(inputs)
		if inputs == "end" {
			break
		}
	}
}

func Hello() {
	fmt.Println("Hello world!")

	statikFS, _ := fs.New()
	r, _ := statikFS.Open("/hello.txt")
	defer r.Close()
	contents, _ := ioutil.ReadAll(r)
	fmt.Println(string(contents))
}
