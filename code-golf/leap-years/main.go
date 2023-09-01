package main

func main() {
	for y := 1800; y <= 2401; y++ {
		if (y%4 == 0 && y%100 != 0) || y%400 == 0 {
			println(y)
		}
	}
}
