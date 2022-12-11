#include <cassert>
#include <set>
#include <vector>

#include "DayNine.hpp"
#include "Point.hpp"

namespace aoc
{

enum class Direction
{
  Up,
  Down,
  Left,
  Right,

};

struct Move
{
  Direction direction;
  int amount;

  [[nodiscard]] static Move
  parse(const std::string& line) noexcept
  {
    Direction direction;
    int amount;

    switch (line[0])
      {
      case 'U': direction = Direction::Up; break;
      case 'D': direction = Direction::Down; break;
      case 'L': direction = Direction::Left; break;
      default: direction = Direction::Right; break;
      }

    amount = std::stoi(line.substr(2));

    return { direction, amount };
  }
};

[[nodiscard]] Point
directionToPoint(Direction direction)
{
  switch (direction)
    {
    case Direction::Left: return Point{ -1, 0 };
    case Direction::Right: return Point{ 1, 0 };
    case Direction::Down: return Point{ 0, 1 };
    default: return Point{ 0, -1 };
    }
}

[[nodiscard]] std::vector<Move>
parseInput(const std::string& input)
{
  std::vector<Move> moves{};

  size_t start = 0;
  size_t end;

  while ((end = input.find('\n', start)) != std::string::npos)
    {
      auto line = input.substr(start, end);
      start = end + 1;
      moves.push_back(Move::parse(line));
    }

  // Handle the last line, which does not have a newline.
  if (auto line = input.substr(start, end); !input.empty())
    {
      moves.push_back(Move::parse(line));
    }

  return moves;
}

Point
moveTail(Point tail, Point head)
{
  if (tail.isAdj(head)) return tail;

  auto signum = [](int x) { return x > 0 ? 1 : x == 0 ? 0 : -1; };

  auto deltaX = signum(head.x() - tail.x());
  auto deltaY = signum(head.y() - tail.y());

  return tail + Point{ deltaX, deltaY };
}

std::string
DayNine::partOne(std::string input)
{
  auto moves{ parseInput(input) };
  assert(!moves.empty());

  auto head = Point::zero();
  auto tail = Point::zero();

  std::set<Point> tailPath{};

  for (auto move : moves)
    {
      for (int i = 0; i < move.amount; i++)
        {
          head = head + directionToPoint(move.direction);
          tail = moveTail(tail, head);
          tailPath.insert(tail);
        }
    }

  return std::to_string(tailPath.size());
}

std::string
DayNine::partTwo(std::string input)
{
  auto moves{ parseInput(input) };
  assert(!moves.empty());

  Point snake[10];

  std::set<Point> tailPath{};

  for (auto move : moves)
    {
      for (int i = 0; i < move.amount; i++)
        {
          snake[0] = snake[0] + directionToPoint(move.direction);
          for (int j = 1; j < 10; j++)
            {
              snake[j] = moveTail(snake[j], snake[j - 1]);
            }

          tailPath.insert(snake[9]);
        }
    }

  return std::to_string(tailPath.size());
}

}
