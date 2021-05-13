package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"sync"
	"unicode"

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

	var IGNORESEXTENSIONS = []string{".dbf"}

	// CLI FLAGS
	var wrapperFlag = flag.String("w", "stegged-byte.bmp", "the wrapper to read from")
	var modeFlag = flag.String("b", "B", "the mode to run as")

	var upperOffsetFlag = flag.Int("ou", UPPERBOUNDOFFSET, "the upper bound offset to check")
	var lowerOffsetFlag = flag.Int("ol", LOWERBOUNDOFFSET, "the lower bound offset to check")

	var upperIntervalFlag = flag.Int("iu", UPPERBOUNDINTERVAL, "the upper bound interval to check")
	var lowerIntervalFlag = flag.Int("il", LOWERBOUNDINTERVAL, "the lower bound interval to check")

	flag.Parse()

	WRAPPERNAME := *wrapperFlag
	MODE := *modeFlag

	upperOffset := *upperOffsetFlag
	lowerOffset := *lowerOffsetFlag

	upperInterval := *upperIntervalFlag
	lowerInterval := *lowerIntervalFlag

	/*
		DISPLAY PROUDLY NOW THE FLAG DATA
	*/

	fmt.Printf("CRACKING\t%s\t\n", WRAPPERNAME)
	fmt.Printf("MODE\t\t%s\t\n", MODE)

	fmt.Printf("OFFSET\t\t%d:%d \n", lowerOffset, upperOffset)
	fmt.Printf("INTERVAL\t%d:%d \n", lowerInterval, upperInterval)

	fmt.Println("---------------------------------------------")

	// fmt.Printf("%d \n", (upperOffset-lowerOffset)*(upperInterval-lowerInterval))

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

	// stuff for finding the best string
	max := 0
	stringOutput := ""
	metadata := ""
	for i := lowerOffset; i <= upperOffset; i++ {
		for j := lowerInterval; j <= upperInterval; j++ {

			wg.Add(1)
			// concurrency start
			go func(i int, j int) {

				var output []byte

				// what mode is the system running as
				if MODE == "B" {
					output = RetrieveByteMode(data, SENTINEL, j, i)
				} else if MODE == "b" {
					output = RetrieveBitMode(data, SENTINEL, j, i)
				}

				// if we found anything
				if len(output) > 0 {

					// get the filetype
					mime := mimetype.Detect(output)

					// ensure we got a file and not gobly guck
					if len(output) >= len(SENTINEL) {

						// check if the string is printable [ignoring the sentinel] and larger than the other previous strings of code found
						if isPrintable(string(output[:len(output)-len(SENTINEL)])) && len(output) >= max {
							max = len(output)
							// Store the metadata
							metadata = fmt.Sprintf("FOUND:\tINTERVAL %d\tOFFSET %d\n", j, i)
							stringOutput = string(output)
						}

						// Otherwise it is a file
						if len(mime.Extension()) > 0 {
							// ensure I do not find the forbidden extensions
							if !contains(IGNORESEXTENSIONS, mime.Extension()) {

								fmt.Printf("FOUND:\tINTERVAL %d\tOFFSET %d\n", j, i)
								name := fmt.Sprintf("file.o.%d.i.%d", i, j)
								fmt.Printf("\t%s\n", name)
								// Saves the bytes to the disk
								StoreFile(output, mime.Extension(), name, MODE)

							}

						}

					}

				}

				defer wg.Done()

			}(i, j)

		}

	}

	// The usual best fit string is filtered by this

	wg.Wait()

	fmt.Println(metadata)
	fmt.Print(stringOutput)
	StoreFile([]byte(stringOutput), ".txt", "beststring", MODE)

}

func contains(s []string, str string) bool {
	for _, v := range s {
		if v == str {
			return true
		}
	}

	return false
}

func MakeDir(thingy string) {

	_, err := os.Stat(thingy)

	if os.IsNotExist(err) {
		errDir := os.MkdirAll(thingy, 0755)
		if errDir != nil {
			log.Fatal(err)
		}

	}

}

func StoreFile(data []byte, extension string, name string, mode string) {
	outputDir := fmt.Sprintf("output/%s/", mode)

	MakeDir(outputDir)

	f, err := os.Create(outputDir + name + extension)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	_, err = f.Write(data)

	if err != nil {
		log.Fatal(err)
	}

}

// RetrieveBitMode is straight from the PDF no explanation needed
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

// RetrieveByteMode is straight from the PDF no explanation needed
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

// Magically checks if the string is printable characters
func isPrintable(s string) bool {
	for _, c := range s {
		if c > unicode.MaxASCII || !unicode.IsPrint(c) {
			if !(c == '\n' || c == '\t' || c == '\r') {
				return false
			}
		}
	}
	return true
}
