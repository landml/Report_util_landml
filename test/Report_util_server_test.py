# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import shutil
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from Report_util_landml.Report_util_landmlImpl import Report_util_landml
from Report_util_landml.Report_util_landmlServer import MethodContext
from Report_util_landml.authclient import KBaseAuth as _KBaseAuth

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil

class Report_util_landmlTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('Report_util_landml'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'Report_util_landml',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = Report_util_landml(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        cls.test_filename = '92477.assembled.fna'
        cls.test_filename = 'test.fna'

        cls.test_path = os.path.join(cls.scratch,
                                          cls.test_filename)
        shutil.copy(os.path.join("data",
                                 cls.test_filename), cls.test_path)

        cls.genbank_file_name = 'minimal.gbff'
        cls.genbank_file_path = os.path.join(cls.scratch, cls.genbank_file_name)
        shutil.copy(os.path.join('data', cls.genbank_file_name), cls.genbank_file_path)

        cls.gfu = GenomeFileUtil(cls.callback_url)

        domain_data_file = 'Carsonella.Domains.json'
        cls.domain_file = os.path.join(cls.scratch, domain_data_file)
        shutil.copy(os.path.join('data', domain_data_file), cls.domain_file)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_Report_util_landml_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def load_fasta_file(self, filename, obj_name, contents):
        f = open(filename, 'w')
        f.write(contents)
        f.close()
        assemblyUtil = AssemblyUtil(self.callback_url)
        assembly_ref = assemblyUtil.save_assembly_from_fasta({'file': {'path': filename},
                                                              'workspace_name': self.getWsName(),
                                                              'assembly_name': obj_name
                                                              })
        return assembly_ref

    def get_fasta_file(self, filename, obj_name):
        assemblyUtil = AssemblyUtil(self.callback_url)
        assembly_ref = assemblyUtil.save_assembly_from_fasta({'file': {'path': filename},
                                                              'workspace_name': self.getWsName(),
                                                              'assembly_name': obj_name
                                                              })
        return assembly_ref

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def getDomainInfo(self, domain_name ):
        lib_i = 0
        if hasattr(self.__class__, 'domainInfo_list'):
            try:
                info = self.__class__.domainInfo_list[lib_i]
                name = self.__class__.domainName_list[lib_i]
                if info != None:
                    if name != domain_name:
                        self.__class__.domainInfo_list[lib_i] = None
                        self.__class__.domainName_list[lib_i] = None
                    else:
                        return info
            except:
                pass

        # 1) transform json to kbase DomainAnnotation object and upload to ws
        # create object
        with open (self.domain_file, 'r', 0) as domain_fh:
            domain_obj = json.load(domain_fh)

        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']

        domain_obj['used_dms_ref'] = 'KBasePublicGeneDomains/All'
        domain_obj['genome_ref'] = genome_ref

        provenance = [{}]
        new_obj_info = self.getWsClient().save_objects({
            'workspace': self.getWsName(),
            'objects': [
                {
                    'type': 'KBaseGeneFamilies.DomainAnnotation',
                    'data': domain_obj,
                    'name': 'test_DOMAINS',
                    'meta': {},
                    'provenance': provenance
                }
            ]})[0]

        # 2) store it
        if not hasattr(self.__class__, 'domainInfo_list'):
            self.__class__.domainInfo_list = []
            self.__class__.domainName_list = []
        for i in range(lib_i+1):
            try:
                assigned = self.__class__.domainInfo_list[i]
            except:
                self.__class__.domainInfo_list.append(None)
                self.__class__.domainName_list.append(None)

        self.__class__.domainInfo_list[lib_i] = new_obj_info
        self.__class__.domainName_list[lib_i] = domain_name

        return str(new_obj_info[6]) + "/" + str(new_obj_info[0]) + "/" + str(new_obj_info[4])

    def getGenomeSet(self):
        ref1 = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']

        genbank_file_name = 'minimal2.gbff'
        genbank_file_path = os.path.join(self.scratch, genbank_file_name)
        shutil.copy(os.path.join('data', genbank_file_name), genbank_file_path)
        ref2 = self.gfu.genbank_to_genome({'file': {'path': genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome2'
                                                    })['genome_ref']
#        genome_ref_list = [str(ref1), str(ref2)]
#
#        print "List:", genome_ref_list

        # build GenomeSet obj
        testGS = {
            'description': 'two genomes',
            'elements': dict()
        }
#        genome_scinames = dict()
#        genome_scinames['ref1'] = 'Saccharomyces cerevisiae 1'
#        genome_scinames['ref2'] = 'Saccharomyces cerevisiae 2'
#
#        for genome_ref in genome_ref_list:
#            testGS['elements'][genome_scinames[genome_ref]] = { 'ref': genome_ref }
        testGS['elements']['Saccharomyces cerevisiae 1'] = { 'ref' : ref1}
        testGS['elements']['Saccharomyces cerevisiae 2'] = { 'ref' : ref2}

        new_obj_info = self.getWsClient().save_objects({'workspace': self.getWsName(),
                                                    'objects': [
                                                        {
                                                            'type':'KBaseSearch.GenomeSet',
                                                            'data':testGS,
                                                            'name':'test_genomeset',
                                                            'meta':{},
                                                            'provenance':[
                                                                {
                                                                    'service':'kb_phylogenomics',
                                                                    'method':'test_view_fxn_profile'
                                                                }
                                                            ]
                                                        }]
                                                })[0]
#        print "NEW:", new_obj_info
#
        return str(new_obj_info[6]) + "/" + str(new_obj_info[0]) + "/" + str(new_obj_info[4])


    def mytest_assembly_metadata(self):

        assembly_ref = self.get_fasta_file(self.test_path,
                                             'TestAssembly3')
        ret = self.getImpl().assembly_metadata_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'assembly_input_ref': assembly_ref,
                                             'showContigs': 1
                                             })

        # Validate the returned data
 #       print  ret

    def mytest_genome_tab(self):
#        genome_object_name = 'test_Genome'
#        genome_ref = "1706/26/1"
        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']
        ret = self.getImpl().genome_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genome_input_ref': genome_ref,
                                             'report_format': 'tab'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_genome_gff(self):
#        genome_object_name = 'test_Genome'
#        genome_ref = "1706/26/1"
        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']
        ret = self.getImpl().genome_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genome_input_ref': genome_ref,
                                             'report_format': 'gff'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_genome_fasta(self):
#        genome_object_name = 'test_Genome'
#        genome_ref = "1706/26/1"
        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']
        ret = self.getImpl().genome_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genome_input_ref': genome_ref,
                                             'report_format': 'fasta'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_genome_mrna(self):
#        genome_object_name = 'test_Genome'
#        genome_ref = "1706/26/1"
        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']
        ret = self.getImpl().genome_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genome_input_ref': genome_ref,
                                             'report_format': 'mRNA'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_genome_DNA(self):
#        genome_object_name = 'test_Genome'
#        genome_ref = "1706/26/1"
        genome_ref = self.gfu.genbank_to_genome({'file': {'path': self.genbank_file_path},
                                                    'workspace_name': self.getWsName(),
                                                    'genome_name': 'minimal_test_genome'
                                                    })['genome_ref']
        ret = self.getImpl().genome_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genome_input_ref': genome_ref,
                                             'report_format': 'DNA'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_domain_annotation(self):
#        genome_object_name = 'test_Genome'
#        domain_ref = "14803/3/3"
        domain_ref = self.getDomainInfo('test_domain')
        ret = self.getImpl().domain_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'evalue_cutoff': '1e-20',
                                             'domain_annotation_input_ref': domain_ref,
                                             'report_format': 'tab'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def mytest_genomeset_meta(self):
#        genome_object_name = 'test_Genome'
#        genomeset_ref = "1706/37/1"
        genomeset_ref = self.getGenomeSet()
        ret = self.getImpl().genomeset_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genomeset_input_ref': genomeset_ref,
                                             'report_format': 'meta'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def test_genomeset_list(self):
#        genome_object_name = 'test_Genome'
        genomeset_ref = "1706/37/1"
#        genomeset_ref = self.getGenomeSet()
        ret = self.getImpl().genomeset_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genomeset_input_ref': genomeset_ref,
                                             'report_format': 'list'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def test_genomeset_tab(self):
#        genome_object_name = 'test_Genome'
#        genomeset_ref = "1706/37/1"
        genomeset_ref = self.getGenomeSet()
        ret = self.getImpl().genomeset_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genomeset_input_ref': genomeset_ref,
                                             'report_format': 'tab'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

    def test_genomeset_csv(self):
#        genome_object_name = 'test_Genome'
#        genomeset_ref = "1706/37/1"
        genomeset_ref = self.getGenomeSet()
        ret = self.getImpl().genomeset_report(self.getContext(),
                                            {'workspace_name': self.getWsName(),
                                             'genomeset_input_ref': genomeset_ref,
                                             'report_format': 'csv'
                                             })
        # Validate the returned data
        print  "RETURN;", ret

