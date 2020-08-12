---
layout: default
navigation: true
order: 400
title: UFO 4
---

UFO 4 will be an extension of [UFO 3](../ufo3). Developoment is being done in the [specification's GitHub issues](https://github.com/unified-font-object/ufo-spec/issues). [Contributions are welcome!](../../contributions)

## Proposals Under Consideration

<ul id="ufo4-considering-issues"></ul>
<script type="text/javascript">   
url = "https://api.github.com/repos/unified-font-object/ufo-spec/issues?state=open&labels=ufo4,proposal,considering&per_page=1000"
fetch(url)
    .then(response => response.json())
    .then(function (json) {
        console.log(json)
        element = document.getElementById("ufo4-considering-issues")
        json.forEach(function (item) {
            li = document.createElement("li") 
            a = document.createElement("a")
            a.href = item.html_url
            a.text = item.title
            li.appendChild(a)
            element.appendChild(li) 
        })
    })
</script>

## Approved Proposals

<ul id="ufo4-approved-issues"></ul>
<script type="text/javascript">   
url = "https://api.github.com/repos/unified-font-object/ufo-spec/issues?state=open&labels=ufo4,proposal,approved&per_page=1000"
fetch(url)
    .then(response => response.json())
    .then(function (json) {
        console.log(json)
        element = document.getElementById("ufo4-approved-issues")
        json.forEach(function (item) {
            li = document.createElement("li") 
            a = document.createElement("a")
            a.href = item.html_url
            a.text = item.title
            li.appendChild(a)
            element.appendChild(li) 
        })
    })
</script>


## Rejected Proposals

<ul id="ufo4-rejected-issues"></ul>
<script type="text/javascript">   
url = "https://api.github.com/repos/unified-font-object/ufo-spec/issues?state=open&labels=ufo4,proposal,rejected&per_page=1000"
fetch(url)
    .then(response => response.json())
    .then(function (json) {
        console.log(json)
        element = document.getElementById("ufo4-rejected-issues")
        json.forEach(function (item) {
            li = document.createElement("li") 
            a = document.createElement("a")
            a.href = item.html_url
            a.text = item.title
            li.appendChild(a)
            element.appendChild(li) 
        })
    })
</script>