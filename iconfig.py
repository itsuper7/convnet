# Copyright (c) 2013, Li Sijin (lisijin7@gmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# 
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from ibasic_convdata import *
from dhmlpe_convdata import *
from util import *
from data import *
from options import *
from iconvdata import *
from noah_convdata import *
from pct_convdata import *
def register_data_provider(DataProvider):
    DataProvider.register_data_provider('largejoints8andlabels', 'LARGEJOINTS8ANDLABELS', LargeJoints8AndLabelDataProvider)
    DataProvider.register_data_provider('largejoints8andlabelsall', 'LARGEJOINTS8ANDLABELSALL', LargeJoints8AndLabelAllDataProvider)
    DataProvider.register_data_provider('largejoints8andindicatorall', 'LARGEJOINTS8ANDINDICATORALL', LargeJoints8AndIndicatorAllDataProvider)
    DataProvider.register_data_provider('largejoints8andindicatorfeatureall', 'LARGEJOINTS8ANDINDICATORFEATUREALL', LargeJoints8AndIndicatorFeatureAllDataProvider)
    DataProvider.register_data_provider('largejoints8andindicatormaskall', 'LARGEJOINTS8ANDINDICATORMASKALLDATAPROVIDER', LargeJoints8AndIndicatorMaskAllDataProvider)
    DataProvider.register_data_provider('largejtindlack_rua', 'LARGEJTINDLACK_RUA_DATAPROVIDER', LargeJtIndLack_RUA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_rla', 'LARGEJTINDLACK_RLA_DATAPROVIDER', LargeJtIndLack_RLA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_lua', 'LARGEJTINDLACK_LUA_DATAPROVIDER', LargeJtIndLack_LUA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_lla', 'LARGEJTINDLACK_LLA_DATAPROVIDER', LargeJtIndLack_LLA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_ua', 'LARGEJTINDLACK_UA_DATAPROVIDER', LargeJtIndLack_UA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_la', 'LARGEJTINDLACK_LA_DATAPROVIDER', LargeJtIndLack_LA_DataProvider)
    DataProvider.register_data_provider('largejtindlack_head', 'LARGEJTINDLACK_HEAD_DATAPROVIDER', LargeJtIndLack_HEAD_DataProvider)
    DataProvider.register_data_provider('largejtindlack_shoulder', 'LARGEJTINDLACK_SHOULDER_DATAPROVIDER', LargeJtIndLack_SHOULDER_DataProvider)
    DataProvider.register_data_provider('largejtind2', 'LARGEJTIND2_DATAPROVIDER', LargeJtInd2_DataProvider)
    DataProvider.register_data_provider('largejtind2mask', 'LARGEJTIND2MASK_DATAPROVIDER', LargeJtInd2Mask_DataProvider)
    DataProvider.register_data_provider('h36mmono', 'H36MMONODATAPROVIDER', H36MMonoDataProvider)
    DataProvider.register_data_provider('croppedimagenet', 'CROPPEDIMAGENETDATAPROVIDER', CroppedImageNetDataProvider)
    DataProvider.register_data_provider('croppeddhmlpejt', 'CROPPEDDHMLPEJOINTDATAPROVIDER', CroppedDHMLPEJointDataProvider)
    DataProvider.register_data_provider('croppeddhmlpejtocc', 'CROPPEDDHMLPEJOINTOCCDATAPROVIDER', CroppedDHMLPEJointOccDataProvider)
    DataProvider.register_data_provider('croppeddhmlpedepthjt', 'CROPPEDDHMLPEDEPTHJOINTDATAPROVIDER', CroppedDHMLPEDepthJointDataProvider)
    DataProvider.register_data_provider('croppeddhmlperelskeljt', 'CROPPEDDHMLPERELSKELJOINTDATAPROVIDER', CroppedDHMLPERelSkelJointDataProvider)
    DataProvider.register_data_provider('croppeddhmlperelskeljtlen', 'CROPPEDDHMLPERELSKELJOINTLENDATAPROVIDER', CroppedDHMLPERelSkelJointLenDataProvider)
    DataProvider.register_data_provider('pct', 'PCTDATAPROVIDERERROR', PCTDataProvider)
    DataProvider.register_data_provider('pose', 'POSE', POSEDataProvider)
    DataProvider.register_data_provider('multipose', 'MULTIPOSE', MultiPOSEDataProvider)
    DataProvider.register_data_provider('largemultipose', 'LARGEMULTIPOSE', LargeMultiPOSEDataProvider)
    DataProvider.register_data_provider('largejoints8', 'LARGEJOINTS8', LargeJoints8DataProvider)
    DataProvider.register_data_provider('croppeddhmlpejtmaxind', 'CROPPEDDHMLPEJOINTMAXINDDATAPROVIDER', CroppedDHMLPEJointMaxIndDataProvider)
    DataProvider.register_data_provider('croppeddhmlperelskeljtmaxind', 'CROPPEDDHMLPERELSKELJOINTMAXINDDATAPROVIDER', CroppedDHMLPERelSkelJointMaxIndDataProvider)
    DataProvider.register_data_provider('croppeddhmlpepairwisereljt', 'CROPPEDDHMLPEPAIRWISERELJOINTDATAPROVIDER', CroppedDHMLPEPairwiseRelJointDataProvider)
    DataProvider.register_data_provider('memfeat', 'MEMORYFEATUREDATAPROVIDER', MemoryFeatureDataProvider)
    DataProvider.register_data_provider('jt', 'JOINTDATAPROVIDER', JointDataProvider)
    DataProvider.register_data_provider('relskeljt', 'RELSKELJOINTDATAPROVIDER', RelSkelJointDataProvider)
    DataProvider.register_data_provider('croppedrelskelpairjt', 'CROPPEDDHMLPERELSKELPAIRJT', CroppedDHMLPERelSkelPairJt)
    DataProvider.register_data_provider('croppedrelskelmixjt', 'CROPPEDDHMLPERELSKELMIXJT',CroppedDHMLPERelSkelMixJt)
    DataProvider.register_data_provider('croppedrelskelmixjtlabel', 'CROPPEDDHMLPERELSKELMIXJTLABEL',CroppedDHMLPERelSkelMixJtLabel)
    DataProvider.register_data_provider('croppedrelskelmixjtplus', 'CROPPEDDHMLPERELSKELMIXJTPLUS',CroppedDHMLPERelSkelMixJtPlus)
    DataProvider.register_data_provider('croppedrelskelmixjtlabel20', 'CROPPEDDHMLPERELSKELMIXJTLABEL20', CroppedDHMLPERelSkelMixJtLabel20)
    DataProvider.register_data_provider('croppedrelskelmixjtlabel10', 'CROPPEDDHMLPERELSKELMIXJTLABEL10', CroppedDHMLPERelSkelMixJtLabel10)
    DataProvider.register_data_provider('croppedrelskelmixjtmultilabel','CROPPEDDHMLPERELSKELMIXJTMULTILABEL', CroppedDHMLPERelSkelMixJtMultiLabel)
    DataProvider.register_data_provider('croppeddhmlperelskeljtdoublelind','CROPPEDDHMLPERELSKELJOINTDOUBLELINDDATAPROVIDER',CroppedDHMLPERelSkelJointDoubleLIndDataProvider)
    DataProvider.register_data_provider('memjtpredmix', 'MEMORYJOINTPREDICTIONMIXDATAPROVIDER', MemoryJointPredictionMixDataProvider)
    DataProvider.register_data_provider('memjtpredanglemix', 'MEMORYJOINTPREDICTIONANGLEMIXDATAPROVIDER', MemoryJointPredictionAngleMixDataProvider)
    DataProvider.register_data_provider('memjtpredknnmix', 'MEMORYJOINTPREDICTIONKNNMIXDATAPROVIDER',  MemoryJointPredictionKNNMixDataProvider)
    DataProvider.register_data_provider('memjtpredknnmixlind', 'MEMORYJOINTPREDICTIONKNNMIXLINDDATAPROVIDER',MemoryJointPredictionKNNMixLIndDataProvider)
    DataProvider.register_data_provider('memjtpredknnmix_t', 'MEMORYJOINTPREDICTIONKNNMIX_T_DATAPROVIDER',MemoryJointPredictionKNNMix_T_DataProvider)
    DataProvider.register_data_provider('croppeddhmlperelskelrandjt', 'CROPPEDDHMLPERELSKELJOINTRANDJTDATAPROVIDER', CroppedDHMLPERelSkelJointRandJtDataProvider)
    DataProvider.register_data_provider('croppeddhmlperelskelrandpairjt', 'CROPPEDDHMLPERELSKELJOINTRANDPAIRJTDATAPROVIDER', CroppedDHMLPERelSkelJointRandPairJtDataProvider) 
def add_options(op):
    op.add_option("shuffle-data", "shuffle_data", IntegerOptionParser, "whether to shullfe the data", default=0)
    op.add_option("batch-size", "batch_size", IntegerOptionParser, "Determine how many data can be loaded in a batch. Note: only valid for data providing loading images directly", default=-1) 
    op.add_option("crop-border", "crop_border", IntegerOptionParser, "Cropped DP: crop border size", default=-1, set_once=True)
    op.add_option("crop-one-border", "crop_one_border", IntegerOptionParser, "Cropped side: crop  size", default=-1, set_once=True)
    op.add_option("external-meta-path", "external_meta_path", StringOptionParser, "Load [mean_image| cropped_mean_image] for external-meta", default="")

def add_dp_params(dp_params, op):
    dp_params['crop_border'] = op.get_value('crop_border')
    dp_params['batch_size'] = op.get_value('batch_size')
    dp_params['crop_one_border'] = op.get_value('crop_one_border')
    try:
        dp_params['shuffle_data'] = op.get_value('shuffle_data')
    except:
        dp_params['shuffle_data'] = 0
    try:
        dp_params['external_meta_path'] = op.get_value('external_meta_path')
        if len(dp_params['external_meta_path']) == 0:
            dp_params['external_meta_path'] = None
    except:
        dp_params['external_meta_path'] = None
