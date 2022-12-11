//
// Created by aloussase on 12/11/22.
//

#include "Point.hpp"

namespace aoc
{

bool
Point::isAdj(Point other) const noexcept
{
  return abs(x_ - other.x()) < 2 && abs(y_ - other.y()) < 2;
}

}
