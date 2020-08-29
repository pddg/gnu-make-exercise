package lib

import (
	"net/http"

	"github.com/rakyll/statik/fs"
	_ "exercise/statik"
)

func RunServer() {
	statikFS, _ := fs.New()
	http.Handle("/", http.FileServer(statikFS))
	http.ListenAndServe(":8080", nil)
}