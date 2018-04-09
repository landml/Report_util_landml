import time
import os
from DataFileUtil.DataFileUtilClient import DataFileUtil


def log(message, prefix_newline=False):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(('\n' if prefix_newline else '') + '{0:.2f}'.format(time.time()) + ': ' + str(message))


class CreateMultiGenomeReport:
    def __init__(self, config):
        self.config = config
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(self.callback_url)

    # Listing of the Elements of a GenomeSet
    #
    def getGenomeSet(self, obj_id, obj_data, format):
#        obj_data = get_object_data(obj_id)
        lst = ['unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk']
        domain, size, num_feat, gc_cont, num_ctg, source, gen_code, assembly, sci_name = lst
        name = obj_data['info'][1]
        if 'Domain' in obj_data['info'][10]:
            domain = obj_data['info'][10]['Domain']
        if 'Size' in obj_data['info'][10]:
            size = obj_data['info'][10]['Size']
        if 'Number features' in obj_data['info'][10]:
            num_feat = obj_data['info'][10]['Number features']
        if 'GC content' in obj_data['info'][10]:
            gc_cont = str(float(obj_data['info'][10]['GC content']) * 100)
        if 'Number contigs' in obj_data['info'][10]:
            num_ctg = obj_data['info'][10]['Number contigs']
        if 'Source' in obj_data['info'][10]:
            source = obj_data['info'][10]['Source']
        if 'Genetic code' in obj_data['info'][10]:
            gen_code = obj_data['info'][10]['Genetic code']
        if 'scientific_name' in obj_data['data']:
            sci_name = obj_data['data']['scientific_name']
        if 'assembly_ref' in obj_data['info'][10]:
            assembly = obj_data['info'][10]
        elif 'assembly_ref' in obj_data['data']:
            assembly = obj_data['data']['assembly_ref']
        elif 'contigset_ref' in obj_data['data']:
            assembly = obj_data['data']['contigset_ref']

        line = ''
        if format == 'list':
            line = name + "\n"
            line += "\tObjectID:     {0:s}\n\tScientName:   {1}\n\tSource:       {2:s}\n\tDomain:       {3:s}\n\tAssembly Ref: {4}\n".format(
                obj_id, sci_name, source, domain, assembly)
            line += "\tFeatures:     {0}\n\tContigs:      {1}\n\tPct. GC:      {2}\n\tGenetic Code: {3}\n".format(num_feat, num_ctg, gc_cont, gen_code)
        if format == 'tab':
            lst = [name, obj_id, sci_name, source, domain, assembly, num_feat, num_ctg, gc_cont, gen_code]
            line = "\t".join(lst) + "\n"
        if format == 'csv':
            lst = [name, obj_id, sci_name, source, domain, assembly, num_feat, num_ctg, gc_cont, gen_code]
            line = ",".join(lst) + "\n"
        return line


    # Metadata for a GenomeSet
    #
    def getGenomeSetMeta(self, obj_data):
        line = ''
        line += "Name         {}\n".format(obj_data['info'][1])
        line += "Type         {}\n".format(obj_data['info'][2])
        line += "Created By   {}\n".format(obj_data['info'][5])
        line += "Narrative    {}\n".format(obj_data['info'][7])
        line += "Description  {}\n".format(obj_data['data']['description'])
        line += "Num Elements {}\n".format(str(len(obj_data['data']['elements'])))
        for ele in obj_data['data']['elements']:
            line += "  Element:   {}\n".format(ele)
        return line


    # Describe a GenomeSet
    #
    def readGenomeSet(self, obj_name, pyStr, format):
        myGS = pyStr['elements']
        line = ''
        if format == 'list':
            line = "Description for: " + obj_name + "\n"
        if format == 'tabcol':
            lst = ["Name", "ObjectID", "ScientName", "Source", "Domain", "Assembly Ref", "Features", "Contigs", "Pct. GC",
                   "Genetic Code"]
            line = "\t".join(lst) + "\n"
        if format == 'cvscol':
            lst = ["Name", "ObjectID", "ScientName", "Source", "Domain", "Assembly Ref", "Features", "Contigs", "Pct. GC",
                   "Genetic Code"]
            line = ",".join(lst) + "\n"

#        data_file_cli = DataFileUtil(self.callback_url)

        for ele in myGS:
            #print ele, myGS[ele]
            #obj_id = myGS[ele]['ref']
            genome = self.dfu.get_objects({'object_refs': [myGS[ele]['ref']]})
#            genome_data = genome['data'][0]['data']
            line += self.getGenomeSet(myGS[ele]['ref'], genome['data'][0], format)

        return line


