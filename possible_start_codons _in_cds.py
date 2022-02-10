def find_starts (cds):
    """ find start codons in a cds """

    start = -1
    while 1:
        start = cds.find("atg", start+1)
        if start == -1:
            break
        if start % 3:
           continue
        print "possible start codon at position %d" % start
