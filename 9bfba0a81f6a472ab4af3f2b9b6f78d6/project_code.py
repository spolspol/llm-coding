cpp#include <iostream>

#include <vector>

//you will write a Rectangle class with following attributes:
//location(render X and Y)
//Size
//Color
//when the rectangle object is created, it should had "location,size,color" by the following default values.
//location:rdefault_x=1
//location:rdefault_y=1
cpp

class Rectangle {
private:
    int x;
    int y;
    int width;
    int height;
    std::string color;

public:
    static const int rdefault_x = 1;
    static const int rdefault_y = 1;

    Rectangle()
        : x(rdefault_x), y(rdefault_y), width(5), height(5), color("black") {}

    Rectangle(int x, int y, int width, int height, std::string color)
        : x(x), y(y), width(width), height(height), color(color) {}

    void setLocation(int x, int y) {
        this->x = x;
        this->y = y;
    }

    void setSize(int width, int height) {
        this->width = width;
        this->height = height;
    }

    void setColor(std::string color) {
        this->color = color;
    }

    void printRectangle() const {
        std::cout << "Rectangle - Location: (" << x << ", " << y << "), Size: (" << width << "x" << height << "), Color: " << color << std::endl;
        //This function will print the rectangle properties
    }
};

