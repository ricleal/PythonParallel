from mrjob.job import MRJob

'''
Run as:

python demo1.py big_2.txt

Outputs the file statistics:
"chars"	6360209
"lines"	128457
"words"	1095695

'''


class MRWordFrequencyCount(MRJob):

  def mapper(self, _, line):
    yield "chars", len(line)
    yield "words", len(line.split())
    yield "lines", 1

  def reducer(self, key, values):
    yield key, sum(values)


if __name__ == '__main__':
  MRWordFrequencyCount.run()
