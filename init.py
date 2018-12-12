#coding:utf8
import os
import nuke

nukePath = os.environ['NUKE_PATH']
nuke.ViewerProcess.register("AlexaV3LogC", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/AlexaV3_K1S1_LogC2Video_Rec709_EE_nuke3d.cube colorspaceIn AlexaV3LogC" % (nukePath)))
