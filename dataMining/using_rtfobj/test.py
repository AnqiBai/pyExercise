from oletools import rtfobj

for index, data in rtfobj.rtf_iter_objects("sample.rtf"):
    print "haha"
    print 'found object size %d at index %08X' % (len(data), index)