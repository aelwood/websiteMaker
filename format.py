#!/usr/bin/python
import glob
import optparse

parser = optparse.OptionParser()
parser.add_option("-t","--title",type='string',default=None)
parser.add_option("-c","--combine",type='string',default="*.png")
options,_ = parser.parse_args()

fd = open('index.html', 'w')
fd.write("""
<html>
<head>
  <title>{TITLE}</title>
</head>
<body>
""".format(TITLE = options.title))

for myfile in glob.glob(options.combine):
  fd.write('  <a href="%s">\n' % myfile)
  fd.write('    <img width="400px" src="%s"/>\n' % myfile)
  fd.write('</a>\b')

fd.write("""
</body>
</html>
""")
fd.close()
