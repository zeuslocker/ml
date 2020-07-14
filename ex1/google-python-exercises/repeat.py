def repeat(str, count, exc):
  res = str * count
  if exc:
    res += '!!!'
  return res

def main():
  print(repeat('Vova ', 4, True))

if __name__ == '__main__':
  main()
