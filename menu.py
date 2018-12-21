import nukescripts
# Addon Menu
mb = menubar.addMenu("Lazypic")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")

# Gizmo
tb = nuke.toolbar("Nodes")
m = tb.addMenu("Lazypic", icon="lazypic_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Slate", "nuke.createNode('slate')")
m.addCommand("Draw/Timecode", "nuke.createNode('timecode')")
