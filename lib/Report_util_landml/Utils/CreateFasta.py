# -----------------------------------------------------------------
#   Split a Sequence into 50 column chunks
#
def splitSequence(seq):
    colsz = 50
    start = 0
    lenseq = len(seq)
    line = ""

    while True:
        end = start + colsz
        if end > lenseq:
            end = lenseq
        # print seq[start:end]
        line += seq[start:end] + "\n"
        start += colsz
        if start > lenseq:
            False
            break
    return line


# -----------------------------------------------------------------
#    Create a protein Fasta file for a genome
#
def readProteinFasta(pyStr, testing):
    myFeat = pyStr['features']
    line = ""
    index = 0
    for feat in myFeat:
        if 'function' not in feat:
            feat['function'] = 'unknown'
        if 'type' in feat and feat['type'] not in ['CDS', 'gene']:
            continue

        if ('protein_translation' in feat):
            line += ">" + feat['id'] + " " + feat['function']
            line += " (len=" + str(feat['protein_translation_length']) + ")" + "\n"

            # print line
            line += splitSequence(feat['protein_translation']) + "\n"

            index += 1

        if index > 5 and testing.upper() == 'YES':
            break

    return line
