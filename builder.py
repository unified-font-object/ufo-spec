import os
import shutil
import textile
import re

baseDirectory = os.path.dirname(__file__)
sourceDirectory = os.path.join(baseDirectory, "source")
siteDirectory = os.path.join(baseDirectory, "site")
templatePath = os.path.join(sourceDirectory, "template.html")
mediaDirectory = os.path.join(siteDirectory, "media")

f = open(templatePath)
templateText = f.read()
f.close()

# remove old site
if os.path.exists(siteDirectory):
    shutil.rmtree(siteDirectory)

# copy the source tree
shutil.copytree(sourceDirectory, siteDirectory)

# convert textile documents to html documents
navigationRE = re.compile(
    "<!-- Navigation URL: [\w/.]+ -->"
)

def convertPages(directory, currentDepth=0):
    for fileName in os.listdir(directory):
        path = os.path.join(directory, fileName)
        if os.path.isdir(path):
            convertPages(path, currentDepth=currentDepth+1)
        elif os.path.splitext(fileName)[-1] == ".textile":
            print "Converting %s..." % fileName
            # make the html path
            htmlName = os.path.splitext(fileName)[0] + ".html"
            htmlPath = os.path.join(directory, htmlName)
            # read the raw text
            f = open(path, "rb")
            text = f.read()
            f.close()
            # convert
            processedText = textile.textile(text)
            html = templateText.replace("<!-- textile content -->", processedText)
            # insert the sub navigation if available
            navigationstubPath = os.path.join(directory, "navigationstub.html")
            if os.path.exists(navigationstubPath):
                f = open(navigationstubPath, "rb")
                navigationStub = f.read()
                f.close()
                pattern = "<!-- Navigation: %s -->" % directory[len(siteDirectory) + 1:]
                html = html.replace(pattern, navigationStub)
            # set the media root
            html = html.replace("<!-- Media Root -->", os.path.relpath(mediaDirectory, os.path.dirname(htmlPath)))
            # set the navigation links
            for comment in navigationRE.findall(html):
                url = comment.split(" ")[3]
                url = os.path.relpath(os.path.join(siteDirectory, url), htmlPath)
                url = url[3:]
                html = html.replace(comment, url)
            # write the html
            f = open(htmlPath, "wb")
            f.write(html)
            f.close()

convertPages(siteDirectory)

# filter out unneeded files

allowedTypes = [
    ".html",
    ".css",
    ".js",
    ".png"
]
allowedExceptions = [
    os.path.join(siteDirectory, "downloads/UFODocumentIcon.zip")
]
mustRemove = [
    os.path.join(siteDirectory, "template.html"),
    os.path.join(siteDirectory, "versions/ufo1/navigationstub.html"),
    os.path.join(siteDirectory, "versions/ufo2/navigationstub.html"),
]

def filterJunk(directory):
    for fileName in os.listdir(directory):
        path = os.path.join(directory, fileName)
        # hidden, svn
        if fileName.startswith("."):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            continue
        # directory
        if os.path.isdir(path):
            filterJunk(path)
        # allowed exceptions
        elif path in allowedExceptions:
            continue
        # allowed file types
        elif os.path.splitext(fileName)[-1] not in allowedTypes:
            os.remove(path)

filterJunk(siteDirectory)

for path in mustRemove:
    os.remove(path)
