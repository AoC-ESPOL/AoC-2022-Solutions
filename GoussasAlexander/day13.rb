class Parser
  def initialize(input)
    @input = input
    @pos = 0
  end

  def advance
    @pos += 1
    @input[@pos - 1]
  end

  def peek
    @input[@pos]
  end

  def consume(expected)
    actual = advance
    return unless expected != actual

    throw "Expected #{expected} but got #{actual}"
  end

  def parse
    case peek
    when '[' then parse_ary
    else parse_number
    end
  end

  def parse_number
    n = ''
    n << advance while peek =~ /\d/
    n.to_i
  end

  def parse_ary
    return nil if advance != '['

    ary = []
    while peek != ']'
      ary.push(parse)
      advance if peek == ','
    end
    consume(']')
    ary
  end
end

def pair_order(fst, snd)
  if fst.is_a?(Numeric) && snd.is_a?(Numeric)
    fst <=> snd
  elsif fst.is_a?(Numeric) && snd.is_a?(Array)
    pair_order([fst], snd)
  elsif snd.is_a?(Numeric) && fst.is_a?(Array)
    pair_order(fst, [snd])
  elsif fst.is_a?(Array) && snd.is_a?(Array)
    fst.zip(snd)
       .map { |x, y| pair_order(x, y) }
       .filter { |order| !order.zero? }
       .first || (fst.length <=> snd.length)
  elsif fst.nil?
    -1
  elsif snd.nil?
    1
  else
    throw "Unexpected types: #{fst.class} and #{snd.class}"
  end
end

def part_one(input)
  input
    .split(/\n\n/)
    .each
    .map { |pair| pair.split(/\n/).map { |line| Parser.new(line).parse } }
    .each_with_index
    .map { |pair, i| pair_order(pair[0], pair[1]).negative? ? i + 1 : 0 }
    .sum
end

def part_two(input)
  input
    .gsub(/\n\n/, "\n")
    .lines
    .map { |line| Parser.new(line).parse }
    .concat([[[2]], [[6]]])
    .sort { |x, y| pair_order(x, y) }
    .each_with_index
    .filter { |p, _| [[[2]], [[6]]].include?(p) }
    .map { |_, idx| idx + 1 }
    .inject(:*)
end

sample_input = <<~INPUT
  [1,1,3,1,1]
  [1,1,5,1,1]

  [[1],[2,3,4]]
  [[1],4]

  [9]
  [[8,7,6]]

  [[4,4],4,4]
  [[4,4],4,4,4]

  [7,7,7,7]
  [7,7,7]

  []
  [3]

  [[[]]]
  [[]]

  [1,[2,[3,[4,[5,6,7]]]],8,9]
  [1,[2,[3,[4,[5,6,0]]]],8,9]
INPUT

puzzle_input = File.read('day13.txt')
# puts part_one sample_input
puts part_one puzzle_input
puts part_two puzzle_input
