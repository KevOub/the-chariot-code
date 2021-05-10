package _

import (
	"bufio"
	"flag"
	"io/ioutil"
	"log"
	"os"
)

func main() {

	// THE FLAGS FOR CRACKING
	var intervalFlag = flag.Int("i", 1, "the inteval to go at")
	var offsetFlag = flag.Int("o", 1024, "the offset to go at")
	var wrapperFlag = flag.String("w", "", "the wrapper to read from")
	var modeFlag = flag.String("b", "B", "the mode to run as")

	flag.Parse()

	INTERVAL := *intervalFlag
	OFFSET := *offsetFlag
	WRAPPERNAME := *wrapperFlag
	MODE := *modeFlag

	// fmt.Printf("INTERVAL %d OFFSET %d\n", INTERVAL, OFFSET)
	SENTINEL := []byte{0x0, 0xff, 0x0, 0x0, 0xff, 0x0}

	var err error
	var data []byte
	data, err = ioutil.ReadFile(WRAPPERNAME)
	if err != nil {
		log.Fatal("FAILED TO READ FILE")
	}

	if MODE == "B" {
		output := RetrieveByteMode(data, SENTINEL, INTERVAL, OFFSET)
		if output != nil {
			f := bufio.NewWriter(os.Stdout)
			defer f.Flush()
			f.Write(output)

		}
	}

	if MODE == "b" {
		output := RetrieveBitMode(data, SENTINEL, INTERVAL, OFFSET)
		if output != nil {
			f := bufio.NewWriter(os.Stdout)
			defer f.Flush()
			f.Write(output)

		}
	}

}

func RetrieveBitMode(wrapper []byte, SENTINEL []byte, INTERVAL int, OFFSET int) []byte {
	// i := 0
	var b byte
	poker := OFFSET
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
				poker += INTERVAL
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
		poker += INTERVAL

	}

	return nil

}

func RetrieveByteMode(wrapper []byte, SENTINEL []byte, INTERVAL int, OFFSET int) []byte {
	i := 0
	poker := OFFSET
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

		poker += INTERVAL
		output = append(output, b)
		i++
	}

	return nil

}
