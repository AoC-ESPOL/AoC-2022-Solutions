# A base parser for all day's parsers.
#
# Provides the foundations on which others parsers can be built,
# as well as other utility methods.
class BaseParser
  def initialize(input)
    @pos = 0
    @input = input
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
    throw "Expected '#{expected}', but got '#{actual}'" if expected != actual
  end

  def parse
    throw 'Not implemented'
  end

  def digits
    yield advance.to_i while peek =~ /\d/
  end

  def parse_number
    n = 0
    digits do |digit|
      n = n * 10 + digit
    end
    n
  end
end
