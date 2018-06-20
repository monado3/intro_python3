#fileobj=open(filename,mode)
poem='''There was a young lady named Bright,\n\
Whose speef was far faster than light;\n\
She started one day\n\
In a relative way,\n\
And returned on the previous night.'''
print(len(poem))

fout=open('relativity','wt')
print(fout.write(poem))
fout.close()

fout2=open('relativity2','wt')
print(poem,file=fout2)
fout2.close()
