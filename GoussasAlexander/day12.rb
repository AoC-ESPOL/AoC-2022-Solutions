module Day12
  extend self

  Graph = Struct.new(:start, :end, :vertices)

  def get_elevation_for(chr)
    case chr
    when 'S' then 0
    when 'E' then 25
    else chr.ord - 'a'.ord
    end
  end

  def parse_input(input)
    start = nil
    end_ = nil
    vertices = []

    input.lines.each_with_index do |line, i|
      vertices.push([])
      line.chars.each_with_index do |c, j|
        next if c.ord == 10

        elevation = get_elevation_for c
        start ||= ([i, j] if c == 'S')
        end_ ||= ([i, j] if c == 'E')
        vertices[i][j] = elevation
      end
    end

    Graph.new(start, end_, vertices)
  end

  def bfs(g, start:, target:)
    visited = {}
    path_to = {}
    q = [start]

    until q.empty?
      v = q.shift

      next if visited[v]

      visited[v] = true

      break if v == target

      elevation = g.vertices[v[0]][v[1]]
      top = [v[0] - 1, v[1]]
      bottom = [v[0] + 1, v[1]]
      left = [v[0], v[1] - 1]
      right = [v[0], v[1] + 1]

      if v[0].positive? && g.vertices[top[0]][top[1]] - elevation <= 1 && !(visited[top])
        path_to[top] = v
        q.push(top)
      end
      if v[0] < g.vertices.size - 1 && g.vertices[bottom[0]][bottom[1]] - elevation <= 1 && !(visited[bottom])
        path_to[bottom] = v
        q.push(bottom)
      end
      if v[1].positive? && g.vertices[left[0]][left[1]] - elevation <= 1 && !(visited[left])
        path_to[left] = v
        q.push(left)
      end
      if v[1] < g.vertices[0].size - 1 && g.vertices[right[0]][right[1]] - elevation <= 1 && !(visited[right])
        path_to[right] = v
        q.push(right)
      end
    end

    return unless visited[target]

    path_to
  end

  def steps(paths, start:, target:)
    v = start
    steps = 0
    while v != target
      v = paths[v]
      steps += 1
    end
    steps
  end

  def part_one(input)
    g = parse_input input
    paths = bfs(g, start: g.start, target: g.end)
    steps(paths, start: g.end, target: g.start)
  end

  def part_two(input)
    g = parse_input input
    shortest_path = 9_999_999_999
    g.vertices.each_with_index do |row, i|
      row.each_with_index do |elevation, j|
        next unless elevation.zero?

        path = bfs(g, start: [i, j], target: g.end)
        if path
          nsteps = steps(path, start: g.end, target: [i, j])
          shortest_path = nsteps < shortest_path ? nsteps : shortest_path
        else
          # puts "Warning: Failed to reach #{[g.end]} from #{[i, j]}"
        end
      end
    end
    shortest_path
  end
end

puzzle_input = File.read('day12.txt')
sample_input = <<~EOF
  Sabqponm
  abcryxxl
  accszExk
  acctuvwj
  abdefghi
EOF

puts "Part one: #{Day12.part_one puzzle_input}"
puts "Part two: #{Day12.part_two puzzle_input}"
