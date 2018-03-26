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
