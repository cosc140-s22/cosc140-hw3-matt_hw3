#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  brokenURL = (url.split('://'))[1]
  scheme = (url.split('://'))[0]
  if scheme != "http" and scheme != "https":
    return False 
  if url.count('?') > 1 and url.count('#') > 1:
    return False
  if url.count(' ') > 0:
    return False
  if url.count('?') == 1 and url.count('#') == 1:
    if url.find('?') < url.find('#'):
      return False
  if brokenURL.find('/') == -1:
    return False
  if brokenURL.count('/') == 1 and brokenURL.count(':') == 1:
    if brokenURL.find('/') < brokenURL.find(':'):
      return False
  if brokenURL.count(':') == 1:
    port = (((brokenURL.split(':'))[1]).split('/'))[0]
    for char in port:
      if char.isdigit() == False:
        return False
  hostName = (brokenURL.split('/'))[0]
  if len(hostName) < 0:
    return False 
  return True


def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")

testurl()
