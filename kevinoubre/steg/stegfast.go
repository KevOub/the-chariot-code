package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"sync"

	"github.com/gabriel-vasile/mimetype"
)

// TODO make these better flags
const (
	UPPERBOUNDOFFSET   = 2048
	LOWERBOUNDOFFSET   = 108
	UPPERBOUNDINTERVAL = 8
	LOWERBOUNDINTERVAL = 1
)

func main() {
	// CLI FLAGS
	var wrapperFlag = flag.String("w", "stegged-byte.bmp", "the wrapper to read from")
	var modeFlag = flag.String("b", "B", "the mode to run as")
	flag.Parse()

	WRAPPERNAME := *wrapperFlag
	MODE := *modeFlag

	// interval := 1
	// offset := 1024

	// fmt.Printf("interval %d offset %d\n", interval, offset)
	SENTINEL := []byte{0x0, 0xff, 0x0, 0x0, 0xff, 0x0}

	// Reads file
	var err error
	var data []byte
	data, err = ioutil.ReadFile(WRAPPERNAME)
	if err != nil {
		log.Fatal("FAILED TO READ FILE")
	}

	// start of multithreading
	var wg sync.WaitGroup

	// Size of wait group
	wg.Add((UPPERBOUNDOFFSET - LOWERBOUNDOFFSET) * (UPPERBOUNDINTERVAL - LOWERBOUNDINTERVAL))

	// Go through the motions
	for i := LOWERBOUNDOFFSET; i <= UPPERBOUNDOFFSET; i++ {
		for j := LOWERBOUNDINTERVAL; j <= UPPERBOUNDINTERVAL; j++ {

			go func(i int, j int) {
				defer wg.Done()

				var output []byte

				// stringOutput := make([]byte, 0)

				if MODE == "B" {
					output = RetrieveByteMode(data, SENTINEL, j, i)
				} else {
					output = RetrieveBitMode(data, SENTINEL, j, i)
				}

				if len(output) > 0 {
					mime := mimetype.Detect(output)

					// if mime.Is("application/octet-stream") {
					// 	invalid, _ := DetectText(output)
					// 	if !invalid {
					// 		f := bufio.NewWriter(os.Stdout)
					// 		defer f.Flush()
					// 		f.Write(output)

					// 	}

					// }

					if len(mime.Extension()) > 0 {
						fmt.Printf("FOUND:\tINTERVAL %d\tOFFSET %d\n", j, i)
						fmt.Printf("\t%s\n", mime.Extension())
						defer StoreFile(output, mime.Extension(), "FOUND")
					}

				}

			}(i, j)
		}

	}
	wg.Wait()

}

func StoreFile(data []byte, extension string, name string) {
	f, err := os.Create("output/" + name + extension)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	_, err = f.Write(data)

	if err != nil {
		log.Fatal(err)
	}

}

func DetectText(data []byte) (bool, string) {
	detectedMIME := mimetype.Detect(data)

	isBinary := true
	for mime := detectedMIME; mime != nil; mime = mime.Parent() {
		if mime.Is("text/plain") {
			isBinary = false
		}
	}

	return isBinary, detectedMIME.Extension()

}

func RetrieveBitMode(wrapper []byte, SENTINEL []byte, interval int, offset int) []byte {
	// i := 0
	var b byte
	poker := offset
	stopcounter := 0
	output := make([]byte, 0)

	for {
		b = 0

		if poker >= len(wrapper) {
			break
		}

		for i := 0; i < 8; i++ {
			if poker < len(wrapper) {
				b = b | (wrapper[poker] & 0b0000001)
			}

			if i < 7 {
				b = uint8(b << 1)
				poker += interval
			}
		}

		if b == SENTINEL[stopcounter] {
			stopcounter++
		} else {
			stopcounter = 0
		}

		if stopcounter >= len(SENTINEL) {
			return output
		}

		output = append(output, b)
		poker += interval

	}

	return nil

}

func RetrieveByteMode(wrapper []byte, SENTINEL []byte, interval int, offset int) []byte {
	i := 0
	poker := offset
	stopcounter := 0

	// const SIZE = 1048576 // 2^20 b/c math.Pow is float aka not perfect

	output := make([]byte, 0)

	for {
		if poker >= len(wrapper) {
			break
		}
		b := wrapper[poker]

		if b == SENTINEL[stopcounter] {
			stopcounter++
		} else {
			stopcounter = 0
		}

		if stopcounter >= len(SENTINEL) {
			return output
		}

		// break out

		poker += interval
		output = append(output, b)
		i++
	}

	return nil

}
