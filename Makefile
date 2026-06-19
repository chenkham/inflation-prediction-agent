# Define the compiler and standard flag settings
CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Isrc/include

# Target name of our final output executable binary file
TARGET   = inflation_forecaster

# Default routine rule executed when running 'make' in your terminal
all: $(TARGET)

$(TARGET): src/main.cpp
	$(CXX) $(CXXFLAGS) src/main.cpp -o $(TARGET)

# Clean utility to purge binary files safely
clean:
	rm -f $(TARGET)
