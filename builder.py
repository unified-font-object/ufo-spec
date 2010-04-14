import os
import shutil
import textile

baseDirectory = os.path.dirname(__file__)
sourceDirectory = os.path.join(baseDirectory, "source")
siteDirectory = os.path.join(baseDirectory, "site")
templatePath = os.path.join(sourceDirectory, "template.html")

f = open(templatePath)
templateText = f.read()
f.close()

links = [
    ("Overview",        "index.html"),
    ("File Structure",  "filestructure/index.html"),
    ("metainfo.plist",  "filestructure/metainfo.html"),
    ("fontinfo.plist",  "filestructure/fontinfo.html"),
    ("groups.plist",    "filestructure/groups.html"),
    ("kerning.plist",   "filestructure/kerning.html"),
    ("lib.plist",       "filestructure/lib.html"),
    ("features.fea",    "filestructure/features.html"),
    ("glyphs",          "filestructure/glyphs.html"),
    ("Storage Formats", "storageformats/index.html"),
    ("GLIF",            "storageformats/glif.html"),
    ("Resources",       "resources.html"),
    ("Road Map",        "roadmap.html"),
    ("Team",            "team.html"),
]

# remove old site
if os.path.exists(siteDirectory):
    shutil.rmtree(siteDirectory)
os.mkdir(siteDirectory)

# copy media
mediaSourcePath = os.path.join(sourceDirectory, "media")
mediaSitePath = os.path.join(siteDirectory, "media")
shutil.copytree(mediaSourcePath, mediaSitePath)

# copy downloads
downloadsSourcePath = os.path.join(sourceDirectory, "downloads")
downloadsSitePath = os.path.join(siteDirectory, "downloads")
shutil.copytree(downloadsSourcePath, downloadsSitePath)

# recurse through the source folders
def runFolder(directory, currentDepth=0):
    for fileName in os.listdir(directory):
        if fileName == "media":
            continue
        if fileName == "downloads":
            continue
        if fileName.startswith("."):
            continue

        print "processing %s..." % fileName

        sourcePath = os.path.join(directory, fileName)

        # work out the nesting
        subDirectories = directory.replace(sourceDirectory, "")
        if subDirectories.startswith("/"):
            subDirectories = subDirectories[1:]
        if subDirectories.endswith("/"):
            subDirectories = subDirectories[:-1]

        sitePath = os.path.join(subDirectories, fileName.replace(".textile", ".html"))
        sitePath = os.path.join(siteDirectory, sitePath)

        # make needed directory
        if os.path.isdir(sourcePath):
            os.mkdir(sitePath)
            runFolder(sourcePath, currentDepth=currentDepth+1)
        # make html
        elif fileName.endswith(".textile"):
            f = open(sourcePath, "r")
            text = f.read()
            f.close()

            html = templateText
            root = "/".join([".." for i in range(currentDepth)])
            if root:
                root += "/"

            # populate links
            for title, link in links:
                search = "<!-- %s -->" % title
                replacement = "<a href=\"%s%s\" class=\"navigation\">%s</a>" % (root, link, title)
                html = html.replace(search, replacement)

            # populate textile content
            processedText = textile.textile(text)
            html = html.replace("<!-- textile content -->", processedText)

            # assign the relative media links
            html = html.replace("<!-- Media Root -->", root)

            # write the file
            f = open(sitePath, "w")
            f.write(html)
            f.close()

# go!
runFolder(sourceDirectory)

