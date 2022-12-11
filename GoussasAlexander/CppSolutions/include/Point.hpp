#pragma once

#include <iostream>

namespace aoc
{

class Point
{
public:
  Point() : x_{0}, y_{0} {}

  Point(int x, int y) : x_{ x }, y_{ y } {}

  [[nodiscard]] int
  x() const noexcept
  {
    return x_;
  }
  [[nodiscard]] int
  y() const noexcept
  {
    return y_;
  }

  Point
  operator+(Point other) const noexcept
  {
    return { x_ + other.x(), y_ + other.y() };
  }

  static Point
  zero() noexcept
  {
    return { 0, 0 };
  };

  [[nodiscard]] bool isAdj(Point other) const noexcept;

  bool
  operator<(const Point& other) const noexcept
  {
    if (x_ == other.x())
      {
        return y_ < other.y();
      }
    else
      {
        return x_ < other.x();
      }
  }

  friend std::ostream&
  operator<<(std::ostream& out, const Point& p)
  {
    return out << "Point{" << p.x() << ", " << p.y() << "}";
  }

private:
  int x_;
  int y_;
};

}
