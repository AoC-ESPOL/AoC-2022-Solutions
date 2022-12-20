require './parser'

Point = Struct.new(:x, :y) do
  def top = Point.new(x, y + 1)
  def bottom = Point.new(x, y + 1)
  def left = Point.new(x - 1, y)
  def right = Point.new(x + 1, y)
end

class Parser < BaseParser
  def parse
    parse_points
  end

  def parse_point
    x = parse_number
    consume(',')
    y = parse_number
    Point.new(x, y)
  end

  def parse_points
    points = []
    while @pos < @input.length
      points << parse_point
      break unless @pos < @input.length

      [' ', '-', '>', ' '].each do |c|
        consume(c)
      end
    end
    points
  end
end

def parse_line(line)
  Parser.new(line).parse
end

def draw_vertical_line(xpos, start, finish)
  start, finish = [start, finish].minmax
  (start..finish).each do |ypos|
    yield Point.new(xpos, ypos)
  end
end

def draw_horizontal_line(ypos, start, finish)
  start, finish = [start, finish].minmax
  (start..finish).each do |xpos|
    yield Point.new(xpos, ypos)
  end
end

def draw_line(world, start:, finish:)
  if start.x == finish.x
    draw_vertical_line(start.x, start.y, finish.y) do |point|
      world[point] = '#'
    end
  elsif start.y == finish.y
    draw_horizontal_line(start.y, start.x, finish.x) do |point|
      world[point] = '#'
    end
  else
    throw "Can't draw diagonal lines!"
  end
end

def move_particle(world:, from:)
  if !(world[from.bottom])
    from.bottom
  elsif !(world[from.bottom.left])
    from.bottom.left
  elsif !(world[from.bottom.right])
    from.bottom.right
  end
end

def parse_input(input)
  walls = input
          .lines
          .reject { |line| line.strip.empty? }
          .map { |line| parse_line(line.strip) }

  world = {}
  abyss = 0

  walls.each do |wall|
    wall.zip(wall[1..]).reject { |_, y| y.nil? }.each do |start, finish|
      abyss = finish.y if finish.y > abyss
      draw_line(world, start:, finish:)
    end
  end

  [world, abyss]
end

def part_one(input)
  world, abyss = parse_input(input)
  units_at_rest = 0

  while true
    sand_position = Point.new(500, 0)

    while (new_position = move_particle(world:, from: sand_position))
      sand_position = new_position
      break if sand_position.y > abyss
    end

    break if sand_position.y > abyss

    world[sand_position] = 'o'
    units_at_rest += 1
  end

  units_at_rest
end

def part_two(input)
  world, abyss = parse_input(input)
  floor = abyss + 2
  units_at_rest = 0

  # This makes the code slower but let's me avoid
  # modifying the move_particle method.
  1_000_000.times do |i|
    world[Point.new(i, floor)] = '#'
  end

  sand_origin = Point.new(500, 0).freeze

  while world[sand_origin] != 'o'
    sand_position = sand_origin

    while (new_position = move_particle(world:, from: sand_position))
      sand_position = new_position
      break if sand_position.y == floor
    end

    world[sand_position] = 'o'
    units_at_rest += 1
  end

  units_at_rest
end

sample_input = <<~INPUT
  498,4 -> 498,6 -> 496,6
  503,4 -> 502,4 -> 502,9 -> 494,9
INPUT

puzzle_input = File.read('day14.txt')
puts "Part one #{part_one puzzle_input}"
puts "Part two #{part_two puzzle_input}"
