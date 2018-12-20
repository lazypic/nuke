#coding:utf8
import os
import nuke

nuke.pluginAddPath("./gizmo", addToSysPath=True)
nuke.pluginAddPath("./image", addToSysPath=True)
nuke.pluginAddPath("./lib", addToSysPath=True)
nuke.pluginAddPath("./script", addToSysPath=True)

nukePath = os.environ['NUKE_PATH']
nuke.ViewerProcess.register("AlexaV3LogC", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/AlexaV3_K1S1_LogC2Video_Rec709_EE_nuke3d.cube colorspaceIn AlexaV3LogC" % (nukePath)))

# We are using Black Magic Pocket Cinema.
# Black Magic Camera : https://www.convergent-design.com/preset-luts
nuke.ViewerProcess.register("v2 Blackmagic Cinema Camera to Rec709", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/BMD_CC_EE_FILM_V2.cube colorspaceIn rec709" % (nukePath)))
nuke.ViewerProcess.register("v2 Blackmagic Production Camera4K to Rec709", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/BMD_PC_EE_FILM_V2.cube colorspaceIn rec709" % (nukePath)))
nuke.ViewerProcess.register("v1 Blackmagic Production Camera4K to Rec709", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/BMD_PC_EE_FILM_V1.cube colorspaceIn rec709" % (nukePath)))
nuke.ViewerProcess.register("v1 Blackmagic Cinema Camera to Rec709", nuke.createNode, ( "Vectorfield", "vfield_file %s/luts/BMD_CC_EE_FILM_V1.cube colorspaceIn rec709" % (nukePath)))

