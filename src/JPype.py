# -*- coding: utf-8 -*-

import jpype

# start the JVM with the good classpaths
classpath = "/home/alex/Software/jars/boilerpipe-1.2.2.jar:/home/alex/Software/jars/nekohtml-1.9.18.jar:/home/alex/Software/jars/xercesImpl.jar"
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)

# get the Java classes we want to use
DefaultExtractor = jpype.JPackage("de").l3s.boilerpipe.extractors.DefaultExtractor

# call them !
print DefaultExtractor.INSTANCE.getText(jpype.java.net.URL("https://item.jd.com/3243686.html#product-detail"))