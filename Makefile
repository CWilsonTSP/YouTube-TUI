all:
	g++ -Wall -O3 main.cpp -o youtube_tui
run:
	make all
	./youtube_tui
clean:
	rm -rf youtube_tui *.o
test:
	echo do some tests
