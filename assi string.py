text = "X-DSPAM-Confidence:    0.8475";
index = text.find('0')
nstr = text[index:]
fnum =  float(nstr)
print fnum
print "hello"
