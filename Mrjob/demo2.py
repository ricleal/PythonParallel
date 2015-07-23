from mrjob.job import MRJob
import re

'''
Run as:

python demo2.py big_2.txt

Outputs words and number of occurences

"zakharchenko"	1
"zakharino"	1
"zakharych"	2
"zakret"	1
"zakuska"	1
"zaletaev"	2
"zanthoma"	5
"zapata"	1


'''

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

  def mapper(self, _, line):
    for word in WORD_RE.findall(line):
      yield word.lower(), 1

  def combiner(self, word, counts):
    yield word, sum(counts)

  def reducer(self, word, counts):
    yield word, sum(counts)


if __name__ == '__main__':
  MRWordFreqCount.run()
