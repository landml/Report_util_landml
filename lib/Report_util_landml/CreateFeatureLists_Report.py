import time

def log(message, prefix_newline=False):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(('\n' if prefix_newline else '') + '{0:.2f}'.format(time.time()) + ': ' + str(message))


class CreateFeatureLists:
    def __init__(self, config):
        self.config = config

    # -----------------------------------------------------------------
    #    Create a Delimited Table version of the genes in a genome
    #


    def delimitedTable(self, genome, format, features):
        line = ""
        lineList = ["Feature ID", "Feature type", "Contig", "Location", "Strand", "Feature function", "Aliases"]
        if format == 'tab':
            line += "\t".join(lineList) + "\n"
        else:
            line += ",".join(lineList) + "\n"
        for feat in genome[features]:
            if 'function' not in feat:
                feat['function'] = 'unknown'

            aliases = ''
            if 'aliases' in feat:
                aliases = ', '.join(feat['aliases'])
            if 'type' not in feat:
                feat['type'] = features

            location = ''
            contig = ''
            strand = ''
            if len(feat['location']) > 0:
                locList = []
                # For those REALLY rare occassions when there is more than one location in Prokaryotes
                for loc in feat['location']:
                    contig = loc[0]
                    strand = loc[2]
                    if strand == '+':
                        start = loc[1]
                        stop = loc[1] + loc[3] - 1
                    else:
                        start = loc[1]
                        stop = loc[1] - loc[3] + 1
                    locList.append(str(start) + '..' + str(stop))

                location = ", ".join(locList)

            if format == 'tab':
                lineList = [feat['id'], feat['type'], contig, location, strand, feat['function'], aliases]
                line += "\t".join(lineList) + "\n"
            else:
                feat['function'] = '"' + feat['function'] + '"'
                aliases = '"' + aliases + '"'
                location = '"' + location + '"'
                lineList = [feat['id'], feat['type'], contig, location, strand, feat['function'], aliases]
                line += ",".join(lineList) + "\n"

        return line

        # -----------------------------------------------------------------
        #    Create a GFF3 version of the features in a genome
        #


    def gff3(self, genome, features):
        line = ""
        for feat in genome[features]:
            if 'function' not in feat:
                feat['function'] = 'unknown'

            aliases = ''
            if 'aliases' in feat:
                aliases = ':'.join(feat['aliases'])

            if 'type' not in feat:
                feat['type'] = features

            location = ''
            contig = ''
            strand = ''
            start = 0
            stop = 0
            if len(feat['location']) > 0:
                locList = []
                # For those REALLY rare occassions when there is more than one location in Prokaryotes
                for loc in feat['location']:
                    contig = loc[0]
                    strand = loc[2]
                    if strand == '+':
                        start = loc[1]
                        stop = loc[1] + loc[3] - 1
                        locList.append(str(start) + '..' + str(stop))
                    else:
                        start = loc[1]
                        stop = loc[1] - loc[3] + 1
                        locList.append(str(start) + '..' + str(stop))

                location = ", ".join(locList)

            ph = "."  # Placeholder for missing data
            attrib = "ID=" + feat['id']
            if feat['function'] != 'unknown':
                attrib += ";FUNCTION=" + feat['function']
            if aliases > '     ':
                attrib += ";ALIASES=" + aliases

            lineList = [contig, ph, feat['type'], str(start), str(stop), ph, strand, ph, attrib]
            line += "\t".join(lineList) + "\n"

        return line



    # -----------------------------------------------------------------
    #   Domain Annotation Reports
    #

    #   OBJECT: DomainAnnotation
    #   FUNCTION: User-defined function to format all the domains for a gene
    #
    def printGeneDomain(self, contig, geneName, geneDomain, format, cutoff):
        line = ""
        lineList = ""
        for domain in geneDomain:
            list = geneDomain[domain]
            if list[0][2] < cutoff:
                lineList = [contig, geneName, domain, str(list[0][2]), str(list[0][0]), str(list[0][1])]
                if format == 'tab':
                    line += "\t".join(lineList)
                elif format == 'csv':
                    line += ",".join(lineList)
                #            print line
                line += "\n"
        return line


    #
    #   OBJECT: DomainAnnotation
    #   FORMAT: tab or comma delimited list of the genes, domains, e-values, and start/stop of domain hit
    #   Loop through all of the contigs and get all of the genes
    #   Uses printGeneDomain to print out individual lines
    #
    def readDomainAnnList(self, pyStr, format, cutoff):
        #   Make sure the cutoff is a number
        if not isinstance(cutoff, (int, long, float, complex)):
            print "Cutoff Value must be numeric."
            return

        # Header
        line = ""
        lineList = ["Contig", "Gene ID", "Domain", "Evalue", "Start", "Stop"]

        #   Check for valid formats
        if format not in ['tab', 'csv']:
            print "Invalid format. Valid formats are tab and csv"
            return
        elif format == 'tab':
            line = "\t".join(lineList)
        elif format == 'csv':
            line = "'" + ",".join(lineList)

        # Add line-end to the header
        line += "\n"

        myData = pyStr['data']

        for contig in myData:
            contigData = myData[contig]
            for gene in contigData:
                if (gene[4]):
                    line += self.printGeneDomain(contig, gene[0], gene[4], format, cutoff)

        return line


    #
    #   OBJECT: DomainAnnotation
    #   FUNCTION: User-defined function to count the domains for a gene
    #
    def countGeneDomain(self, contig, geneName, geneDomain, format, cutoff, myDict):
        for domain in geneDomain:
            list = geneDomain[domain]
            if list[0][2] < cutoff:
                if domain in myDict:
                    myDict[domain] += 1
                else:
                    myDict[domain] = 1

        return myDict


    #
    #   OBJECT: DomainAnnotation
    #   FORMAT: List of the domains and number of occurrences in the genome
    #   Uses countGeneDomain to get the statistics for an individual gene
    #
    def readDomainAnnCount(self, pyStr, format, cutoff):
        #   Make sure the cutoff is a number
        if not isinstance(cutoff, (int, long, float, complex)):
            print "Cutoff Value must be numeric."
            return

        # Header
        line = ""
        lineList = ["Contig", "Count"]

        #   Check for valid formats
        if format not in ['tab', 'csv']:
            print "Invalid format. Valid formats are tab and csv"
            return
        elif format == 'tab':
            line = "\t".join(lineList)
        elif format == 'csv':
            line = "'" + ",".join(lineList)

        # Add line-end to the header
        line += "\n"

        myData = pyStr['data']
        count = 0
        myDict = {}
        for contig in myData:
            contigData = myData[contig]

            for gene in contigData:
                if (gene[4]):
                    myDict = self.countGeneDomain(contig, gene[0], gene[4], format, cutoff, myDict)

        domainList = myDict.keys()
        domainList.sort()
        for domain in domainList:
            lineList = [domain, str(myDict[domain])]
            if format == 'tab':
                line += "\t".join(lineList)
            elif format == 'csv':
                line += ",".join(lineList)
            line += "\n"

        return line


print "Done"