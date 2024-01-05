    def convert(self, s: str, numRows: int) -> str:
      start,step = 0, 1
      lst = [''] * numRows
      if len(s) < numRows or numRows == 1:
          return s
      for letter in s:
          if start == (numRows - 1):
              step = -1
          elif start == 0:
              step = 1
          lst[start] += letter
          start += step
      return ''.join(lst)
