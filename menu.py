tb = nuke.toolbar("Nodes")
m = tb.addMenu("Lazypic", icon="lazypic_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Slate", "nuke.createNode('slate')")
